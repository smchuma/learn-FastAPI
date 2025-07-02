from fastapi import FastAPI
from pydantic import BaseModel 
from typing import List

app = FastAPI()




class Book(BaseModel):
    title: str
    author: str
    publisher_id: int
    published_date: str
    page_count: int
    language: str
    id: int


# api endpoints

@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books

@app.get("/book/{book_id}")
async def get_single_book(book_id: int):
    pass


@app.post("/book/{book_id}")
async def create_book(book_id: int):
    pass

@app.patch("/book/{book_id}")
async def update_book(book_id : int):
    pass

@app.delete("/book/{book_id}")
async def delete_book(book_id : int):
    pass