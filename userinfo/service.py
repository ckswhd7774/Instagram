from django.contrib.auth.models import User
from userinfo.models import Profile
from userinfo.dto import SignupDto


class UserService():

    @staticmethod
    def signup(dto:SignupDto) :
        user = User.objects.create_user(username=dto.userid, password=dto.password)
        Profile.objects.create(user=user, name=dto.name, introduce=dto.introduce, address=dto.address)
        
        return {'user':user}
