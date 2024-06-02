# Generated by Django 5.0.2 on 2024-05-27 09:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_resetpassword_work"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Jury",
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
                ("name", models.CharField(max_length=250, verbose_name="ФИО")),
                ("email", models.CharField(max_length=3500, verbose_name="E-mail")),
                ("password", models.CharField(max_length=250, verbose_name="Пароль")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Закреплено за пользователем",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JuryGroups",
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
                ("users", models.ManyToManyField(to="core.jury")),
            ],
        ),
    ]