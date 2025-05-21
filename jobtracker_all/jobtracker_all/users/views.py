from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model() #get_user_model is a function that returns the user model that is currently active in the project. This is useful for projects that use a custom user model, as it allows you to avoid hardcoding the user model name.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data) #serializer takes the data from the request and passes it to the LoginSerializer
        if serializer.is_valid(): #checks if the data is valid according to the rules of loginserializer
            user = serializer.validated_data # after is_valid, confirm the user, put their information into serializer.validated_data
            token, created = Token.objects.get_or_create(user=user) #looks for a token for this user, if it doesn't exist, creates a new one (getorcreate)
            print('token:', token)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)