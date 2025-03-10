from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from challenges.views import BookViewSet, ChallengeViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('challenges', ChallengeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),  # Djoser Endpoints
    path('api/auth/', include('djoser.urls.jwt')),  # JWT Authentication
    path('api/', include(router.urls)),  # Books Endpoints
]