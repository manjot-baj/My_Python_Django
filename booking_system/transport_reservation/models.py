from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BaseModel(models.Model):
    create_date = models.DateTimeField(default=timezone.now, null=True, blank=True, editable=False)
    write_date = models.DateTimeField(default=timezone.now, null=True, blank=True, editable=False)
    create_user = models.ForeignKey(
        User, related_name='created_by_%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL, null=True, editable=False)
    write_user = models.ForeignKey(
        User, related_name='written_by_%(app_label)s_%(class)s_related',
        on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        return super(BaseModel, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class Pick(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'pick_area'
        verbose_name = 'Pick Area'

    def __str__(self):
        return self.name


class Drop(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'drop_area'
        verbose_name = 'Drop Area'

    def __str__(self):
        return self.name


class Vehicle_Type(BaseModel):
    AC = 'AC'
    NON_AC = 'NAC'

    TYPES = ((AC, 'AC'),
             (NON_AC, 'Non AC'),)

    name = models.CharField(max_length=50, null=True, blank=False)
    type = models.CharField(choices=TYPES, default=AC, max_length=10)

    class Meta:
        db_table = 'vehicle_type'
        verbose_name = 'Vehicle Type'

    def __str__(self):
        return self.name


class Vehicle_detail(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    type = models.ForeignKey(Vehicle_Type, on_delete=models.SET_NULL, null=True, blank=False)
    arriving_time = models.TimeField(null=True, blank=False)
    depature_time = models.TimeField(null=True, blank=False)
    arriving_from = models.ForeignKey(Pick, on_delete=models.SET_NULL, null=True, blank=False)
    depature_at = models.ForeignKey(Drop, on_delete=models.SET_NULL, null=True, blank=False)
    fare = models.DecimalField(max_digits=9, decimal_places=2)
    no_of_seats = models.IntegerField(default=1,null=True, blank=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'vehicle_details'
        verbose_name = 'Vehicle Details'

    def __str__(self):
        return self.name
