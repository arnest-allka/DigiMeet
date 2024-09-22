from bson import ObjectId
from .. import mongo

class Event():
    def __init__(self, event_data):
        self.id = str(event_data["_id"])
        self.name = event_data["name"]
        self.description = event_data["description"]
        self.date = event_data["date"]
        self.time = event_data["time"]
        self.place = event_data["place"]
        self.type = event_data["type"]
        self.user_id = str(event_data["user_id"])
        self.participants = event_data.get("participants", [])
        
    @staticmethod
    def create_event(name, description, date, time, place, type, user_id):
        event_id = mongo.db.events.insert_one({
            "name": name,
            "description": description,
            "date": date,
            "time": time,
            "place": place,
            "type": type,
            "user_id": user_id,
            "participants": [],
        }).inserted_id
        return str(event_id)
    
    @staticmethod
    def find_by_id(event_id):
        event_data = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        if event_data:
            return Event(event_data)
        return None

    @staticmethod
    def find_by_name(event_name):
        event_data = mongo.db.events.find_one({"name": event_name})
        if event_data:
            return Event(event_data)
        return None
    
    @staticmethod
    def get_events():
        events = mongo.db.events.find()
        return [Event(event) for event in events]

    @staticmethod
    def find_by_user_id(user_id):
        events = mongo.db.events.find({"user_id": user_id})
        return [Event(event) for event in events]

    @staticmethod
    def delete_event(event_id):
        result = mongo.db.events.delete_one({"_id": ObjectId(event_id)})
        if result.deleted_count == 0:
            return False
        return True
    
    @staticmethod
    def find_by_participant(user_id):
        result = []
        events = mongo.db.events.find({"participants.user_id": ObjectId(user_id)})
        for event in events:
            for participant in event['participants']:
                if participant['user_id'] == ObjectId(user_id):
                    result.append((Event(event), participant['status']))
        return result
        

    @staticmethod
    def add_participant(event_id, user, status):
        event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        
        if event:
            # Check if the user is already in the participants list
            participant_entry = next((p for p in event.get('participants', []) if p['user_id'] == ObjectId(user.id)), None)

            if participant_entry:
                if status == "not":
                    mongo.db.events.update_one(
                        {"_id": ObjectId(event_id), "participants.user_id": ObjectId(user.id)},
                        {"$pull": {"participants": {"user_id": ObjectId(user.id)}}}
                    )
                else:
                    mongo.db.events.update_one(
                        {"_id": ObjectId(event_id), "participants.user_id": ObjectId(user.id)},
                        {"$set": {"participants.$.status": status}}
                    )
            else:
                if status != "not":
                    mongo.db.events.update_one(
                        {"_id": ObjectId(event_id)},
                        {"$push": {"participants": {"user_id": ObjectId(user.id), "first_name": user.first_name, "last_name": user.last_name, "status": status}}}
                    )
            return True
        return False
    
    @staticmethod
    def update_event(event_id, updates):
        event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        if event:
            mongo.db.events.update_one(
                {"_id": ObjectId(event_id)}, 
                {"$set": updates}
            )
            
    @staticmethod
    def search_events(title, place, type):
        query = {}
    
        if title:
            query['name'] = {'$regex': title, '$options': 'i'}  # Case-insensitive search for title
        if place:
            query['place'] = {'$regex': place, '$options': 'i'}  
        if type:
            query['type'] = {'$regex': type, '$options': 'i'}

        events = mongo.db.events.find(query)

        # Convert MongoDB event data to Event objects
        return [Event(event) for event in events]

    @staticmethod
    def remove_participant_from_events(user_id):
        events = mongo.db.events.find({"participants.user_id": ObjectId(user_id)})
        
        if events:
            for event in events:
                mongo.db.events.update_one(
                    {"_id": event["_id"]}, 
                    {"$pull": {"participants": {"user_id": ObjectId(user_id)}}}
                )

    @staticmethod
    def delete_events_by_owner(user_id):
        # Find all events created by the user
        events = mongo.db.events.find({"user_id": user_id})

        if events:
            for event in events:
                print(event['_id'])
                # Delete each event found
                mongo.db.events.delete_one({"_id": event["_id"]})
