from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm 
import pdb


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
def add_pet():  # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    """Add pet; handle form"""
   
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
       

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        # pdb.set_trace()
   
        flash(f" {new_pet.name} added")
        return redirect("/add")
    else:
        return render_template("pet_add_form.html", form=form)


@app.route("/pets/<int:pet_id>/edit", methods=["GET, POST"])
def edit_pet(pet_id):
    """Edit pet form and handle edit"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data 
        pet.species = form.species.data 
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data 
        pet.notes = form.notes.data 
        pet.available = form.available.data
        
        # pdb.set_trace()
        
        db.session.commit()
        # flash(f"{pet_id} successfully updated")
        return redirect("/")
    
    else:
        return render_template("edit_pet.html", pet=pet, form=form)
        
        


# if __name__ == "__main__":
#     app.run(debug=True)
