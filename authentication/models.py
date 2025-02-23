from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Super Admin', 'Super Admin'),
        ('Customer', 'Customer'),
        ('Staff', 'Staff'),
    )
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.user_type == 'Admin' or self.user_type == 'Super Admin':
            self.is_superuser = True
            self.is_staff = True
        if self.user_type == 'Staff':
            self.is_staff = True
        if self.user_type == 'Customer':
            self.is_superuser = False
            self.is_staff = False
        super().save(*args, **kwargs)


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='customer_authentication')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    can_read = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)