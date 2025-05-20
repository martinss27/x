from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), #register new users
    path('login/', LoginView.as_view(), name='login'), #check if user exist and return token
]