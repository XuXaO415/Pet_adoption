"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, session, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
import pdb


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ThIsIsToTaLSeCrEt92761#"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


def serialize_cupcake(cupcake):
    """Serialize a cupcake SQLAlchemy obj to dict"""
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image,
    }
    
@app.route("/")
def cupcake_home():
    """Cupcake homepage"""
    return render_template("base.html")
    
@app.route("/api/cupcakes")
def list_cupcakes():
    """Gather data and list all cupcakes"""
    
    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]
    
    return (jsonify(cupcakes=serialized))
    

#  GET /cupcakes/[id] --> Get snack
@app.route("/api/cupcakes/<int:cupcake_id>")
def single_cupcake(cupcake_id):
    """Gather data on single cupcake"""
    
    # cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)
    
    #Removed 404 because it caused tests to fail
    # return (jsonify(cupcake=serialized), 404)
    return (jsonify(cupcake=serialized))

    
@app.route("/api/cupcakes", methods=["POST"])
def custom_cupcake():
    """Customize cupcake. 
    Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    """


    # pdb.set_trace()
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]
    # pdb.set_trace()
    
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    
    serialized = serialize_cupcake(new_cupcake)
    # Return w/status code 201 -- return tuple (json, status)
    return (jsonify(cupcake=serialized), 201)
    
    # data = request.json
    # cupcake = Cupcake(
    #     flavor=data["flavor"],
    #     size=data["size"],
    #     rating=data["rating"],
    #     image=data["image"] or None
    # )
    # serialized = serialize_cupcake(cupcake)
    # db.session.add(cupcake)
    # db.session.commit()
    
    # return (jsonify(cupcake=serialized), 201)

    
#############################################################
#Part three: Update a& Delete Cupcakes

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake
    Returns JSON like this: {cupcake: {id, flavor, size, rating, image}}
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)
    
    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]
    cupcake.image = request["image"]
    
    # pdb.set_trace()
    
    new_cupcake = Cupcake(flavor=cupcake.flavor, size=cupcake.size, rating=cupcake.rating, image=cupcake.image)
    db.session.add(new_cupcake)
    db.session.commit()
    
    return jsonify(cupcake=serialized)
    

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """"Delete cupcake or raise 404 if cupcake is not found
 Returns JSON like this: {"message": "Deleted"}"""
 
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()
    
    return jsonify(message="deleted")
    
