from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template
from db import Member, Facility, db
import json
import psycopg2

app = Flask(__name__)
app.config["DEBUG"] = False

# app config
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rnjchqtvccnzma:50f02f117dc856205960e1a4ae949c032752d428d802d26615938c3976cd8497@ec2-52-204-20-42.compute-1.amazonaws.com: 5432/dcsbpv4h35ss8v"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def hello():
    return "Welcome to the Kalpataru Residency's ClubHouse Manager!"


if __name__ == '__main__':
    app.run()
