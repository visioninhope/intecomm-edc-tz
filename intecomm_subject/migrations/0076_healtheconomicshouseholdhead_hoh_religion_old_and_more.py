# Generated by Django 4.2.3 on 2023-08-03 03:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_subject", "0075_auto_20230803_0459"),
    ]

    operations = [
        migrations.RenameField(
            model_name="historicalhealtheconomicshouseholdhead",
            old_name="hoh_religion",
            new_name="hoh_religion_old",
        ),
        migrations.RenameField(
            model_name="healtheconomicshouseholdhead",
            old_name="hoh_religion",
            new_name="hoh_religion_old",
        ),
        migrations.RenameField(
            model_name="historicalhealtheconomicspatient",
            old_name="pat_religion",
            new_name="pat_religion_old",
        ),
        migrations.RenameField(
            model_name="healtheconomicspatient",
            old_name="pat_religion",
            new_name="pat_religion_old",
        ),
    ]
