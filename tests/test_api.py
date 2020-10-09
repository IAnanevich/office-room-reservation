from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from reservation.models import Employee, Room, Office


class ApiTest(APITestCase):
    def setUp(self) -> None:
        office = Office.objects.create(
            office_name="office",
            street="street",
            house_number=1,
            number_of_rooms=1,
            photo_of_office=SimpleUploadedFile(name='innowise.jpeg', content=open('media/innowise.jpeg', 'rb').read()),
        )

        room1 = Room.objects.create(
            room_number=1,
            number_seats=1,
            name_office=office
        )

        room2 = Room.objects.create(
            room_number=2,
            number_seats=1,
            name_office=office
        )

        Employee.objects.create(
            first_name="First name 1",
            last_name="Last name 1",
            email="email1@gmail.com",
            room_number=room1,
            date_from="2020-10-10",
            date_to="2020-10-30",
        )

        Employee.objects.create(
            first_name="First name 2",
            last_name="Last name 2",
            email="email2@gmail.com",
            room_number=room2,
            date_from="2020-10-10",
            date_to="2020-10-30",
        )

        self.client = APIClient()
        self.client.login()

    def test_get_all_articles(self):
        response = self.client.get("/reservations/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
