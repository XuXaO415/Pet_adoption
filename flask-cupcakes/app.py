"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, session, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ThIsIsToTaLSeCrEt92761#"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/api/cupcakes")
def list_cupcakes():
    """Gather data and list all cupcakes"""
    

#  GET /cupcakes/[id] --> Get snack
@app.route("/api/cupcakes/<int:cupcake_id>")
def single_cupcake()s:
    """Gather data on single cupcake"""
    
@app.route("/api/cupcakes", methods=["POST"])
def custom_cupcake():
    """Customize cupcake"""
    
    
#############################################################
#Part three: Update a& Delete Cupcakes

# @app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
# def update_cupcake():
#     """Update cupcake"""
    

# @app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
# def delete_cupcake():
#     """"Delete cupcake or raise 404 if cupcake is not found"""
    