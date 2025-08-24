"""A simplistic implementation with no retrieval or chain of thought."""

from pydantic_ai import Agent, RunContext
from ..models.pydai import google_model
from ..types.deps import TaskDependency

simple_pydai_agent = Agent(
    google_model,
    deps_type=TaskDependency
)

@simple_pydai_agent.instructions
def fill_prompt(ctx: RunContext[TaskDependency]) -> str:
    """Fill the prompt with the given context."""
    task_instructions = ctx.deps.make_instructions()
    return f"You are an expert academic researcher. The user message will consist of an academic question or topic. Your task is: {task_instructions}. Your response should consist of the requested content only, with no additional framing or commentary."