from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.providers.together import TogetherProvider
from ..types.config import GoogleGeminiConfig, TogetherAIConfig

def google_provider(config: GoogleGeminiConfig):
    return GoogleProvider(
        vertexai=True,
        project=config.project,
        location=config.location,
    )

def google_model(config: GoogleGeminiConfig):
    return GoogleModel(
        model_name=config.model_name,
        provider=google_provider(config),
    )

def together_provider(config: TogetherAIConfig):
    return TogetherProvider(
        api_key=config.api_key,
    )