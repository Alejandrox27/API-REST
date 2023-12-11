#API REST WITH FLASK

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost:3306/bdpythonapi'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# creation Table
class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))
    
    def __init__(self, cat_name, cat_desp):
        self.cat_name = cat_name
        self.cat_desp = cat_desp
        
with app.app_context():
    db.create_all()
    
#schema
class CategorySchema(ma.Schema):
    class Meta:
        fields = ("cat_id", "cat_name", "cat_desp")
# one response
category_schema = CategorySchema()
# multiple responses
categories_schema = CategorySchema(many=True)

# Get #####################################
@app.route("/category", methods=["GET"])
def get_categories():
    all_categories = Category.query.all()
    print(all_categories)
    result = categories_schema.dump(all_categories)
    return jsonify(result)

# Get X Id ################################
@app.route("/category/<id>", methods=["GET"])
def get_category_by_id(id):
    category_one = Category.query.get(id)
    return category_schema.jsonify(category_one)

# POST ###################################
@app.route("/category", methods=["POST"])
def insert_category():
    data = request.get_json(force=True)
    cat_name = request.json["cat_name"]
    cat_desp = request.json["cat_desp"]
    
    new_register = Category(cat_name, cat_desp)
    
    db.session.add(new_register)
    db.session.commit()
    return category_schema.jsonify(new_register)

# PUT ####################################
@app.route("/category/<id>", methods=["PUT"])
def update_category(id):
    updatecategory = Category.query.get(id)
    
    data = request.get_json(force=True)
    cat_name = data["cat_name"]
    cat_desp = data["cat_desp"]
    
    updatecategory.cat_name = cat_name
    updatecategory.cat_desp = cat_desp
    
    db.session.commit()
    
    return category_schema.jsonify(updatecategory)

#welcome message
@app.route("/", methods=["GET"])
def index():
    return jsonify({"Message": "Welcome"})

if __name__ == "__main__":
    app.run(debug=True)