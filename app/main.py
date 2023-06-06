from fastapi import FastAPI, HTTPException, Depends
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
async def signup(signup_details: models.UserSchema):
    infoDict = jsonable_encoder(signup_details)
    # print(infoDict)
    infoDict = dict(infoDict)
    # Checking if email already exists
    if database.user_collection.find_one({"email": infoDict["email"]}):
        raise HTTPException(status_code=400, detail="User with this email already exists")
    # Insert new user

    encoded_password = ops.hash_password(str(infoDict["password"]))
    infoDict["password"] = encoded_password
    # print(infoDict)
    json_signup_details = jsonable_encoder(infoDict)
    await ops.inserter(json_signup_details)
    return responses.response(True, "inserted", signJWT(infoDict))



# @app.post("/user/authenticate")
# def authenticate_user(user: UserAuthentication):
#     existing_user = database.user_collection.find_one({"api_key": user.api_key})
#     if existing_user:
#         token = generate_token(existing_user["email"])
#         return {"access_token": token}

#     raise HTTPException(status_code=400, detail="Invalid API key")


@app.get("/all-users",dependencies=[Depends(JWTBearer())],tags=["protected"])
async def Get_all_data():
    try:
        
        response = ops.get_all_data()
        for x in response:
            del x["_id"]
        return responses.response(True, None, response)
    except Exception as e:
        return responses.response(
            False, str(e), "something went wrong please try again"
        )

