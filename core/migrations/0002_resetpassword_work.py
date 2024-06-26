# Generated by Django 5.0.2 on 2024-05-24 15:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ResetPassword",
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
                ("id_off", models.CharField(max_length=99999, verbose_name="")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Work",
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
                ("project_name", models.CharField(max_length=3500)),
                ("brand_name", models.CharField(max_length=3500)),
                ("agency_name", models.CharField(max_length=3500)),
                ("nom", models.CharField(max_length=3500)),
                ("period", models.CharField(max_length=3500)),
                ("short_info", models.CharField(max_length=3500)),
                ("position", models.CharField(max_length=3500)),
                ("point", models.CharField(max_length=3500)),
                ("strategy", models.CharField(max_length=3500)),
                ("idea", models.CharField(max_length=3500)),
                ("channel1", models.CharField(max_length=3500)),
                ("channel2", models.CharField(max_length=3500)),
                ("channel3", models.CharField(max_length=3500)),
                ("budget", models.CharField(max_length=3500)),
                ("desc", models.CharField(max_length=3500)),
                ("result", models.CharField(max_length=3500)),
                ("file", models.FileField(blank=True, null=True, upload_to="media/")),
                ("url", models.CharField(blank=True, max_length=3500, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.member",
                        verbose_name="Владелец",
                    ),
                ),
            ],
        ),
    ]
