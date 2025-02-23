from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import AdminTokenObtainPairSerializers, AdminUserCreationSerializers, CustomerTokenObtainPairSerializers, CustomerRegistrationSerializers
from rest_framework.generics import CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Customer

#=========================Admin User Creation & Login views Start========================
class AdminTokenObtainPairView(TokenObtainPairView):
    serializer_class = AdminTokenObtainPairSerializers

class AdminUserCreationViews(CreateAPIView):
    serializer_class = AdminUserCreationSerializers
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
#=========================Admin User Creation & Login views End========================


#=========================Customer Registration & Login views Start========================
class CustomerTokenObtainPariView(TokenObtainPairView):
    serializer_class = CustomerTokenObtainPairSerializers

class CustomerRegistrationViews(CreateAPIView):
    serializer_class = CustomerRegistrationSerializers
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'message': 'Customer Registration Successfully!',
            }, status=status.HTTP_201_CREATED
        )
        
#=========================Customer Registration & Login views End========================



