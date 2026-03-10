from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models import (
	StartSessionRequest,
	ApproveTranscriptRequest,
	InterviewResponseRequest,
	GenerateDocumentRequest,
	PublishDocumentRequest,
	Session,
	SessionState
)
from app.storage.session_manager import SessionManager
from app.services.interview_engine import InterviewEngine
from app.services.transcription import TranscriptionService
from app.services.rabbitmq_publisher import RabbitMQPublisher
from app.services.document_generator import document_generator
from pydantic import BaseModel
from typing import List
import io

router = APIRouter(prefix="/api/documentation", tags=["documentation"])

# Initialize services
interview_engine = InterviewEngine()
rabbitmq_publisher = RabbitMQPublisher()

class DocumentGenerationRequest(BaseModel):
	session_id: str
	document_type: str
	interview_qa: List[dict]


class PDFExportRequest(BaseModel):
	session_id: str
	document_content: str
	author_name: str = ""
	document_type: str = ""
	diagrams: List[dict] = []


class ChecklistRequest(BaseModel):
	session_id: str
	document_type: str


@router.post("/start")
async def start_session(request: StartSessionRequest):
	"""Start a new documentation session"""
	session = SessionManager.create_session(
		author_name=request.author_name,
		document_type=request.document_type
	)

	return {
		"session_id": session.session_id,
		"author_name": session.author_name,
		"document_type": session.document_type,
		"state": session.state
	}


@router.post("/transcript/approve")
async def approve_transcript(request: ApproveTranscriptRequest):
	"""User approves/edits transcript, triggers AI interview"""
	session = SessionManager.get_session(request.session_id)
	if not session:
		raise HTTPException(status_code=404, detail="Session not found")

	# Update session with approved transcript
	SessionManager.update_session(
		request.session_id,
		transcript=request.edited_transcript,
		transcript_edited=True,
		state=SessionState.AI_INTERVIEW
	)

	# Generate interview questions based on transcript
	questions, context = await interview_engine.analyze_transcript(
		transcript=request.edited_transcript,
		doc_type=session.document_type,
		author_name=session.author_name
	)

	# Store first question in session
	if questions:
		SessionManager.update_session(
			request.session_id,
			current_question=questions[0],
			questions_remaining=len(questions)
		)

	return {
		"first_question": questions[0] if questions else None,
		"questions_remaining": len(questions),
		"detected_context": {
			"steps_identified": context.steps_identified,
			"safety_warnings": context.safety_warnings,
			"gaps_detected": context.gaps_detected
		}
	}


@router.post("/interview/respond")
async def submit_interview_response(request: InterviewResponseRequest):
	"""Submit answer to interview question"""
	session = SessionManager.get_session(request.session_id)
	if not session:
		raise HTTPException(status_code=404, detail="Session not found")

	# Add Q&A to history
	qa_entry = {
		"question": session.current_question,
		"answer": request.answer
	}
	session.interview_qa.append(qa_entry)

	# Get next question
	next_question = await interview_engine.process_answer(
		conversation_history=session.interview_qa,
		user_answer=request.answer,
		doc_type=session.document_type,
		author_name=session.author_name
	)

	questions_remaining = session.questions_remaining - 1

	# Force completion if no questions are left
	if questions_remaining <= 0:
		next_question = None

	# Update session
	SessionManager.update_session(
		request.session_id,
		interview_qa=session.interview_qa,
		current_question=next_question,
		questions_remaining=max(0, questions_remaining)
	)

	return {
		"next_question": next_question,
		"questions_remaining": max(0, questions_remaining),
		"completed": next_question is None
	}


@router.post("/document/generate")
async def generate_document_endpoint(request: DocumentGenerationRequest):
	"""Generate final document from interview responses using AI"""
	try:
		document_content = document_generator.generate_document(
			document_type=request.document_type,
			interview_qa=request.interview_qa
		)

		return {
			"document": document_content,
			"status": "success"
		}
	except Exception as e:
		print(f"❌ [GENERATE DOC ERROR] {e}")
		raise HTTPException(status_code=500, detail=str(e))


