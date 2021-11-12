import os
from app import db
from app import login
import requests 
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.forms import LoginForm, FlaskForm

session = requests.Session()
url = "http://hp-api.herokuapp.com/api/characters"
r = requests.get(url)
data = json.loads(r.text)

fields = [x for x in data[0]]

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    buscas = db.relationship('Busca', backref='usuário', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Busca(db.Model, FlaskForm):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(140))
    alternate_names = db.Column(db.String(140))
    species = db.Column(db.String(140))
    gender = db.Column(db.String(140))
    house = db.Column(db.String(140))
    dateOfBirth = db.Column(db.String(140))
    yearOfBirth = db.Column(db.String(140))
    wizard  = db.Column(db.String(140))
    ancestry = db.Column(db.String(140))
    eyeColour = db.Column(db.String(140))
    hairColour = db.Column(db.String(140))
    wand = db.Column(db.String(140))
    patronus = db.Column(db.String(140))
    hogwartsStudent = db.Column(db.String(140))
    hogwartsStaff = db.Column(db.String(140))
    actor = db.Column(db.String(140))
    alternate_actors = db.Column(db.String(140))
    alive = db.Column(db.String(140))
    image = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Busca {}>'.format(self.name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))