from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerialiser(TokenObtainPairSerializer):


    def get_token(cls, user):
        token =super(MyTokenObtainPairSerialiser, cls).get_token(user)

        token['username'] = user.username
        return token