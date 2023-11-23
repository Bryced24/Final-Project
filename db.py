from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

# MongoDB URI
uri = "mongodb+srv://bryced24:Antmente0924@finalproject.vbnx9ih.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoClient
client = MongoClient(uri, server_api=ServerApi('1'))

# Database and Collection
db = client.event_management
events_collection = db.events

# Test the connection and print a success message
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)

def add_event(event):
    try:
        event_data = event.to_dict()
        result = events_collection.insert_one(event_data)
        return result.inserted_id
    except Exception as e:
        return f"Error adding event: {e}"

def get_all_events():
    try:
        return list(events_collection.find({}))
    except Exception as e:
        return f"Error retrieving events: {e}"

def update_event(event_id, update_data):
    try:
        result = events_collection.update_one({"_id": ObjectId(event_id)}, {"$set": update_data})
        if result.matched_count == 0:
            return "No event found with the given ID."
        return "Event updated successfully."
    except Exception as e:
        return f"Error updating event: {e}"

def delete_event(event_id):
    try:
        result = events_collection.delete_one({"_id": ObjectId(event_id)})
        if result.deleted_count == 0:
            return "No event found with the given ID."
        return "Event deleted successfully."
    except Exception as e:
        return f"Error deleting event: {e}"
