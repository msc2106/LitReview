from pydantic import BaseModel

class Questions(BaseModel):
    social_freedom: str
    civil_society: str
    coercion: str
    meiji_restoration: str

class BasicTemplates(BaseModel):
    theory_comp: str
    lit_review: str