from fastapi import FastAPI
from . import responses, models, database, ops
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder




app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["greetings"])
async def greet():
    return {"hello ": "people from SixtyFour Data Intelligence LLP"}

@app.post("/signup", tags=["auth"])
async def signup(signup_details: models.User):
    infoDict = jsonable_encoder(signup_details)
    # print(infoDict)
    infoDict = dict(infoDict)
    # Checking if email already exists
    email_count = database.user_collection.count_documents({"email": infoDict["email"]})
    if email_count > 0:
        return responses.response(False, "duplicated user, email already in use", None)
    # Insert new user

    encoded_password = ops.hash_password(str(infoDict["password"]))
    infoDict["password"] = encoded_password
    # print(infoDict)
    json_signup_details = jsonable_encoder(infoDict)
    await ops.inserter(json_signup_details)
    return responses.response(True, "inserted", signJWT(infoDict))