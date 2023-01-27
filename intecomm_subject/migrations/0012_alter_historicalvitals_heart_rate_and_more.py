# Generated by Django 4.1.2 on 2023-01-27 02:45

from django.db import migrations
import edc_vitals.models.fields.heart_rate
import edc_vitals.models.fields.temperature


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_subject", "0011_remove_clinicalreviewbaseline_complications_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalvitals",
            name="heart_rate",
            field=edc_vitals.models.fields.heart_rate.HeartRateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalvitals",
            name="temperature",
            field=edc_vitals.models.fields.temperature.TemperatureField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="vitals",
            name="heart_rate",
            field=edc_vitals.models.fields.heart_rate.HeartRateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="vitals",
            name="temperature",
            field=edc_vitals.models.fields.temperature.TemperatureField(blank=True, null=True),
        ),
    ]