@router.post("/document/publish")
async def publish_document(request: PublishDocumentRequest):
	"""Publish document to knowledge base via RabbitMQ"""
	session = SessionManager.get_session(request.session_id)
	if not session:
		raise HTTPException(status_code=404, detail="Session not found")

	# Try to publish to RabbitMQ (optional - won't fail if RabbitMQ is unavailable)
	rabbitmq_success = False
	try:
		rabbitmq_success = rabbitmq_publisher.publish_document(request.final_document)
		if rabbitmq_success:
			print(f"✅ [PUBLISH] Document {request.final_document.get('id')} published to RabbitMQ")
		else:
			print(f"⚠️  [PUBLISH] RabbitMQ publish failed (connection issue) - continuing anyway")
	except Exception as e:
		print(f"⚠️  [PUBLISH] RabbitMQ error: {e} - continuing anyway")

	# Mark session as completed (regardless of RabbitMQ status)
	SessionManager.update_session(
		request.session_id,
		state=SessionState.COMPLETED
	)

	return {
		"status": "completed" if not rabbitmq_success else "published",
		"document_id": request.final_document.get("id", "unknown"),
		"message": "Document completed successfully" + (" and published to knowledge base" if rabbitmq_success else " (RabbitMQ unavailable)")
	}


@router.get("/session/{session_id}")
async def get_session(session_id: str):
	"""Get session details"""
	session = SessionManager.get_session(session_id)
	if not session:
		raise HTTPException(status_code=404, detail="Session not found")

	return session


