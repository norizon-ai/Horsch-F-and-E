from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import documentation, audio, tts, diagrams
import uvicorn

app = FastAPI(
	title="Documentation Assistant API",
	description="Voice-based documentation creation system",
	version="1.0.0"
)

# Configure CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=settings.cors_origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/")
async def root():
	return {
		"message": "Documentation Assistant API",
		"version": "1.0.0",
		"status": "running"
	}


@app.get("/health")
async def health():
	return {"status": "healthy"}


# Include API routers
app.include_router(documentation.router)
app.include_router(audio.router)
app.include_router(tts.router)
app.include_router(diagrams.router)


if __name__ == "__main__":
	uvicorn.run(
		"app.main:app",
		host="0.0.0.0",
		port=8000,
		reload=True
	)
