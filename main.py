#
#
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api import test
from api import job


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(
    test.router,
    prefix="/api/test",
    tags=["test"]
)


app.include_router(
    job.router,
    prefix="/api/job",
    tags=["job"]
)

app.mount("/", StaticFiles(directory="./client_react/build", html=True), name="ui")
