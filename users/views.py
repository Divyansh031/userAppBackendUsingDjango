from django.http import JsonResponse
from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser   
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from .permissions import IsOwnerOrReadOnly  # Import the custom permission
from django.db import IntegrityError


# Welcome API View
class WelcomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return JsonResponse({"message": "Welcome to the API!"})

# User Registration API View
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

# User Detail API View (Retrieve, Update, Delete User by ID)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)  

# Custom Token View with Username & Email Support
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["email"] = self.user.email  # Add email in response    
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ObtainTokenPairView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = get_user_model().objects.filter(username=username).first()
        if not user:
            raise AuthenticationFailed("User not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid credentials")

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })
