"""A simplistic implementation with no retrieval or chain of thought."""

from pydantic_ai import Agent, RunContext
from ..models.pydai import google_model

simple_pydai_agent = Agent(
    google_model,
    deps_type=str
)

@simple_pydai_agent.instructions
def fill_prompt(ctx: RunContext[str]) -> str:
    """Fill the prompt with the given context."""
    return ctx.deps