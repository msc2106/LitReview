from pydantic import BaseModel

class GoogleGeminiConfig(BaseModel):
    project: str
    location: str
    model_name: str

class TogetherAIModels(BaseModel):
    ...

class TogetherAIConfig(BaseModel):
    api_key: str
    model_name: str