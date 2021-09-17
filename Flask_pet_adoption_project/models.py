from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)
    

class Pet(db.Model):
    """Pet Model"""
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(
        db.Text, default="https://t4.ftcdn.net/jpg/02/26/53/33/360_F_226533348_TiIz0m2dU4dBXC6yFJrNOfXfh5YcEecY.jpg")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
    # def __repr__(self):
    #     return f"<Pet{self.name} {self.species} {self.photo_url} {self.age} {self.notes} {self.available}>"
