import json
import os

DB_FILE = "password_db.json"

def load_database():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    else:
        new_db = {}
        save_database(new_db)
        return new_db

def save_database(db):
    with open(DB_FILE, "w") as file:
        json.dump(db, file, indent=4)