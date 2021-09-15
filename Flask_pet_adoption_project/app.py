from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SuPpOrT_yOuR_lOcAl_ShElTeR"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# @app.route('/')
# def homepage():
#     pet = Pet.query.all()
