# Generated by Django 4.1.4 on 2022-12-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_dr_lpredict_dr_rprediict"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dr",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]