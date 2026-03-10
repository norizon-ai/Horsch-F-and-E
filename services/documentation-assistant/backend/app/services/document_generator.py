from openai import OpenAI
from app.config import settings
from typing import List, Dict


class DocumentGenerator:
	"""Generates structured documentation from interview Q&A using OpenAI."""

	def __init__(self):
		self.client = OpenAI(api_key=settings.openai_api_key)

	def generate_document(self, document_type: str, interview_qa: List[Dict]) -> str:
		"""Generate formatted document from interview responses."""

		# Format interview Q&A for the prompt
		qa_text = "\n\n".join([
			f"Q: {qa['question']}\nA: {qa['answer']}"
			for qa in interview_qa
		])

		# Document-type specific templates
		templates = {
			"Work Instruction": self._work_instruction_template(),
			"Architecture Decision Record": self._adr_template(),
			"Custom Documentation": self._custom_template()
		}

		template = templates.get(document_type, self._custom_template())

		prompt = f"""{template}

Interview Responses:
{qa_text}

Based on the interview responses above, generate a complete, professional {document_type} document.

Requirements:
1. Use the appropriate structure for this document type
2. Be detailed and specific based on the interview answers
3. Use professional language
4. Include all relevant information from the interview
5. Format clearly with sections and subsections
6. Make it actionable and clear

Generate the complete document now:"""

		try:
			response = self.client.chat.completions.create(
				model="gpt-4o",
				messages=[
					{
						"role": "system",
						"content": "You are a professional technical writer creating clear, detailed documentation."
					},
					{
						"role": "user",
						"content": prompt
					}
				],
				temperature=0.3,
				max_tokens=3000
			)

			document = response.choices[0].message.content.strip()
			print(f"✅ [DOC GEN] Generated {document_type} ({len(document)} chars)")
			return document

		except Exception as e:
			print(f"❌ [DOC GEN ERROR] {e}")
			raise e

	def generate_checklist(self, document_type: str, document_content: str = "") -> List[str]:
		"""Generate an action checklist based on document type."""

		prompt = f"""Generate a concise action checklist for implementing or using this {document_type}.

Document content:
{document_content[:1000] if document_content else "General checklist for " + document_type}

Requirements:
1. Create 5-10 actionable checklist items
2. Each item should be specific and clear
3. Order them logically (preparation → execution → validation)
4. Keep items concise (1-2 sentences max each)
5. Return ONLY a JSON array of strings

Example format:
["Verify all prerequisites are met", "Review safety protocols", "Execute step 1: Configure settings", ...]

Generate the checklist now:"""

		try:
			response = self.client.chat.completions.create(
				model="gpt-4o",
				response_format={"type": "json_object"},
				messages=[
					{
						"role": "system",
						"content": "You are creating actionable checklists. Return only a JSON object with a 'checklist' array."
					},
					{
						"role": "user",
						"content": prompt
					}
				],
				temperature=0.3
			)

			import json
			result = json.loads(response.choices[0].message.content)
			checklist = result.get("checklist", [])

			print(f"✅ [CHECKLIST] Generated {len(checklist)} items")
			return checklist

		except Exception as e:
			print(f"❌ [CHECKLIST ERROR] {e}")
			raise e

	def _work_instruction_template(self) -> str:
		return """You are creating a Work Instruction document. Use this structure:

# Work Instruction: [Title]

**Document ID:** WI-[YYYY-MM-DD]-[XXX]
**Created by:** [Author]
**Date:** [Date]
**Version:** 1.0

## 1. Purpose
Brief description of what this instruction covers and why it's needed.

## 2. Scope
What is included and what is not included in this instruction.

## 3. Safety & Prerequisites
- Safety requirements
- Required tools/equipment
- Required knowledge/training
- Environmental conditions

## 4. Procedure
Step-by-step instructions with:
- Clear numbering
- One action per step
- Safety warnings where needed
- Quality checkpoints

## 5. Quality Checks
Verification steps and acceptance criteria.

## 6. Troubleshooting
Common issues and solutions.

## 7. References
Related documents, standards, or resources."""

	def _adr_template(self) -> str:
		return """You are creating an Architecture Decision Record (ADR). Use this structure:

# ADR [Number]: [Title]

**Status:** Proposed/Accepted/Deprecated/Superseded
**Date:** [YYYY-MM-DD]
**Decision Makers:** [Names]
**Consulted:** [Names]

## Context
What is the issue we're facing? What factors are driving this decision?

## Decision
What is the change we're proposing and implementing?

## Consequences
What becomes easier or more difficult as a result of this change?

### Positive Consequences
- Benefit 1
- Benefit 2

### Negative Consequences
- Trade-off 1
- Trade-off 2

## Alternatives Considered
What other options were evaluated?

## Implementation Notes
Key considerations for implementation.

## References
Links to related documents, discussions, or resources."""

	def _custom_template(self) -> str:
		return """You are creating custom documentation. Use this flexible structure:

# [Document Title]

**Created by:** [Author]
**Date:** [Date]
**Version:** 1.0

## Overview
High-level summary of the document's purpose and content.

## [Section 1]
Main content organized logically based on the interview responses.

## [Section 2]
Additional content sections as needed.

## Conclusion
Summary and next steps if applicable.

## References
Related documents or resources."""


# Global instance
document_generator = DocumentGenerator()
