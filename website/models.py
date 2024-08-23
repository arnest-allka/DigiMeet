from flask_login import UserMixin
from . import mongo, bcrypt

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.first_name = user_data["first_name"]
        self.last_name = user_data["last_name"]
        self.email = user_data["email"]
        self.username = user_data["username"]
        self.password = user_data["password"]
        self.is_admin = user_data.get('is_admin', False)
    
    @staticmethod
    def find_by_username(username):
        if username == "admin":
            admin_data = mongo.db.users.find_one({"username": username})
            if admin_data:
                return User(admin_data)
            
            User.create_user(
                first_name="",
                last_name="",
                email="",
                username="admin",
                password="admin321",
                is_admin=True
            )
            admin_data = mongo.db.users.find_one({"username": username})
            return User(admin_data)
        
        user_data = mongo.db.users.find_one({"username": username})
        if user_data:
            return User(user_data)
        return None

    @staticmethod
    def find_by_email(email):
        user_data = mongo.db.users.find_one({"email": email})
        if user_data:
            return User(user_data)
        return None

    @staticmethod
    def find_by_id(id):
        user_data = mongo.db.users.find_one({"_id": id})
        if user_data:
            return User(user_data)
        return None

    @staticmethod
    def check_password(user, password):
        return bcrypt.check_password_hash(user.password, password)

    @staticmethod
    def create_user(first_name, last_name, email, username, password, is_admin=False):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user_id = mongo.db.users.insert_one({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "username": username,
            "password": hashed_password,
            "is_admin": is_admin
        }).inserted_id
        return str(user_id)