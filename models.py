from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    published_year: int = Field(..., gt=0)
    isbn: str = Field(..., min_length=10, max_length=13)

class BookInDB(Book):
    id: str
