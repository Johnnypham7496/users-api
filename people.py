# people.py

from flask import abort, make_response




def create(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
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
    person = Person.query.filter(Person.lname == lname).one_or_none()

    if person is not None::
        return person_schema.dump(person)
    else: 
        abort(
            404, f"Person with last name {lname} not found"
        )


def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]['fname'] = person.get("fname", PEOPLE[lname]['fname'])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404, f'Person with last name {lname} not found'
        )


def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f'{lname} successfully deleted', 200
        )
    else:
        abort(
            404, f'Person with name {lname} not found'
        )