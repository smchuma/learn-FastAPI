from fastapi import FastAPI
from src.books.routes import router

version = "v1"
app = FastAPI(
    title="Bookly",
    description="A web api for a book review web service",
    version=version,
)


app.include_router(router, prefix=f"/api/{version}/books")
