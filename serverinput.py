from flask import Flask
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://arpulivarthi:invincible@Agriculture.mongodb.net/AgriHack?retryWrites=true&w=majority'
mongo = PyMongo(app)

hashed_password = generate_password_hash('user123')

new_user = {
    "username": "user123",
    "password": hashed_password,
    "email": "user123@example.com",
    "first_name": "user",
    "last_name": "123",
    "created_at": datetime.utcnow()
}

mongo.db.users.insert_one(new_user)
