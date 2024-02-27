from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from .utils.jwt import sendToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):
    def post(self, req):
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, req):
        email = req.data["email"]
        password = req.data["password"]
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("Invalid Credentials(Email)..!")
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid Credentials(Password)..!")

        return sendToken(user)


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, req):
        user = req.user
        serializer = UserSerializer(instance=user)
        return Response({"user": serializer.data})
        


class LogoutView(APIView):
    def post(self, req):
        response = Response({
            "success": True,
            "message": "User Logged Out Successfully...!",
        })
        response.delete_cookie(key="token")
        return response
