from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from userinfo.models import Profile
from userinfo.dto import SignupDto, LoginDto


ERROR_MSG = {
    'EXIST_ID' : '이미 존재하는 아이디 입니다.',
    'NO_EXIST_ID' : '존재하지 않는 아이디 입니다',
    'MISSING_INPUT' : '항목을 모두 채워주세요',
    'PASSWORD_CHECK' : '비밀번호를 확인해주세요',
}

class UserService():

    @staticmethod
    def signup(dto:SignupDto) :
        # 팝업창으로 모든 항목 체크, 아이디 중복 체크, 비밀번호체크 구현
        user = User.objects.create_user(username=dto.userid, password=dto.password)
        Profile.objects.create(user=user, name=dto.name, introduce=dto.introduce, address=dto.address)
        
        return {'user':user}

    @staticmethod
    def login(dto:LoginDto) :
        if not(dto.userid and dto.password) :
            return {'error':{'state':True},'msg': ERROR_MSG['MISIING_INPUT']}
        user = User.objects.filter(username=dto.userid)
        if len(user) == 0 :
            return {'error':{'state':True},'msg': ERROR_MSG['NO_EXIST_ID']}
        if dto.password is None :
            return {'error':{'state':True},'msg': ERROR_MSG['PASSWORD_CHECK']}
        auth_user = authenticate(username=dto.userid, password=dto.password)

        return {'error':{'state':False}, 'user':auth_user}