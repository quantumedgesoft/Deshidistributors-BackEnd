from django.contrib import admin
from django.urls import path, include

admin.site.site_title = "Deshi Distributors"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
]
