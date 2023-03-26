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
  

#as an example for backref
#with the post below
# p1 = Post()
# p1.author

    def __init__(self, username, email, password, id):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password) 
        #self.password = password   ---OLD  not hashed
        self.id = id

    def saveUser(self):
        db.session.add(self)
        db.session.commit()
        