from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer, InventorySerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class RegisterView(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = Response()
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # request.session['user'] = user

        response.set_cookie(key='token', value=token.key)
        response.set_cookie(key='user', value=user.pk)
        response.set_cookie(key='is_superuser', value=user.is_superuser)
        response.set_cookie(key='username', value=serializer.validated_data['username'])
        response.status_code = status.HTTP_200_OK
        data = {
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_superuser': user.is_superuser,
            'username': serializer.validated_data['username']
        }
        response.data = {"Success": "Login successfully", "data": data}
        return response


class InventoryView(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()



