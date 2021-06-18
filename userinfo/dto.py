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
    image : str

@dataclass
class EditDto :
    name : str
    introduce : str
    address : str
    pk:str

@dataclass
class CommentDto :
    article_pk : str
    owner : str
    writer : User
    content : str

@dataclass
class LikeDto :
    comment_pk : str
    users : User


@dataclass
class RelateDto :
    user_pk : str
    requester : User