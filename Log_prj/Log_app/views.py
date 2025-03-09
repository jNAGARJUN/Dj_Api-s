from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmpDetails
from .serializers import EmpDetailsSerializer
from django.contrib.auth.hashers import check_password



class RegisterView(APIView):
    def post(self, request):
        serializer = EmpDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = EmpDetails.objects.get(username=username)
            if password==user.password:
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
        except EmpDetails.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
