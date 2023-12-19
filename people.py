# people.py

from flask import abort, make_response
from config import db
from models.models import Person, people_schema, person_schema



def create(person):
    lname = person.get("lname")

    if (existing_person := Person.query.filter(Person.lname == lname).one_or_none()) is None:
        new_person = person_schema.load(person, session = db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists"
        )

        
def read_all():
    people = Person.query.all()
    return people_schema.dump(people)


def read_one(lname):

    if (person := Person.query.filter(Person.lname == lname).one_or_none()) is not None:
        return person_schema.dump(person)
    else: 
        abort(
            404, f"Person with last name {lname} not found"
        )


def update(lname, person):

    if existing_person := Person.query.filter(Person.lname == lname).one_or_none():
        update_person = person_schema.load(person, session = db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    
    else:
        abort(
            404, f'Person with last name {lname} not found'
        )


def delete(lname):

    if existing_person := Person.query.filter(Person.lname == lname).one_or_none():
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f'{lname} successfully deleted', 200)
    
    else:
        abort(
            404, f'Person with name {lname} not found'
        )


