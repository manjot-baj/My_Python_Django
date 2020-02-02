from django.db import models
from django.utils import timezone
from .models import Vehicle_detail, BaseModel
import random


def random_string():
    return str(random.randint(10000, 99999))


class Ticket(BaseModel):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'

    STATUS = ((PENDING, 'Pending'), (CONFIRMED, 'Confirmed'),)
    number = models.CharField(default=random_string, max_length=50, null=True,blank=False)
    date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    name = models.CharField(max_length=50, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=False)
    vehicle = models.ForeignKey(Vehicle_detail, on_delete=models.SET_NULL, null=True, blank=False)
    seats = models.IntegerField(default=1, null=True, blank=False)
    fare = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=False)
    status = models.CharField(choices=STATUS, default=PENDING, max_length=2)

    class Meta:
        db_table = 'Ticket'
        verbose_name = 'Ticket Booking'

    def __str__(self):
        return self.number
