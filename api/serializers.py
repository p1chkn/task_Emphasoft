from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=True)

    class Meta:
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "last_login",
            "is_superuser",
            "password",
        ]
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
