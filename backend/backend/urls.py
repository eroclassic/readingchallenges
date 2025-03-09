from django.contrib import admin
from django.urls import path, include
from challenges.views import get_challenges

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),  # Djoser Endpoints
    path('api/auth/', include('djoser.urls.jwt')),  # JWT Authentication
    path('api/challenges/', get_challenges),  # Challenges Endpoints
]