from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

# Get environment variables
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]



product_collection = database["products"]

# Optional: To test connection
async def test_connection():
    try:
        await client.admin.command("ping")
        print("Connected to MongoDB Atlas successfully!")
    except Exception as e:
        print("MongoDB connection error:", e)