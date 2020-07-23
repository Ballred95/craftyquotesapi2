from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
import io
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ""
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