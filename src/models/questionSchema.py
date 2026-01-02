from typing import List
from pydantic import BaseModel, Field, validator


class McqQuestion(BaseModel):
    
    question:str = Field(description="the question text")
    options:List[str] = Field(description="List of 4 options")
    correct_answer:str = Field(description="The correct answer from the options")

    @validator('question',pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description',str(v))
        return str(v)
    
class FillBlankQuestion(BaseModel):

    question:str = Field(description="the question text with  '_____' for the blank")
    correct_answer:str =Field(description="correct word or phrase for the blank")

    @validator('question',pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description',str(v))
        return str(v)

