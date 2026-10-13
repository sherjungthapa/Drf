from rest_framework import viewsets
from .serializer import ResgisterSerialer
from django.contrib.auth.models import User
from rest_framework import authentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class RegisterView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=ResgisterSerialer

class LoginView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    def create(self, request, *args, **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            token,created =Token.objects.get_or_create(user=user)
            return Response({
                'token':token.key
            })
        return Response({'message':"invalid credentials"})