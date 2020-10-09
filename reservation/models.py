from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Office(models.Model):
    office_name = models.CharField(max_length=70)
    street = models.CharField(max_length=70)
    house_number = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField()
    photo_of_office = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.office_name

    def address(self):
        return f"{self.street}, {self.house_number}"


class Room(models.Model):
    room_number = models.CharField(max_length=1)
    number_seats = models.PositiveIntegerField()
    name_office = models.ForeignKey(Office, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return str(self.room_number)


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    room_number = models.OneToOneField(Room, on_delete=models.PROTECT, null=False)
    date_from = models.DateField()
    date_to = models.DateField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
