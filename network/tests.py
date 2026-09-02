from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .models import Device
from .permissions import HasFeaturePermission
from .views import DashboardView


class PermissionTests(TestCase):
    def test_feature_permission_is_required(self):
        request = APIRequestFactory().get("/api/network/dashboard")
        request.auth = {"permissions": []}
        self.assertFalse(HasFeaturePermission().has_permission(request, DashboardView()))
        request.auth = {"permissions": ["network:dashboard:view"]}
        self.assertTrue(HasFeaturePermission().has_permission(request, DashboardView()))

    def test_device_uses_external_user_uuid(self):
        field = Device._meta.get_field("created_by_user_id")
        self.assertEqual(field.get_internal_type(), "UUIDField")

