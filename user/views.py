import jwt
import json
import bcrypt

from django.views import View
from django.shortcuts import render
from user.models import User, UserOption
from .utils import login_decorator

class UserView(View):

    def post(self, request):
        new_user = json.loads(request.body)

        if User.Objects.filter(user_name=new_user['user_name']).exists():
            return JsonResponse({'status':'false','message':'USERNAME_EXIST'}, status=400)
        else:
            password = bytes(new_user['user_pasword'], 'utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

            new_user = User(
                user_name = new_user['user_name'],
                user_password = hashed_password.decode('utf-8'),
                user_gender = new_user['user_gender']
            )
            new_user.save()

            user_settings = UserOption(
                hate_hot = False,
                hate_cold = False,
                user = new_user
            )
            user_settings.save()

            return JsonResponse({'status': 'true', 'message': 'SIGNUP_SUCCESS'}, status=200)
    
    @login_decorator
    def get(self, request):
        return JsonResponse({
            'user_name' : request.user.user_name    
        })
    

