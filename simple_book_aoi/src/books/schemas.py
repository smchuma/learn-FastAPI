from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    publisher_id: str
    published_date: str
    page_count: int
    language: str
    id: int


class BookUpdate(BaseModel):
    title: str
    author: str
    language: str
