# Generated by Django 4.1.7 on 2023-05-03 18:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("flights", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Flights",
            new_name="Flight",
        ),
    ]
