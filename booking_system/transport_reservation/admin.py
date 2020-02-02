from django.contrib import admin

# Register your models here.
from .models import Vehicle_detail,Vehicle_Type,Pick,Drop
from .booking import Ticket

admin.site.register(Pick)
admin.site.register(Drop)
admin.site.register(Vehicle_Type)
admin.site.register(Vehicle_detail)
admin.site.register(Ticket)