from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
	# OpenAI
	openai_api_key: str

	# RabbitMQ
	rabbitmq_host: str = "localhost"
	rabbitmq_port: int = 5672
	rabbitmq_user: str = "guest"
	rabbitmq_password: str = "guest"
	rabbitmq_queue: str = "knowledge_queue"

	# Storage
	session_storage_path: str = "./data/sessions"
	audio_storage_path: str = "./data/audio"

	# CORS
	cors_origins: List[str] = ["http://localhost:5173", "http://localhost:5174"]

	class Config:
		env_file = ".env"
		case_sensitive = False


settings = Settings()
