from pydantic import BaseModel

class GoogleGeminiConfig(BaseModel):
    project: str
    location: str

class TogetherAIConfig(BaseModel):
    api_key: str