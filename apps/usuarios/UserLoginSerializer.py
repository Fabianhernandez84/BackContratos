from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        
        if user and user.is_active:           
            refresh = RefreshToken.for_user(user)                 
            return {'token': str(refresh.access_token)}
        
        raise serializers.ValidationError('Credenciales inválidas')