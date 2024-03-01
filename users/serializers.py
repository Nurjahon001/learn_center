from rest_framework import serializers
from .models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate_username(self,username):
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists")
        return username

    def validate_email(self,email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email