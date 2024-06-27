from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CommandViewSet

router = DefaultRouter()
router.register(r'commands', CommandViewSet)

urlpatterns=[
    path('',views.all_commands),
    path('api/', include(router.urls)),
]