from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'realisateur', views.RealisateurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]