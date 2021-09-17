from flask_wtf import FlaskForm
from wtforms import (BooleanField, FloatField, IntegerField, RadioField,
                     SelectField, StringField)
from wtforms.validators import (URL, InputRequired, Length, NumberRange,
                                Optional)


class AddPetForm(FlaskForm):
    # name = StringField("Pet Name", validators=[InputRequired(message="Pet Name cannot be left blank")]),
    # species = StringField("Species", validators=[InputRequired(message="Species field cannot be left blank")]),
    # photo_url = StringField("Pet's Photo", validators=[Optional(), URL()]),
    # age = IntegerField("Enter Pet's age", validoators=[Optional()]),
    # notes = StringField("Notes", validators=[Optional()]),
    # available = BooleanField("Pet is available", validators=[InputRequired(message="Pet is")])
    
    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )

    notes = StringField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = StringField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")


