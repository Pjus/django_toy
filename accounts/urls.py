from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_try, name='login'),
    path('logout/', views.logout, name='logout'),
]