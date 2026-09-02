from django.db import connection
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Device
from .permissions import HasFeaturePermission
from .serializers import DeviceSerializer


class HealthLiveView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def get(self, request): return Response({"status": "ok", "service": "network"})


class HealthReadyView(HealthLiveView):
    def get(self, request):
        with connection.cursor() as cursor: cursor.execute("SELECT 1")
        return Response({"status": "ready", "service": "network"})


class DashboardView(APIView):
    permission_classes = [HasFeaturePermission]
    required_permission = "network:dashboard:view"
    def get(self, request): return Response({"service": "network", "deviceCount": Device.objects.count()})


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [HasFeaturePermission]

    def get_required_permission(self):
        return {
            "list": "network:devices:view", "retrieve": "network:devices:view",
            "create": "network:devices:create", "update": "network:devices:update",
            "partial_update": "network:devices:update", "destroy": "network:devices:delete",
        }.get(self.action)

    @property
    def required_permission(self): return self.get_required_permission()

    def perform_create(self, serializer): serializer.save(created_by_user_id=self.request.user.id)

