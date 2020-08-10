from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    flat = db.Column(db.String(5), unique=False, nullable=False)
    in_time = db.Column(db.DateTime, nullable=False)
    out_time = db.Column(db.DateTime, nullable=True)
    facility_id = db.Column(
        db.Integer, db.ForeignKey('facility.id'))
    users = db.relationship('facility', back_populates="member")

    def __init__(**kwargs):
        super(Member, self).__init__(**kwargs)

    def serialize(self):
        """
        JSON of Member object
        """
        return {
            'id': self.id,
            'name': self.name,
            'flat': self.flat,
            'in_time': self.in_time,
            'out_time': self.out_time,
            'facility_id': self.facility_id,
        }


class Facility(db.Model):
    __tablename__ = 'facility'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    occupied = db.Column(db.Boolean, unique=False, default=False)
    users = db.relationship('member', back_populates="facility")

    def __init__(**kwargs):
        super(Facility, self).__init__(**kwargs)

    def serialize(self):
        """
        JSON of Facility object
        """
        return {
            'id': self.id,
            'name': self.name,
            'occupied': self.occupied
        }
