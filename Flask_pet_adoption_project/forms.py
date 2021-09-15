from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL, Optional



class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name cannot be left blank")])
    species = StringField("Species", validators=[InputRequired(message="Species field cannot be left blank")])
    photo_url = StringField("Pet's Photo", validators=[Optional(), URL()])
    age = FloatField("Enter Pet's age", validoators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Pet is available", validators=[InputRequired(message="Pet is")])
    






