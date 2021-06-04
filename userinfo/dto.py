from dataclasses import dataclass


@dataclass
class SignupDto :
    userid : str
    password : str
    password_check : str
    name : str
    introduce : str
    address : str