from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "bookstore"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]
books_collection = database.get_collection("books")
