from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re
import json
from openai import OpenAI
from app.config import settings

router = APIRouter(prefix="/api/diagrams", tags=["diagrams"])


class DiagramRequest(BaseModel):
	text: str
	session_id: str

def sanitize_mermaid_code(code: str) -> str:
    """Sanitizes node labels in Mermaid code to prevent syntax errors."""
    def sanitize_label(match):
        # Keep only letters, numbers, spaces, and hyphens
        sanitized_text = re.sub(r'[^a-zA-Z0-9 -]', '', match.group(1))
        # Mermaid requires quotes for labels with spaces or special characters
        return f'["{sanitized_text}"]'
    
    # This regex finds content within brackets `[...]` which are node labels
    return re.sub(r'\[(.*?)\]', sanitize_label, code)

@router.post("/generate")
async def generate_diagram(request: DiagramRequest):
	"""Generate Mermaid diagram from text description."""

	api_key = settings.openai_api_key
	if not api_key:
		raise HTTPException(status_code=500, detail="OPENAI_API_KEY not configured")

	client = OpenAI(api_key=api_key)

	prompt = f"""
Extract the process flow from this text and generate a title and Mermaid diagram syntax.

Text: {request.text}

Rules:
1. Generate a concise, descriptive title for the diagram (5-10 words).
2. Generate the Mermaid diagram syntax based on the process flow.
3. Return a valid JSON object with two keys: "title" and "mermaid_code".

Example output format:
{{
	 "title": "Data Processing Workflow",
	 "mermaid_code": "graph LR\\n    A[Data Ingestion] --> B[Preprocessing]\\n    B --> C[Model Training]"
}}
"""
	try:
		response = client.chat.completions.create(
			model="gpt-4o",
			response_format={"type": "json_object"},
			messages=[{
				"role": "user",
				"content": prompt
			}],
			temperature=0.3
		)

		content = response.choices[0].message.content.strip()
		
		try:
			diagram_data = json.loads(content)
			title = diagram_data.get("title", "Process Diagram")
			mermaid_code = diagram_data.get("mermaid_code", "")
		except json.JSONDecodeError:
			raise HTTPException(status_code=500, detail="Failed to parse diagram JSON from AI response")

		# Clean up the response (remove markdown code blocks if present)
		if mermaid_code.startswith('```'):
			lines = mermaid_code.split('\n')
			mermaid_code = '\n'.join(lines[1:-1]) if len(lines) > 2 else mermaid_code

		sanitized_code = sanitize_mermaid_code(mermaid_code)

		print(f"✅ [DIAGRAM] Generated '{title}':\n{sanitized_code}")

		return {
			"title": title,
			"mermaid_code": sanitized_code,
			"status": "success"
		}
	except Exception as e:
		print(f"❌ [DIAGRAM ERROR] {e}")
		raise HTTPException(status_code=500, detail=str(e))
