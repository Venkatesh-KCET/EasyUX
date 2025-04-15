from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

class CustomAdminLoginView(LoginView):
    template_name = 'admin/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/dashboard/'  # force it, ignoring ?next
