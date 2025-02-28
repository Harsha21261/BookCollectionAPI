<<<<<<< HEAD
# BookCollectionAPI
=======
📚 Book Collection API - FastAPI & MongoDB

This project is a Book Management REST API built using FastAPI and MongoDB. The API provides endpoints for adding, retrieving, updating, and deleting books in a database. It follows standard RESTful principles and supports asynchronous database operations using motor.

Features:
•	CRUD Operations: Create, Read, Update, and   Delete books
•	Asynchronous MongoDB Integration using motor
•	RESTful API Endpoints with JSON responses
•	Pydantic Models for request validation
•	Swagger UI & ReDoc for API documentation


Project Overview

*Framework: FastAPI (Asynchronous & High-Performance Web Framework)
*Database: MongoDB (NoSQL Document Database)
*ORM: motor (Asynchronous MongoDB Driver)
*Project Structure: Modular design with routers and services

Project Structure

BookCollectionAPI/
├── main.py
├── models.py
├── routers/
│   ├── books.py
│   └── crud.py
├── venv/
│   ├── Scripts/
│   └── ...
├── playground-1.mongodb.js
├── playground-2.mongodb.js
├── .env
├── requirements.txt
└── README.md
Each component is modularized to follow best practices for maintainability and scalability.

Installation & Setup
Step_1: Download the Project
Ensure the project folder is available on your system. If hosted on GitHub, you can clone it using:
 git clone <repository_url>
 cd BookCollectionAPI
If you are working in a local directory, proceed to the next step.
Step_2:Set Up a Virtual Environment
# Windows (Powershell)
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Step_3:Install Dependencies
pip install -r requirements.txt
If requirements.txt is missing, install dependencies manually:
pip install fastapi uvicorn motor python-dotenv pydantic

Step_4: Set Up MongoDB
Ensure MongoDB is running locally or use MongoDB Atlas (cloud database):
# Start MongoDB (if installed locally)
mongod
Or configure your .env file with a MongoDB connection string:
MONGO_URI=mongodb://localhost:27017
Step_5: Running the API
Start the FastAPI Server
uvicorn main:app --reload
You should see output like:
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
Step6:Access API Documentation
•	Swagger UI (Interactive API docs): http://127.0.0.1:8000/docs
•	ReDoc (Alternative docs): http://127.0.0.1:8000/redoc
🔗 API Endpoints
Method	Endpoint	Description
POST	/books/	Add a new book
GET	/books/	Retrieve all books
GET	/books/{book_id}	Retrieve a book by ID
PUT	/books/{book_id}	Update book details
DELETE	/books/{book_id}	Delete a book
Example API Requests
Create a Book (POST /books/)
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_year": 1925,
  "isbn": "9780743273565"
}
Retrieve All Books (GET /books/)
[
  {
    "id": "65d123abc456ef789",
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "isbn": "9780743273565"
  }
]
Update a Book (PUT /books/{book_id})
{
  "title": "1984",
  "author": "George Orwell",
  "published_year": 1949,
  "isbn": "9780451524935"
}
Delete a Book (DELETE /books/{book_id})
{
  "message": "Book deleted successfully"
}
Future Enhancements
•	Add JWT Authentication for secured access
•	Implement pagination for better performance
•	Support search and filtering options
Author
•	Harsha Vardhan
________________________________________
This project is part of an assignment for [kode blue].



>>>>>>> 76ee090 (Initial commit - FastAPI backend)
