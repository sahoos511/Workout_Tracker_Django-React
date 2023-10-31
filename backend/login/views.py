from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import serializers, views
from rest_framework.response import Response
import requests
from rest_framework.authentication import SessionAuthentication
from .serializers import *




# Define a view class for user registration
class UserRegistrationView(views.APIView):
    def post(self, request):
        # Serialize the user registration data
        serializer = UserRegistrationSerializer(data=request.data)

        # Validate the user registration data
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        # Create a new user object
        user = User.objects.create_user(serializer.validated_data['username'], serializer.validated_data['email'], serializer.validated_data['password'])

        # Login the user
        login(request, user)

        # Return a response with the user's information
        return Response({'user': user.get_username()})

# Define a view class for user login
class UserLoginView(views.APIView):
    def post(self, request):
        # Serialize the user login data
        serializer = UserLoginSerializer(data=request.data)

        # Validate the user login data
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        # Authenticate the user
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        # If the user is authenticated, log them in
        if user is not None:
            login(request, user)
            return Response({'user': user.get_username()})

        # Otherwise, return an error response
        else:
            return Response({'non_field_errors': 'Invalid username or password.'}, status=401)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


# Define a view class for user dashboard
class UserDashboardView(views.APIView):
    # Authentication is required for this view class
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        # Get the current user
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    


