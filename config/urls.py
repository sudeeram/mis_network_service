from django.urls import include, path

urlpatterns = [path("api/network/", include("network.urls"))]

