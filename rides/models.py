from django.db import models

class User(models.Model):
    ADMIN = 'admin'
    OTHER = 'other'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (OTHER, 'Other'),
    ]

    id_user = models.AutoField(primary_key=True)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Ride(models.Model):
    EN_ROUTE = 'en-route'
    PICKUP = 'pickup'
    DROPOFF = 'dropoff'

    STATUS_CHOICES = [
        (EN_ROUTE, 'En-Route'),
        (PICKUP, 'Pickup'),
        (DROPOFF, 'Dropoff'),
    ]

    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    id_rider = models.ForeignKey(User, related_name='rides_as_rider', on_delete=models.CASCADE)
    id_driver = models.ForeignKey(User, related_name='rides_as_driver', on_delete=models.CASCADE)
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()

    def __str__(self):
        return f"Ride {self.id_ride}"

class RideEvent(models.Model):
    id_ride_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(Ride, related_name='events', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.id_ride_event} for Ride {self.id_ride.id_ride}"
