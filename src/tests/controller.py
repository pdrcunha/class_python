import requests
import random
from user_service import UserService

class Controller:
    def __init__(self):
        self.baseName = "/asada"
    
    def run(self):
        self.post(self.get())

    def post(self, data):
        return requests.post(self.baseName, data=data)
    
    def get(self):
        return requests.get("http://meka.com/me")

class UserController:
    def __init__(self):
        self.service = UserService()
    
    def welcome_user(self, user_id):
        user = self.service.get_user(user_id)
        return f"Welcome, {user['name']}!"

def pick_winner():
    return random.choice(["Alice", "Bob", "Joyce"])
