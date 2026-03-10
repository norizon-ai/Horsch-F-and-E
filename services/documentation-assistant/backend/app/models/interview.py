from pydantic import BaseModel
from typing import List


class InterviewQA(BaseModel):
	question: str
	answer: str


class InterviewContext(BaseModel):
	steps_identified: int = 0
	safety_warnings: int = 0
	gaps_detected: int = 0
	technical_terms: List[str] = []
	missing_info: List[str] = []
