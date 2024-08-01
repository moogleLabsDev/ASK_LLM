from typing import List
from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from enum import Enum
from typing import Literal


class MobileType(str, Enum):
    ios = "ios"
    android = "android"

    



# Base schema for user information
class UserBase(BaseModel):
    email: EmailStr
    name: str
    phone_number:str



# Schema for creating a user
class UserCreate(UserBase):
    password: str
    device_type: MobileType

# Schema for representing a user
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Schema for OTP verification
class OTPVerification(BaseModel):
    id: int
    otp: str

# Schema for response after OTP verification
class OTPVerificationResponse(BaseModel):
    message: str


class LoginCredential(BaseModel):
    email: EmailStr
    password:str

class Forgetchangepassword(BaseModel):
    id:int
    password:str
    confirm_password:str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    Id: int | None = None

class PasswordChange(BaseModel):
    current_password: str
    new_password: str
    confirm_password:str


class Userprofile(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None

class Resendotp(BaseModel):
    id:int


class Gpt_query(BaseModel):
    llm_type: List[int] = Field(default_factory=lambda: [0])
    query: str
    user_id: str
    
    

class model_selection(BaseModel):
    user_id : int
    selected: List[str]

class Llm_query(BaseModel):
    llm_type: List[str]
    query: str
    user_id: str
    regenerate: bool = False
    
class model_selected(BaseModel):
    user_id : str
    selected: List[str]
    unselected:List[str]
    
class Llm_chat(BaseModel):
    user_id : str
    llm_id: str







