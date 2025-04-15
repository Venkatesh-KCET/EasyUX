from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

class MyCustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Treat username as email for login
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            else:
                return None
        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None