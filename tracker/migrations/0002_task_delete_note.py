# Generated by Django 4.2.20 on 2025-06-26 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=100)),
                ("status", models.CharField(default="Pending", max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name="Note",
        ),
    ]
