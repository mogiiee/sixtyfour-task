from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta


class UserSchema(BaseModel):
    _id : 0
    name: str
    email: EmailStr 
    password: str 
    registeration_date = datetime.now()
    expiry_date = registeration_date + timedelta(days=365)
