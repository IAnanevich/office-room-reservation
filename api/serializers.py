from reservation.models import Employee, Office, Room
from rest_framework import serializers


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ("office_name", "address", "number_of_rooms", "photo_of_office", "url")


class RoomSerializer(serializers.ModelSerializer):
    name_office = serializers.CharField(source="name_office.office_name")

    class Meta:
        model = Room
        fields = ("room_number", "number_seats", "name_office", "url")


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "first_name",
            "last_name",
            "email",
            "room_number",
            "date_from",
            "date_to",
            "url",
        )
