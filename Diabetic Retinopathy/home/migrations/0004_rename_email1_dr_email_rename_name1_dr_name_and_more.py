# Generated by Django 4.1.4 on 2022-12-12 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_dr"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dr",
            old_name="email1",
            new_name="email",
        ),
        migrations.RenameField(
            model_name="dr",
            old_name="name1",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="dr",
            old_name="phone1",
            new_name="phone",
        ),
    ]
