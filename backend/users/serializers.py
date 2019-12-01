from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'password', 'code', 'address']
        extra_kwargs = {"password": {"write_only": True}, "address": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user


class UserCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=1000)
