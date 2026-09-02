from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DashboardView, DeviceViewSet, HealthLiveView, HealthReadyView

router = DefaultRouter(trailing_slash=False)
router.register("devices", DeviceViewSet)
urlpatterns = [
    path("dashboard", DashboardView.as_view()),
    path("health/live", HealthLiveView.as_view()),
    path("health/ready", HealthReadyView.as_view()),
    path("", include(router.urls)),
]

