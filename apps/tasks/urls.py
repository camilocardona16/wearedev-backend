from django.db import models

from django.urls import include, path
from rest_framework import routers

from apps.tasks.login import LoginView
from apps.tasks.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path('', include(router.urls), ),
]
