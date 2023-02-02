from fastapi import FastAPI
#posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware
from .routers import prompts, exercises, login, resources, users, journalEntries, completed_exercises, loadAll


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#adds routes to app
app.include_router(users.router)
app.include_router(resources.router)
app.include_router(exercises.router)
app.include_router(login.router)
app.include_router(prompts.router)
app.include_router(journalEntries.router)
app.include_router(completed_exercises.router)
app.include_router(loadAll.router)

@app.get("/")
def root():
    return {"message": "Hello Bigger Applications!!!!!!"} 