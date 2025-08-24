from pydantic import BaseModel
from typing import Literal
from .prompts import BasicTemplates

class TaskDependency(BaseModel):
    task_description: Literal['exam', 'lit_review']

    def instructions(self) -> str:
        if self.task_description == 'exam':
            return BasicTemplates().theory_comp
        elif self.task_description == 'lit_review':
            return BasicTemplates().lit_review
        else:
            raise ValueError(f"Unknown task description: {self.task_description}")

class OutlineItem(BaseModel):
    section_title: str
    theme: str
    points: list[str]
    sources: list[str]

class Outline(BaseModel):
    question: str
    sections: list[OutlineItem]

class WriterDependency(BaseModel):
    outline: Outline
    task: TaskDependency