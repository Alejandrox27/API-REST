#API REST WITH FLASK

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost:3306/bdpythonapi'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#welcome message
@app.route("/", methods=["GET"])
def index():
    return jsonify({"Message": "Welcome"})

if __name__ == "__main__":
    app.run(debug=True)