import hashlib
import json

def load_db() -> dict:
    with open("db.json","r") as loaded_db:
        return json.load(loaded_db)

def save_db(db):
    with open("db.json","w") as loaded_db:
        json.dump(db,loaded_db)


db = load_db()

def save(username,password):
    passhash = hashlib.sha256(bytes(password,"utf-8")).hexdigest()
    db[username] = passhash    
    save_db(db)

def verify(username,password):
    passhash = hashlib.sha256(bytes(password,"utf-8")).hexdigest()
    try:    
        if db[username] == passhash:
            return True
    except:
        None
    return False