
from fastapi import APIRouter, HTTPException, status
from crud import create_book, get_books, get_book, update_book, delete_book
from models import Book
import routers.books as books



router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(book: Book):
    book_id = await create_book(book)
    return {"message": "Book added", "id": book_id}

@router.get("/")
async def list_books():
    return await get_books()

@router.get("/{book_id}")
async def retrieve_book(book_id: str):
    book = await get_book(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/{book_id}")
async def edit_book(book_id: str, book: Book):
    if await update_book(book_id, book):
        return {"message": "Book updated"}
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}")
async def remove_book(book_id: str):
    if await delete_book(book_id):
        return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
