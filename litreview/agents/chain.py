"""A simplistic implementation with no retrieval or chain of thought."""

from pydantic_ai import Agent, RunContext
from ..models.pydai import google_model
from ..types.deps import TaskDependency, Outline, WriterDependency


async def call_write_agent(ctx: RunContext[TaskDependency], outline: Outline) -> str:
    outline_str = f"Question: {outline.question}\n" + "\n".join(
        f"Section title: {item.section_title}\nTheme: {item.theme}\n"
        + "\n".join(f"- {point}" for point in item.points)
        + "\n"
        + "Sources:\n"
        + "\n".join(f"- {source}" for source in item.sources)
        for item in outline.sections
    )
    result = await writer_agent.run(
        outline_str, deps=WriterDependency(outline=outline, task=ctx.deps)
    )
    return result.output


chain_pydai_agent = Agent(
    google_model, output_type=call_write_agent, deps_type=TaskDependency
)

writer_agent = Agent(google_model, deps_type=TaskDependency)


@chain_pydai_agent.instructions
async def outline_instructions(ctx: RunContext[TaskDependency]) -> str:
    """Instructs model to write an outline for the given task and question."""
    task_instructions = ctx.deps.make_instructions()
    return f"You are an expert academic researcher. The user message will consist of an academic question or topic. Based on this question, the goal is to: {task_instructions}. Your immediate task is to write an outline to pass to another agent that will write the final response. The outline should consist of a list of themes, each with 3-5 bullet points and 2-3 academic sources."


@writer_agent.instructions
async def write_instructions(ctx: RunContext[TaskDependency]) -> str:
    """Fill the prompt with the given context."""
    task_instructions = ctx.deps.task.make_instructions()
    return f"You are an expert academic researcher. Your task is: {task_instructions}. The user message will describe the question to address as well as a outline to follow. Please write a comprehensive and well-structured response based on this outline. Your response should be detailed, coherent, and adhere to academic standards. Ensure that you cover all the themes and points mentioned in the outline, and reference the provided sources where appropriate. Your response should be self-contained and make sense to a reader who is not aware of the original question or outline. Please focus on delivering high-quality content that meets the user's needs."
