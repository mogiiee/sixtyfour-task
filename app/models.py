from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserSchema(BaseModel):
    _id : 0
    name: str
    email: EmailStr 
    password: str 
    registeration_date = datetime.now()
    