@router.post("/export-pdf")
async def export_pdf(request: PDFExportRequest):
	"""Export document as PDF with enhanced aesthetics"""
	print(f"📄 [PDF] Export request - Diagrams count: {len(request.diagrams) if request.diagrams else 0}")
	if request.diagrams:
		for idx, diag in enumerate(request.diagrams, 1):
			print(f"   Diagram {idx}: title='{diag.get('title', 'N/A')}', has_svg={bool(diag.get('svg'))}")

	try:
		from reportlab.lib.pagesizes import letter
		from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image as RLImage
		from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
		from reportlab.lib.units import inch
		from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
		from reportlab.lib import colors
		from reportlab.pdfgen import canvas
		from datetime import datetime
		import os

		# Path to logo
		logo_path = os.path.join(os.path.dirname(__file__), "..", "static", "norizon-logo.png")

		# Custom canvas class for header/footer with logo
		class LogoCanvas(canvas.Canvas):
			def __init__(self, *args, **kwargs):
				canvas.Canvas.__init__(self, *args, **kwargs)
				self.pages = []

			def showPage(self):
				self.pages.append(dict(self.__dict__))
				self._startPage()

			def save(self):
				page_count = len(self.pages)
				for page_num, page in enumerate(self.pages, 1):
					self.__dict__.update(page)

					# Add small logo to top left on every page except the first
					if page_num > 1 and os.path.exists(logo_path):
						self.drawImage(logo_path, 0.5*inch, letter[1] - 0.8*inch,
									   width=1.2*inch, height=0.4*inch,
									   preserveAspectRatio=True, mask='auto')

					# Add page number at bottom
					self.setFont('Helvetica', 9)
					self.setFillColor(colors.HexColor('#6b7280'))
					self.drawRightString(letter[0] - 0.5*inch, 0.5*inch, f"Page {page_num} of {page_count}")

					canvas.Canvas.showPage(self)
				canvas.Canvas.save(self)

		# Create PDF in memory
		buffer = io.BytesIO()
		doc = SimpleDocTemplate(
			buffer,
			pagesize=letter,
			rightMargin=72,
			leftMargin=72,
			topMargin=90,  # Increased to accommodate logo
			bottomMargin=50,
			title=f"{request.document_type} - {request.author_name}",
			author=request.author_name
		)

		# Container for the 'Flowable' objects
		elements = []

		# Define enhanced styles
		styles = getSampleStyleSheet()

		# Custom title style
		styles.add(ParagraphStyle(
			name='CustomTitle',
			parent=styles['Title'],
			fontSize=24,
			textColor=colors.HexColor('#1e3a8a'),
			spaceAfter=12,
			alignment=TA_CENTER,
			fontName='Helvetica-Bold'
		))

		# Custom heading styles
		styles.add(ParagraphStyle(
			name='CustomHeading1',
			parent=styles['Heading1'],
			fontSize=16,
			textColor=colors.HexColor('#2563eb'),
			spaceAfter=10,
			spaceBefore=15,
			fontName='Helvetica-Bold'
		))

		styles.add(ParagraphStyle(
			name='CustomHeading2',
			parent=styles['Heading2'],
			fontSize=14,
			textColor=colors.HexColor('#3b82f6'),
			spaceAfter=8,
			spaceBefore=12,
			fontName='Helvetica-Bold'
		))

		# Custom body style
		styles.add(ParagraphStyle(
			name='CustomBody',
			parent=styles['BodyText'],
			fontSize=11,
			leading=16,
			alignment=TA_JUSTIFY,
			textColor=colors.HexColor('#1f2937')
		))

		# Metadata style
		styles.add(ParagraphStyle(
			name='Metadata',
			fontSize=10,
			textColor=colors.HexColor('#6b7280'),
			alignment=TA_CENTER,
			spaceAfter=20
		))

		# Add large logo at the top of first page (preserve aspect ratio)
		if os.path.exists(logo_path):
			logo = RLImage(logo_path)
			# Calculate proper height based on aspect ratio
			# Set max width to 3 inches and calculate proportional height
			max_logo_width = 3*inch
			aspect_ratio = logo.imageHeight / float(logo.imageWidth)
			logo.drawWidth = max_logo_width
			logo.drawHeight = max_logo_width * aspect_ratio
			elements.append(logo)
			elements.append(Spacer(1, 0.3*inch))
		else:
			elements.append(Spacer(1, 0.3*inch))

		# Add metadata header (Author, Date, Document Type)
		current_date = datetime.now().strftime("%B %d, %Y")
		if request.author_name:
			elements.append(Paragraph(f"<b>Author:</b> {request.author_name}", styles['Metadata']))
		elements.append(Paragraph(f"<b>Date:</b> {current_date}", styles['Metadata']))
		if request.document_type:
			elements.append(Paragraph(f"<b>Document Type:</b> {request.document_type}", styles['Metadata']))

		# Add separator line
		elements.append(Spacer(1, 0.2*inch))
		line_data = [['']]
		line_table = Table(line_data, colWidths=[6.5*inch])
		line_table.setStyle(TableStyle([
			('LINEABOVE', (0, 0), (-1, 0), 2, colors.HexColor('#3b82f6')),
		]))
		elements.append(line_table)
		elements.append(Spacer(1, 0.3*inch))

		# Parse and add document content
		lines = request.document_content.split('\n')
		for line in lines:
			# Skip duplicate metadata lines that are in the generated content
			line_lower = line.strip().lower()
			if (line_lower.startswith('created by:') or
				line_lower.startswith('author:') or
				line_lower.startswith('date:') or
				line_lower.startswith('**created by:**') or
				line_lower.startswith('**author:**') or
				line_lower.startswith('**date:**')):
				continue

			if line.startswith('# '):
				# H1 - Title
				elements.append(Paragraph(line[2:], styles['CustomTitle']))
				elements.append(Spacer(1, 0.2*inch))
			elif line.startswith('## '):
				# H2 - Heading
				elements.append(Paragraph(line[3:], styles['CustomHeading1']))
				elements.append(Spacer(1, 0.1*inch))
			elif line.startswith('### '):
				# H3 - Subheading
				elements.append(Paragraph(line[4:], styles['CustomHeading2']))
				elements.append(Spacer(1, 0.08*inch))
			elif line.strip().startswith('**') and line.strip().endswith('**'):
				# Bold text
				clean_line = line.strip()[2:-2]
				elements.append(Paragraph(f"<b>{clean_line}</b>", styles['CustomBody']))
			elif line.strip().startswith('- '):
				# Bullet point
				elements.append(Paragraph(f"• {line.strip()[2:]}", styles['CustomBody']))
			elif line.strip():
				# Regular paragraph
				elements.append(Paragraph(line, styles['CustomBody']))
			else:
				# Empty line
				elements.append(Spacer(1, 0.12*inch))

		# Add diagrams section if diagrams are provided
		if request.diagrams and len(request.diagrams) > 0:
			elements.append(PageBreak())
			elements.append(Paragraph("Generated Diagrams", styles['CustomTitle']))
			elements.append(Spacer(1, 0.3*inch))

			for idx, diagram in enumerate(request.diagrams, 1):
				try:
					# Add diagram title
					diagram_title = diagram.get('title', f'Diagram {idx}')
					elements.append(Paragraph(diagram_title, styles['CustomHeading1']))
					elements.append(Spacer(1, 0.2*inch))

					# Get SVG from diagram
					svg_content = diagram.get('svg', '')

					if svg_content:
						try:
							# Convert SVG to PNG using cairosvg (more robust than svglib)
							import tempfile
							import cairosvg

							# Create temporary files
							with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_png:
								tmp_png_path = tmp_png.name

							try:
								# Convert SVG to PNG
								cairosvg.svg2png(bytestring=svg_content.encode('utf-8'),
												write_to=tmp_png_path,
												output_width=800)  # Max width in pixels

								# Open PNG and add to PDF
								img = RLImage(tmp_png_path)

								# Scale to fit page (max 6 inches wide)
								max_width = 6 * inch
								aspect = img.imageHeight / float(img.imageWidth)

								if img.imageWidth > max_width:
									img.drawWidth = max_width
									img.drawHeight = max_width * aspect
								else:
									img.drawWidth = img.imageWidth * 0.75  # Convert pixels to points
									img.drawHeight = img.imageHeight * 0.75

								elements.append(img)
								print(f"✅ [PDF] Successfully rendered diagram {idx}")

							except Exception as conv_err:
								print(f"❌ [PDF] Error converting SVG to PNG for diagram {idx}: {conv_err}")
								import traceback
								traceback.print_exc()
								# Fallback message
								elements.append(Paragraph(
									f"<i>Diagram preview available in digital format</i>",
									styles['Normal']
								))

							# Clean up temp file
							try:
								os.unlink(tmp_png_path)
							except:
								pass

						except Exception as e:
							print(f"❌ [PDF] Error rendering diagram {idx}: {e}")
							import traceback
							traceback.print_exc()
							# Fallback: show placeholder message
							elements.append(Paragraph(
								f"<i>Diagram preview available in digital format</i>",
								styles['Normal']
							))
					else:
						# No SVG available
						elements.append(Paragraph(
							"<i>No diagram visualization available</i>",
							styles['Normal']
						))

					elements.append(Spacer(1, 0.4*inch))

				except Exception as e:
					print(f"❌ [PDF] Error processing diagram {idx}: {e}")
					import traceback
					traceback.print_exc()
					# Continue with next diagram
					continue

		# Add footer
		elements.append(Spacer(1, 0.5*inch))

		# Add separator line for footer
		footer_line_data = [['']]
		footer_line_table = Table(footer_line_data, colWidths=[6.5*inch])
		footer_line_table.setStyle(TableStyle([
			('LINEABOVE', (0, 0), (-1, 0), 1, colors.HexColor('#d1d5db')),
		]))
		elements.append(footer_line_table)
		elements.append(Spacer(1, 0.1*inch))
		elements.append(Paragraph(
			"Generated with Documentation Assistant",
			styles['Metadata']
		))

		# Build PDF with custom canvas
		doc.build(elements, canvasmaker=LogoCanvas)

		# Get PDF content
		pdf_content = buffer.getvalue()
		buffer.close()

		print(f"✅ [PDF] Generated PDF ({len(pdf_content)} bytes) for {request.author_name}")

		filename = f"{request.document_type.replace(' ', '-')}-{request.author_name.replace(' ', '-')}-{datetime.now().strftime('%Y%m%d')}.pdf"

		return StreamingResponse(
			io.BytesIO(pdf_content),
			media_type="application/pdf",
			headers={"Content-Disposition": f"attachment; filename={filename}"}
		)
	except Exception as e:
		print(f"❌ [PDF ERROR] {e}")
		import traceback
		print(traceback.format_exc())
		raise HTTPException(status_code=500, detail=str(e))


@router.post("/checklist/generate")
async def generate_checklist(request: ChecklistRequest):
	"""Generate action checklist for the document"""
	try:
		checklist = document_generator.generate_checklist(
			document_type=request.document_type,
			document_content=""
		)

		return {
			"checklist": checklist,
			"status": "success"
		}
	except Exception as e:
		print(f"❌ [CHECKLIST ERROR] {e}")
		raise HTTPException(status_code=500, detail=str(e))
