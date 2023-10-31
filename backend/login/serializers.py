from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')




class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 255)
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

    # Validate the user registration data
    def validate(self, data):
        # Check if the username already exists
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'username': 'Username already exists.'})

        # Check if the email already exists
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'})

        return data

# Define a serializer class for user login
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    # Validate the user login data
    def validate(self, data):
        # Check if the user exists
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError({'non_field_errors': 'Invalid username or password.'})

        return data