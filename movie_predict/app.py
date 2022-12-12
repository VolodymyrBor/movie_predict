from fastapi import FastAPI

from . import db, rest_api


def create_app() -> FastAPI:
    app = FastAPI(
        on_startup=[
            db.init_db,
        ],
    )
    app.include_router(rest_api.router)
    return app
