# Generated by Django 5.1.6 on 2025-03-13 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bibliotheque", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cd",
            old_name="name",
            new_name="nom",
        ),
        migrations.RenameField(
            model_name="dvd",
            old_name="name",
            new_name="nom",
        ),
        migrations.RenameField(
            model_name="livre",
            old_name="name",
            new_name="nom",
        ),
    ]
