from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    id: int = Field(description="Not required", default=None)
    title: str = Field(min_length=3, max_length=150)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=350)
    rating: int = Field(gt=0,lt=6)
    published_date: int = Field(gt=1999)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Thinking, Fast and Slow",
                "author": "Daniel Kahneman",
                "category": "Psychology",
                "description": "An exploration of the two systems that drive human thought.",
                "rating": 4,
                "published_date": 2012,
            }
        }
    }