from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import Inventory
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                message = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Must include "username" and "password".'
            raise serializers.ValidationError(message, code='authorization')
        data['user'] = user
        return data


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'





