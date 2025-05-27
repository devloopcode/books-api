from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: int = None
    title: str = Field(min_length=3, max_length=150)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=350)
    rating: int = Field(gt=-1,lt=6)