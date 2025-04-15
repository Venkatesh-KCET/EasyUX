from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

UserModel = get_user_model()

class MyCustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        print('Running')
        try:
            # Treat username as email for login
            print(username, password)
            user = UserModel.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except UserModel.DoesNotExist:
            print('User does not exist')
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None