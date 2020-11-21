from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet


router = DefaultRouter()
router.register('api/v1/users', UserViewSet)


urlpatterns = [
    path('api-token-auth/', TokenObtainPairView.as_view()),
    path('api-token-auth/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]
