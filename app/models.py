import os

from werkzeug import datastructures
from app import db
from app import login
import requests 
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

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

class Personagens():
    session = requests.Session()
    url = "http://hp-api.herokuapp.com/api/characters"
    r = requests.get(url)
    datas = json.loads(r.text)

    for data in datas:
        name = data['name']
        gender = data['gender']
        house = data['house']
        actor = data['actor']

    

    def __repr__(self):
        return '<Busca {}>'.format(self.name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))