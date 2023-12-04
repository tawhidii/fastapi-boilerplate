
import logging
from fastapi import FastAPI
from app.api import ping
from app.db import init_db
from app.api.users import users
from app.api.auth import authenticate


log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    _app = FastAPI(title="AI Delighter",version="1.0.0")
    _app.include_router(users.router,prefix="/users",tags=["Users"])
    _app.include_router(authenticate.router,prefix="/users",tags=["Users"])
    _app.include_router(ping.router)


    return _app

app = create_application()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up....")
    init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")