# Generated by Django 5.1 on 2024-10-04 14:28

import edc_utils.date
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_reports", "0022_rename_apptlocationqa_appointmentlocationqa_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointmentlocationqa",
            name="created",
            field=models.DateTimeField(default=edc_utils.date.get_utcnow),
        ),
        migrations.AlterField(
            model_name="diagnoses",
            name="created",
            field=models.DateTimeField(default=edc_utils.date.get_utcnow),
        ),
    ]