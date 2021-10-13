from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        print("User is not logged in :(")
    return render(request, 'catalog/index.html', {"logged":request.user.is_authenticated})

