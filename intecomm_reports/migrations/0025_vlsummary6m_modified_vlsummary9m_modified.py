# Generated by Django 5.1.2 on 2024-10-31 01:54

import edc_utils.date
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_reports", "0024_alter_missingvldrawdates_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="vlsummary6m",
            name="modified",
            field=models.DateTimeField(default=edc_utils.date.get_utcnow),
        ),
        migrations.AddField(
            model_name="vlsummary9m",
            name="modified",
            field=models.DateTimeField(default=edc_utils.date.get_utcnow),
        ),
    ]
