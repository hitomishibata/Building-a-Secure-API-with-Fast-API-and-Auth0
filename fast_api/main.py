from fastapi import Depends, FastAPI

app = FastAPI(openapi_url=None)

@app.get("/api/public")
def public_data():
    return {"data": "public data"}

@app.get("/api/private", dependencies=[Depends(validate_token)])
def private_data():
    return {"data": "private data"}

@app.get("/api/admin", dependencies=[Depends(validate_role)])
def admin_data():
    return {"data": "admin data"}

