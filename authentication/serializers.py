from rest_framework import serializers
from .models import CustomUser, Customer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed

#=========================Admin User Creation & Login Serializers Start========================
class AdminUserCreationSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    user_type = serializers.ChoiceField(choices=CustomUser.USER_TYPE, required=True)
    
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'username', 'email', 'user_type', 'password']

class AdminTokenObtainPairSerializers(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.user_type == 'Customer':
            raise AuthenticationFailed("Only Admin, Super Admin or Staff can login!", code="authorization")
        return data
#=========================Admin User Creation & Login Serializers End========================



#=========================Customer Registration & Login Serializers Start========================
class CustomerTokenObtainPairSerializers(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.user_type != 'Customer':
            raise AuthenticationFailed("Only Customer can login!", code="authorization")
        return data

class CustomerRegistrationSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'phone', 'email', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        name = validated_data.pop('name')
        phone = validated_data.pop('phone')
        
        validated_data['password'] = make_password(password)
        validated_data['username'] = name.lower()
        validated_data['first_name'] = name
        validated_data['user_type'] = 'Customer'
        
        user = CustomUser.objects.create(**validated_data)
        Customer.objects.create(
            user=user, name=name, phone=phone, email=user.email
        ).save()
        return user
#=========================Customer Registration & Login Serializers End========================


