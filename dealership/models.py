from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q

from dealership.apps import DealershipConfig


class Vehicle(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    year = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class Car(Vehicle):
    tank_size = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_type = models.CharField(max_length=64)


class ElectricCar(Vehicle):
    battery_capacity = models.DecimalField(max_digits=5, decimal_places=2)
    charging_time = models.DurationField()


class Motorcycle(Vehicle):
    tank_size = models.DecimalField(max_digits=5, decimal_places=2)
    has_sidecar = models.BooleanField(default=False)


CONTENT_TYPE_CHOICES = (
    Q(app_label=DealershipConfig.name, model=Car.__name__.lower())
    | Q(app_label=DealershipConfig.name, model=ElectricCar.__name__.lower())
    | Q(app_label=DealershipConfig.name, model=Motorcycle.__name__.lower())
)


class Sale(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=CONTENT_TYPE_CHOICES,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def get_related_object_instance(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def __str__(self):
        return f"{self.get_related_object_instance()} sold for ${self.price}"
