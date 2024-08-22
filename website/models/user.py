from flask_login import UserMixin
from .. import login_manager, mongo 

@login_manager.user_loader
def load_user(user_id):
    return mongo.db.users.find_one({"_id": user_id})

class User(UserMixin):
    def __init__(self, first_name, last_name, email, username, password, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password_hash = password  # Hash the password

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self._id

    @staticmethod
    def get_by_id(user_id):
        """
        Fetch a user by their unique ID. This is required by Flask-Login to load a user.
        Replace this with the actual database query logic.
        """
        repo = Repository.instance()  # Assuming you're using the singleton pattern from before
        user_data = repo.users.find_one({"_id": user_id})
        if user_data:
            return User(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                username=user_data["username"],
                password=user_data["password_hash"],
                id=user_data["_id"],
            )
        return None

    @staticmethod
    def get_by_username(username):
        """
        Fetch a user by their username. Useful for login functionality.
        Replace this with the actual database query logic.
        """
        repo = Repository.instance()  # Assuming you're using the singleton pattern from before
        user_data = repo.users.find_one({"username": username})
        if user_data:
            return User(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                username=user_data["username"],
                password=user_data["password_hash"],
                id=user_data["_id"],
            )
        return None
    
    @staticmethod
    def get_by_email(email):
        """
        Fetch a user by their username. Useful for login functionality.
        Replace this with the actual database query logic.
        """
        repo = Repository.instance()  # Assuming you're using the singleton pattern from before
        user_data = repo.users.find_one({"email": email})
        if user_data:
            return User(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                email=user_data["email"],
                username=user_data["username"],
                password=user_data["password_hash"],
                id=user_data["_id"],
            )
        return None

    def save_to_db(self):
        """
        Save the user object to the database. This method can be used for new user registrations.
        """
        repo = Repository.instance()  # Assuming you're using the singleton pattern from before
        user_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "username": self.username,
            "password_hash": self.password_hash,
        }
        if self.id is None:
            result = repo.users.insert_one(user_data)
            self.id = result.inserted_id
        else:
            repo.users.update_one({"_id": self.id}, {"$set": user_data})

    def get_id(self):
        """
        This method is required by Flask-Login. It returns the unique ID for the user.
        """
        return str(self.id)  # Convert ObjectId to string if using MongoDB


