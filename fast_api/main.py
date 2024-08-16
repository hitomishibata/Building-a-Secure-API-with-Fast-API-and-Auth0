from os import environ as env
from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, FastAPI
from validate_permissions import PermissionValidator

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = FastAPI(openapi_url=None)
oauth = Oauth(app)

@app.get("/api/public")
def public_data():
    return {"data": "public data"}

@app.get("/api/private", dependencies=[Depends(validate_token)])
def private_data():
    return {"data": "private data"}

@app.get("/api/admin", dependencies=[Depends(PermissionValidator(["read:admin-messages"]))],)
def admin_data():
    return {"data": "admin data"}

