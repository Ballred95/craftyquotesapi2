from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
import io
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://gnarbcujgezqwy:da1382c414ee750b237f9f93b33c7c0b54e941ed49e85aee5896f57af1140798@ec2-54-161-208-31.compute-1.amazonaws.com:5432/dam2m47vr1cbj6"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

heroku = Heroku(app)
CORS(app) 

class Save(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    imgsrc = db.Column(db.String(), unique=False)
    text_content = db.Column(db.String(100), unique=False)
    text_align = db.Column(db.String(100), unique=False)
    clipart = db.Column(db.String(100), unique=False)

    def __init__(self, name, imgsrc, text_content, text_align, clipart):
        self.name = name
        self.imgsrc = imgsrc
        self.text_content = text_content
        self.text_align = text_align
        self.clipart = clipart

class SaveSchema(ma.Schema):
    class Meta:
        fields = ('name', 'imgsrc', 'text_content', 'text_align', 'clipart')

save_schema = SaveSchema()
saves_schema = SaveSchema(many=True)