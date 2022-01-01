from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.controllers import mailer_controller
import os
from os.path import join, dirname
from dotenv import load_dotenv



dotenv_path = join(dirname(__file__), 'env/.env')
load_dotenv(dotenv_path)
PORT = os.environ.get("PORT")

app = FastAPI()

#Root
@app.get("/")
async def root():
    return {"message": f"Listen in {PORT}..."}


app.include_router(mailer_controller.router)

#OpenAPI Config
def my_schema():
    openapi_schema = get_openapi(
       title="Mailer with FastAPI",
       version="1.0",
       description="An API Mailer demo make with FastAPI",
       routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = my_schema
