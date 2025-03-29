from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone", "address", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "error_messages": {"required": "Password is required"}}  # Hide password in responses
        }
    def validate(self, data):
        # Ensure email is unique
        if User.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})

        # Ensure phone number is unique
        if User.objects.filter(phone=data.get('phone')).exists():
            raise serializers.ValidationError({"phone": "This phone number is already registered."})

        return data
    

    def create(self, validated_data):
        """Ensure password is hashed before saving"""
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Ensure password is hashed when updating"""
        password = validated_data.get("password", None)
        if password:
            instance.password = make_password(password)
        return super().update(instance, validated_data)
