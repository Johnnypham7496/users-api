# User models are used to generate or adapt user interfaces at runtime, to address particular user needs and preferences. 
# User models are also known as user profiles, personas or archetypes
from datetime import datetime
from config import db, ma


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(100), unique=True)
    fname = db.Column(db.String(100), unique=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class PersonSchema(ma.SQLAlchemySchema):
    class Meta:
        model= Person
        load_instance = True
        sqla_session = db.session

person_schema = PersonSchema()
person_schema = PersonSchema(many=True)