# Generated by Django 4.2.1 on 2023-06-30 03:08

import edc_utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_screening", "0033_remove_consentrefusal_subject_identifier_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consentrefusal",
            name="screening_identifier",
            field=models.CharField(editable=False, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name="historicalconsentrefusal",
            name="screening_identifier",
            field=models.CharField(db_index=True, editable=False, max_length=36),
        ),
        migrations.AlterField(
            model_name="historicalpatientlog",
            name="screening_identifier",
            field=models.CharField(
                default=edc_utils.get_uuid,
                help_text="Auto populated when screening form is complete",
                max_length=36,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatientlog",
            name="subject_identifier",
            field=models.CharField(
                default=edc_utils.get_uuid,
                help_text="Auto populated when consent form is complete",
                max_length=36,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patientlog",
            name="screening_identifier",
            field=models.CharField(
                default=edc_utils.get_uuid,
                help_text="Auto populated when screening form is complete",
                max_length=36,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="patientlog",
            name="subject_identifier",
            field=models.CharField(
                default=edc_utils.get_uuid,
                help_text="Auto populated when consent form is complete",
                max_length=36,
                null=True,
            ),
        ),
    ]