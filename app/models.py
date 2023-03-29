from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.utcnow)

    def __init__(self, username, email, password, id):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password) 
        #self.password = password   ---OLD  not hashed
        self.id = id

    def saveUser(self):
        db.session.add(self)
        db.session.commit()
        
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    ability = db.Column(db.String, nullable=False, unique=True)
    base_xp = db.Column(db.Integer, nullable=False)
    front_shiny = db.Column(db.String, nullable=False, unique=True)
    base_atk = db.Column(db.Integer, nullable=False)
    base_hp = db.Column(db.Integer, nullable=False)
    base_def = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, ability, base_xp, front_shiny, base_atk, base_hp, base_def):
        self.name = name
        self.ability = ability
        self.base_xp = base_xp
        self.front_shiny = front_shiny
        self.base_atk = base_atk
        self.base_hp = base_hp
        self.base_def = base_def

    def savePokemon(self):
        db.session.add(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()