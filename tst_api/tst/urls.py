from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TstViewSet

router = DefaultRouter()
router.register(r'tst', TstViewSet)

urlpatterns = [
    path('', include(router.urls)),
]