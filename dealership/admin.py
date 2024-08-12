from django.contrib import admin

from dealership.models import Motorcycle, ElectricCar, Car, Sale

admin.site.register(Car)
admin.site.register(ElectricCar)
admin.site.register(Motorcycle)
admin.site.register(Sale)
