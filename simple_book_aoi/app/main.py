from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Things Fall Apart",
        "author": "Chinua Achebe",
        "publisher_id": "PUB006",
        "published_date": "1958-06-17",
        "page_count": 209,
        "language": "en",
    }
]


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


# api endpoints


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/book")
async def create_book(data: Book) -> dict:

    new_book = data.model_dump()

    books.append(new_book)

    return new_book


@app.get("/book/{book_id}")
async def get_single_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found")


@app.patch("/book/{book_id}")
async def update_book(book_id: int, data: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            book["title"] = (data.title,)
            book["author"] = (data.author,)
            book["language"] = (data.language,)
            return book
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found"
        )


@app.delete("/book/{book_id}")
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book removed successfully"}

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found"
        )
