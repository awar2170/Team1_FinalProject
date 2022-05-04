# import dependencies
import json
from config import username, db_pass, db_name

# import SQLAlchemy dependency
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import Flask dependency
from flask import Flask, jsonify, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
from ml import runML

# setup database engine
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

# create Base to reflect our DB
Base = automap_base()

# create Flask instance
app = Flask(__name__)
app.template_folder = '.'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://"+username+":"+db_pass+"@localhost:5432/"+db_name
db = SQLAlchemy(app)

# create db instance
class mushroom(db.Model):
    __tablename__ = 'attributes'

    id = db.Column(db.Integer, primary_key=True)
    poisonous_or_edible = db.Column(db.String())
    cap_shape = db.Column(db.String())
    cap_surface = db.Column(db.String())
    cap_color = db.Column(db.String())
    bruises = db.Column(db.String())
    odor = db.Column(db.String())
    gill_attachment = db.Column(db.String())
    gill_spacing = db.Column(db.String())
    gill_size = db.Column(db.String())
    gill_color = db.Column(db.String())
    stalk_shape = db.Column(db.String())
    stalk_root = db.Column(db.String())
    stalk_surface_above_ring = db.Column(db.String())
    stalk_surface_below_ring = db.Column(db.String())
    stalk_color_above_ring = db.Column(db.String())
    stalk_color_below_ring = db.Column(db.String())
    veil_type = db.Column(db.String())
    veil_color = db.Column(db.String())
    ring_number = db.Column(db.String())
    ring_type = db.Column(db.String())
    spore_print_color = db.Column(db.String())
    population = db.Column(db.String())
    habitat = db.Column(db.String())

    def __init__(self, poisonous_or_edible, cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment, gill_spacing, gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat):
        self.poisonous_or_edible = poisonous_or_edible
        self.cap_shape = cap_shape
        self.cap_surface = cap_surface
        self.cap_color = cap_color
        self.bruises = bruises
        self.odor = odor
        self.gill_attachment = gill_attachment
        self.gill_spacing = gill_spacing
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_shape = stalk_shape
        self.stalk_root = stalk_root
        self.stalk_surface_above_ring = stalk_surface_above_ring
        self.stalk_surface_below_ring = stalk_surface_below_ring
        self.stalk_color_above_ring = stalk_color_above_ring
        self.stalk_color_below_ring = stalk_color_below_ring
        self.veil_type = veil_type
        self.veil_color = veil_color
        self.ring_number = ring_number
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        self.population = population
        self.habitat = habitat

    def __repr__(self):
        return f"<attributes {self.name}>"

# define base route
@app.route('/')
def home():
    return render_template("index.html")

# define db entries route
@app.route('/mushrooms', methods=['GET'])
def qmushrooms():
    attributes = mushroom.query.all()
    results = [
        {
            "poisonous_or_edible": attr.poisonous_or_edible,
            "cap_shape": attr.cap_shape,
            "cap_surface": attr.cap_surface,
            "cap_color": attr.cap_color,
            "bruises": attr.bruises,
            "odor": attr.odor,
            "gill_attachment": attr.gill_attachment,
            "gill_spacing": attr.gill_spacing,
            "gill_size": attr.gill_size,
            "gill_color": attr.gill_color,
            "stalk_shape": attr.stalk_shape,
            "stalk_root": attr.stalk_root,
            "stalk_surface_above_ring": attr.stalk_surface_above_ring,
            "stalk_surface_below_ring": attr.stalk_surface_below_ring,
            "stalk_color_above_ring": attr.stalk_color_above_ring,
            "stalk_color_below_ring": attr.stalk_color_below_ring,
            "veil_type": attr.veil_type,
            "veil_color": attr.veil_color,
            "ring_number": attr.ring_number,
            "ring_type": attr.ring_type,
            "spore_print_color": attr.spore_print_color,
            "population": attr.population,
            "habitat": attr.habitat
        } for attr in attributes]

    return json.dumps(results)

# define machine learning route
@app.route('/predict', methods=['POST'])
def prediction():
    #req = request.get_json()
    req = request.json
    return jsonify(runML(req))


if __name__ == "__main__":
    app.run(debug=True)
