from fastapi import FastAPI, status
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from src.books.book_data import books

from typing import List
from src.books.schemas import Book, BookUpdate


router = APIRouter()


@router.get("/", response_model=List[Book])
async def get_all_books():
    return books


@router.post("/create")
async def create_book(data: Book) -> dict:

    new_book = data.model_dump()

    books.append(new_book)

    return new_book


@router.get("/{book_id}")
async def get_single_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found")


@router.patch("/{book_id}")
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


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book removed successfully"}

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found"
        )
