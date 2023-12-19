from flask import abort, make_response
from config import db
from models.models import Note, note_schema, Person


def create_note(note):
    person_id = note.get("person_id")

    if person := Person.query.get(person_id):
        new_note = note_schema.load(note, session= db.session)
        person.notes.append(new_note)
        db.session.commit()
        return note_schema.dump(new_note), 201

    else:
        abort(
            406,
            f"Person not found for ID: {person_id}"
        )


def read_one(note_id):

    if (note := Note.query.get(note_id)) is not None:
        return note_schema.dump(note)

    else:
        abort(
            404, f'Note with ID {note_id} not found'
        )


def update_note(note_id, note):

    if existing_note := Note.query.get(note_id):
        update_note = note_schema.load(note, session= db.session)
        existing_note.content = update_note.content
        db.session.merge(existing_note)
        db.session.commit()
        return note_schema.dump(existing_note), 201


def delete_note(note_id):

    if existing_note := Note.query.get(note_id):
        db.session.delete(existing_note)
        db.session.commit()
        return make_response(f'{note_id} successfully deleted', 204)
    
    else:
        abort(
            404, f'Note with ID {note_id} not found'
        )
