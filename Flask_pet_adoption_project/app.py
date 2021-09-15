from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
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

@app.route("/")
def list_pets():
    """List pets"""
    pets = Pet.query.all()
    return render_template("list_pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add pet; handle form"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.phot_url.data
        age = form.age.data
        notes = form.notes.data
        
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session(new_pet)
        db.session.commit()
        flash(f"{new_pet} added")
        return render_template("pet_add_form.html", form=form)
    
    # else:
    #     return render_template("pet_add_form.html", form=form )

    
