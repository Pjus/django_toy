from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'accounts/sign_up.html')
    return render(request, 'accounts/sign_up.html')

def login():
    return render(request, 'accounts/login.html')

def logout():
    return render(request, 'accounts/logout.html')