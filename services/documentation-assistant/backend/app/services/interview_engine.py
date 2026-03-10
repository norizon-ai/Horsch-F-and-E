from openai import AsyncOpenAI
from app.config import settings
from app.utils.prompts import get_system_prompt
from app.models import InterviewContext
from typing import List, Tuple


class InterviewEngine:
	"""AI-powered interview engine that generates follow-up questions"""

	def __init__(self):
		self.client = AsyncOpenAI(api_key=settings.openai_api_key)

	async def analyze_transcript(self, transcript: str, doc_type: str, author_name: str = "") -> Tuple[List[str], InterviewContext]:
		"""
		Analyze transcript and generate initial interview questions

		Returns:
			Tuple of (questions_list, context_info)
		"""
		system_prompt = get_system_prompt(doc_type)
		name_instruction = f"Address the user by their first name '{author_name}' in your questions to make the conversation more personal." if author_name else ""

		try:
			# Ask AI to analyze the transcript and generate questions
			response = await self.client.chat.completions.create(
				model="gpt-4o-mini",
				messages=[
					{
						"role": "system",
						"content": system_prompt
					},
					{
						"role": "user",
						"content": f"""Analyze this transcript and generate 5-8 diverse follow-up questions.

Transcript:
{transcript}

CRITICAL REQUIREMENTS:
1. First, identify ALL the main topics, steps, or sections mentioned in the transcript
2. Ensure your questions cover DIFFERENT topics - don't ask 3+ questions about the same narrow area
3. Distribute questions across: beginning → middle → end of the process
4. Each question should address a DIFFERENT aspect or phase
5. Only ask about specific details (like temperature, safety, etc.) if they're clearly relevant to THIS specific process

{name_instruction}

Format your response as JSON:
{{
  "context": {{
    "topics_identified": [<list of main topics/sections found in transcript>],
    "steps_identified": <number>,
    "coverage_gaps": [<list of different areas that need more detail>]
  }},
  "questions": [<list of 5-8 question strings, each covering a DIFFERENT topic/area>]
}}

EXAMPLE of GOOD question distribution (if transcript covers deployment):
1. Prerequisites question
2. Configuration question
3. Deployment steps question
4. Validation question
5. Rollback question

EXAMPLE of BAD question distribution:
1. Temperature during deployment?
2. What temperature is ideal?
3. How do you monitor temperature?
4. Temperature safety limits?
(All about ONE narrow topic!)"""
					}
				],
				response_format={"type": "json_object"},
				temperature=0.8
			)

			import json
			result = json.loads(response.choices[0].message.content)

			# Extract context
			context_data = result.get("context", {})
			context = InterviewContext(
				steps_identified=context_data.get("steps_identified", 0),
				safety_warnings=context_data.get("safety_warnings", 0),
				gaps_detected=context_data.get("gaps_detected", 0),
				missing_info=context_data.get("missing_info", [])
			)

			questions = result.get("questions", [])

			return questions, context

		except Exception as e:
			# Fallback for testing
			mock_context = InterviewContext(
				steps_identified=5,
				safety_warnings=2,
				gaps_detected=3
			)

			mock_questions = [
				"Can you clarify what safety precautions should be taken?",
				"What are the prerequisites before starting this process?",
				"What should someone do if they encounter an error?",
				"Are there any specific tools or equipment required?",
				"What quality checks should be performed?"
			]

			return mock_questions, mock_context

	async def process_answer(
		self,
		conversation_history: List[dict],
		user_answer: str,
		doc_type: str,
		author_name: str = ""
	) -> str:
		"""
		Process user's answer and generate next question

		Args:
			conversation_history: List of {question, answer} pairs
			user_answer: User's latest answer
			doc_type: Document type

		Returns:
			Next question or None if interview complete
		"""
		system_prompt = get_system_prompt(doc_type)
		name_instruction = f"Address the user by their first name '{author_name}' in your question." if author_name else ""

		try:
			# Build conversation context
			messages = [{"role": "system", "content": system_prompt}]

			for qa in conversation_history:
				messages.append({"role": "assistant", "content": qa["question"]})
				messages.append({"role": "user", "content": qa["answer"]})

			# Add instruction for next question
			# Build list of topics already covered
			topics_covered = []
			for qa in conversation_history[-3:]:  # Last 3 questions
				topics_covered.append(qa["question"][:50])  # First 50 chars as identifier

			topics_summary = "\n".join([f"- {t}..." for t in topics_covered]) if topics_covered else "No questions yet"

			messages.append({
				"role": "user",
				"content": f"""Based on the conversation so far, generate ONE more specific follow-up question to improve the documentation.

Recent topics covered:
{topics_summary}

IMPORTANT:
- Ask about a DIFFERENT aspect than the recent questions above
- Cover a new topic area or phase of the process
- Don't ask another variation of what was just discussed
- If we have comprehensive coverage of all major areas, respond with: "INTERVIEW_COMPLETE"

{name_instruction}

Generate ONE new question covering a different aspect, or respond "INTERVIEW_COMPLETE" if sufficient."""
			})

			response = await self.client.chat.completions.create(
				model="gpt-4o-mini",
				messages=messages,
				temperature=0.7,
				max_tokens=200
			)

			next_question = response.choices[0].message.content.strip()

			if "INTERVIEW_COMPLETE" in next_question.upper():
				return None

			return next_question

		except Exception as e:
			# Fallback - end interview after a few questions
			if len(conversation_history) >= 3:
				return None
			return "Can you provide any additional details that might be helpful?"
