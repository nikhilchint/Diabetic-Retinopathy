# Generated by Django 4.1.4 on 2022-12-12 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_rename_email1_dr_email_rename_name1_dr_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dr",
            old_name="email",
            new_name="email1",
        ),
        migrations.RenameField(
            model_name="dr",
            old_name="name",
            new_name="name1",
        ),
        migrations.RenameField(
            model_name="dr",
            old_name="phone",
            new_name="phone1",
        ),
    ]
