from api.views import EmployeeViewSet, OfficeViewSet, RoomViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()

router.register(r"offices", OfficeViewSet)
router.register(r"rooms", RoomViewSet)
router.register(r"reservations", EmployeeViewSet)

urlpatterns = [
    path("offices/", OfficeViewSet.as_view({"get": "list"})),
    path("rooms/", RoomViewSet.as_view({"get": "list"})),
]

urlpatterns += router.urls
