from . import database
from . import database, responses
import bcrypt


async def email_finder(email):
    existing_user = database.user_collection.find_one({"email": email})
    if existing_user is not None:
        return False
    else:
        return True


# hashes passwords using utf8
def hash_password(password: str) -> str:
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Return the hashed password as a string
    return hashed_password.decode("utf-8")



# verifies the credentials from mongodb
async def verify_credentials(username: str, password: str) -> bool:
    user = await full_user_data(username)
    if user is None:
        return False
    hashed_password = user["password"].encode("utf-8")
    is_valid_password = bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    return is_valid_password


# gets full user data
async def full_user_data(email):
    user = database.user_collection.find_one({"email": email})
    if not user:
        return responses.response(False, "does not exist", email)
    return user


def get_all_data():
    response = database.user_collection.find({})
    return list(response)


async def inserter(metadata: dict):
    database.user_collection.insert_one(metadata)
    return responses.response(True, "inserted successfully", metadata)