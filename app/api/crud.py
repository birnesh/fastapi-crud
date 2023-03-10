from app.api.models import NoteSchema
# from app.db import notes_list # temp db
from app.db import notes, database

async def post(payload: NoteSchema):
    query = notes.insert().values(
        title=payload.title,
        description=payload.description,
        is_completed=payload.is_completed,
        created_at=payload.created_at
    )
    return await database.execute(query=query)

async def get(id:int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)

async def get_all():
    query = notes.select()
    return await database.fetch_all(query=query)

async def put(id:int, payload:NoteSchema):
    query = notes.update().where(id == notes.c.id).values(
        title = payload.title,
        description = payload.description,
        is_completed = payload.is_completed,
        created_at = payload.created_at
    ).returning(notes.c.id)
    return await database.execute(query=query)

async def delete(id:int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)
