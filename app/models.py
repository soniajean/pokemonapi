from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
<<<<<<< HEAD
db = SQLAlchemy()

=======

db = SQLAlchemy()
>>>>>>> 931548056e8b0465b13bfc4ef7f04fed0ba2fdfa

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

<<<<<<< HEAD
# as an example for backref
#with the post below
#p1 = Post()
#p1.author

    def __init__(self,username, email, password):
=======
#as an example for backref
#with the post below
# p1 = Post()
# p1.author

    def __init__(self, username, email, password):
>>>>>>> 931548056e8b0465b13bfc4ef7f04fed0ba2fdfa
        self.username = username
        self.email = email
        self.password = password

<<<<<<< HEAD
        def saveUser(self):
            db.session.add(self)
            db.session.commit()

=======
    def saveUser(self):
        db.session.add(self)
        db.session.commit()
>>>>>>> 931548056e8b0465b13bfc4ef7f04fed0ba2fdfa


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String)
    body = db.Column(db.String)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
<<<<<<< HEAD
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #notice user_id is lowercase 

    def __init__(self,title, img_url, body, user_id):
        self.title = title
        self.img_url = img_url
        self.body = body
        self.user_id = user_id
=======
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
                                #  notice          ^^^^^ --> lowercase?  yep.  User.id

    def __init__(self, title, img_url, body, user_id):
        self.title = title
        self.img_url = img_url
        self.body = body
        self.user_id = user_id

>>>>>>> 931548056e8b0465b13bfc4ef7f04fed0ba2fdfa
