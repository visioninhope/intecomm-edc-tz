# Generated by Django 4.2.3 on 2023-08-03 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_subject", "0072_auto_20230803_0305"),
    ]

    operations = [
        migrations.RenameField(
            model_name="healtheconomicspatient",
            old_name="pat_ethnicity",
            new_name="pat_ethnicity_old",
        ),
        migrations.RenameField(
            model_name="historicalhealtheconomicspatient",
            old_name="pat_ethnicity",
            new_name="pat_ethnicity_old",
        ),
    ]
