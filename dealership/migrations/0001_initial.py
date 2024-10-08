# Generated by Django 5.1 on 2024-08-12 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("make", models.CharField(max_length=64)),
                ("model", models.CharField(max_length=64)),
                ("year", models.IntegerField()),
                ("tank_size", models.DecimalField(decimal_places=2, max_digits=5)),
                ("fuel_type", models.CharField(max_length=64)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ElectricCar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("make", models.CharField(max_length=64)),
                ("model", models.CharField(max_length=64)),
                ("year", models.IntegerField()),
                (
                    "battery_capacity",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("charging_time", models.DurationField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Motorcycle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("make", models.CharField(max_length=64)),
                ("model", models.CharField(max_length=64)),
                ("year", models.IntegerField()),
                ("tank_size", models.DecimalField(decimal_places=2, max_digits=5)),
                ("has_sidecar", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "content_type",
                    models.ForeignKey(
                        limit_choices_to=models.Q(
                            models.Q(("app_label", "dealership"), ("model", "car")),
                            models.Q(
                                ("app_label", "dealership"), ("model", "electriccar")
                            ),
                            models.Q(
                                ("app_label", "dealership"), ("model", "motorcycle")
                            ),
                            _connector="OR",
                        ),
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["content_type", "object_id"],
                        name="dealership__content_248b19_idx",
                    )
                ],
            },
        ),
    ]
