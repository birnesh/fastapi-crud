from app.api.models import NoteSchema
from app.db import notes_list # temp db

def post(payload: NoteSchema):
    note = {
        "title": payload.title,
        "description": payload.description,
        "is_completed": payload.is_completed,
        "created_at": payload.created_at
    }
    if len(notes_list) == 0:
        note['id'] = 1
    else:
        note['id'] = notes_list[-1]['id']+1
    notes_list.append(note)
    return note['id']

def get(id:int):
    filtered_list = list(filter(lambda item: item["id"] == id, notes_list))
    if len(filtered_list) > 0:
        return filtered_list[0]
    else:
        return None

def get_all():
    return notes_list

def put(id:int, payload:NoteSchema):
    # iterate through the list to update the note
    for item in notes_list:
        if item["id"] == id:
            item["title"] = payload.title,
            item["description"] = payload.description
            item["is_completed"] = payload.is_completed
            item["created_at"] = payload.created_at
            break
    return id

def delete(id:int):
    # iterate through the list to delete the note by id
    for idx in range(len(notes_list)):
        if notes_list[idx]["id"] == id:
            del notes_list[idx]
    return id