from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI

from src.api import api_router
from src.clients.dummy_json import DummyJsonClient
from src.core.config import settings
from src.db.mongo import MongoClientManager

mongo_manager = MongoClientManager(settings.mongodb_uri, settings.mongodb_db)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongo_manager.connect()
    app.state.db = mongo_manager.database
    app.state.http_client = httpx.AsyncClient()
    app.state.dummy_client = DummyJsonClient(settings.dummy_user_url, app.state.http_client)
    try:
        yield
    finally:
        await app.state.http_client.aclose()
        await mongo_manager.disconnect()


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.include_router(api_router)


@app.get("/", tags=["health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
