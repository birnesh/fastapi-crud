from fastapi import FastAPI
from app.api import root, notes
app = FastAPI()

app.include_router(root.router,tags=["root"])
app.include_router(notes.router, prefix="/notes",tags=["Notes"])