from fastapi import FastAPI
from fastapi.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import os
from {{cookiecutter.app_name}}.app import api as a_app
import inspect
import logging

logger = logging.getLogger(__name__)


API_STR = os.getenv("API_ROOT", "/api")
app = None
develop = bool(os.getenv("DEVELOP", False))
logger.info("App is up and running!")
if develop:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
        )

    ]
    app = FastAPI(middleware=middleware)
else:
    app = FastAPI()

for name, obj in inspect.getmembers(a_app):
    if "_router" in name:
        app.include_router(obj, prefix=API_STR)
