from dataclasses import dataclass
from django.contrib.auth.models import User

@dataclass
class SignupDto :
    userid : str
    password : str
    password_check : str
    name : str
    introduce : str
    address : str

@dataclass
class LoginDto :
    userid : str
    password : str

@dataclass
class ArticleDto :
    title : str
    article : str
    user : User

@dataclass
class EditDto :
    name : str
    introduce : str
    address : str
    pk:str


@dataclass
class RelateDto :
    user_pk : str
    requester : User