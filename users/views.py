
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    UserDetailSerializer,
    UserUpdateSerializer
)

# Create your views here.

class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetailAPIView(APIView):
    
    def get_object(self, username):
        return get_object_or_404(get_user_model(), username=username)
        
    
    def get(self, request, username):
        user=self.get_object(username)
        serializer=UserDetailSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username):
        password=request.data.get('password')
        password2=request.data.get('password2')
        if (password or password2) and (password!=password2):
            return Response({'error':"password or password2 not exist or password is not equal"}, status=status.HTTP_400_BAD_REQUEST)
        
        user=self.get_object(username)
        serializer=UserDetailSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            user=serializer.save()
            if password:
                user.set_password(password)
                user.save()
            serializer=UserUpdateSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)