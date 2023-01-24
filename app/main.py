from fastapi import FastAPI
#posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware
from .routers import users

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

@app.get("/")
def root():
    return {"message": "Hello Bigger Applications!!!!!!"} 