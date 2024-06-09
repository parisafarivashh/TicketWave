from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.hall import HallViewSet

router = DefaultRouter()
router.register('halls', HallViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
