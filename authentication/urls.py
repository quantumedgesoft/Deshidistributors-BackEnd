from django.urls import path
from .views import AdminTokenObtainPairView, CustomerTokenObtainPariView, AdminUserCreationViews, CustomerRegistrationViews

urlpatterns = [
    #Admin
    path('admin-login/', AdminTokenObtainPairView.as_view(), name='admin-login'),
    path('admin-creation/', AdminUserCreationViews.as_view(), name='admin-creation'),
    
    #customer
    path('customer-login/', CustomerTokenObtainPariView.as_view(), name='customer-login'),
    path('customer-registration/', CustomerRegistrationViews.as_view(), name='customer-registration'),
]
