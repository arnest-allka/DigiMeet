from website import create_app
from pymongo import MongoClient

app = create_app()
client = MongoClient('localhost', 27017)
db = client['database']
users_collection = db['users']


if __name__ == '__main__':
    app.run(debug=True)

