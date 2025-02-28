from fastapi import FastAPI
from routers import books
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId

# Initialize FastAPI app
app = FastAPI()
app.include_router(books.router)
# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
database = client.bookstore
collection = database.books

# Pydantic model for Book
class Book(BaseModel):
    title: str
    author: str
    published_year: int
    isbn: str

# Helper function to convert MongoDB document to Python dict
def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "published_year": book["published_year"],
        "isbn": book["isbn"],
    }

# Create a new book
@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    book_dict = book.dict()
    # Check if ISBN already exists
    if await collection.find_one({"isbn": book_dict["isbn"]}):
        raise HTTPException(status_code=400, detail="ISBN already exists")
    # Insert the book into the database
    new_book = await collection.insert_one(book_dict)
    created_book = await collection.find_one({"_id": new_book.inserted_id})
    return book_helper(created_book)

# Get all books
@app.get("/books/", response_model=list[Book])
async def get_books():
    books = []
    async for book in collection.find():
        books.append(book_helper(book))
    return books

# Get a specific book by ID
@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: str):
    book = await collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return book_helper(book)
    raise HTTPException(status_code=404, detail="Book not found")

# Update a book
@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: str, book: Book):
    book_dict = book.dict()
    # Check if the book exists
    existing_book = await collection.find_one({"_id": ObjectId(book_id)})
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    # Update the book
    await collection.update_one({"_id": ObjectId(book_id)}, {"$set": book_dict})
    updated_book = await collection.find_one({"_id": ObjectId(book_id)})
    return book_helper(updated_book)

# Delete a book
@app.delete("/books/{book_id}")
async def delete_book(book_id: str):
    # Check if the book exists
    existing_book = await collection.find_one({"_id": ObjectId(book_id)})
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    # Delete the book
    await collection.delete_one({"_id": ObjectId(book_id)})
    return {"message": "Book deleted successfully"}