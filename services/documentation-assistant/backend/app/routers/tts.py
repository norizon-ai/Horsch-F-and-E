from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from openai import OpenAI
import traceback
from app.config import settings

router = APIRouter(prefix="/api/tts", tags=["tts"])


class TTSRequest(BaseModel):
	text: str


@router.post("/generate")
async def generate_speech(request: TTSRequest):
	"""Generate natural speech using OpenAI TTS."""
	print("🎤 [TTS] Endpoint HIT!")
	text = request.text

	if not text:
		raise HTTPException(status_code=400, detail="No text provided")

	api_key = settings.openai_api_key
	if not api_key:
		raise HTTPException(status_code=500, detail="OPENAI_API_KEY not configured")

	print(f"🎤 [TTS] API Key loaded: {api_key[:10]}...")
	client = OpenAI(api_key=api_key)

	try:
		print(f"🎤 [TTS] Calling OpenAI API for text: {text[:50]}...")
		response = client.audio.speech.create(
			model="tts-1",
			voice="nova",
			input=text,
			speed=0.95
		)

		print(f"🎤 [TTS] OpenAI response received, type: {type(response)}")
		print(f"🎤 [TTS] Response content length: {len(response.content) if hasattr(response, 'content') else 'N/A'}")

		# Stream the audio back
		return StreamingResponse(
			iter([response.content]),
			media_type="audio/mpeg"
		)
	except Exception as e:
		print(f"❌ [TTS ERROR] {e}")
		print(f"❌ [TTS TRACEBACK] {traceback.format_exc()}")
		raise HTTPException(status_code=500, detail=str(e))
