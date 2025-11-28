from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.core.config import settings

# -----------------------------------------
# MongoDB Client Initialization
# -----------------------------------------
class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

mongodb = MongoDB()


async def connect_to_mongo():
    """
    Connect to MongoDB when FastAPI starts.
    """
    mongodb.client = AsyncIOMotorClient(settings.MONGO_URI)
    mongodb.db = mongodb.client[settings.MONGO_DB_NAME]
    print("Connected to MongoDB:", settings.MONGO_URI)


async def close_mongo_connection():
    """
    Close MongoDB connection when FastAPI shuts down.
    """
    mongodb.client.close()
    print("MongoDB connection closed.")


# -----------------------------------------
# Utility converter for BSON ObjectId
# -----------------------------------------

def serialize_doc(doc):
    """
    Converts MongoDB document to JSON-serializable dict.
    """
    if not doc:
        return None

    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


def serialize_list(docs):
    """
    Converts multiple documents to JSON list.
    """
    return [serialize_doc(doc) for doc in docs]


# -----------------------------------------
# Collection getters
# -----------------------------------------

def get_user_collection():
    return mongodb.db.get_collection("users")

def get_prediction_collection():
    return mongodb.db.get_collection("predictions")

def get_logs_collection():
    return mongodb.db.get_collection("logs")

def get_metadata_collection():
    return mongodb.db.get_collection("model_metadata")
