# Generated by Django 5.0.3 on 2024-03-13 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_subject", "0152_rename_visit_cost_careseekinga_care_visit_cost_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="careseekinga",
            old_name="visit_duration",
            new_name="care_visit_duration",
        ),
        migrations.RenameField(
            model_name="historicalcareseekinga",
            old_name="visit_duration",
            new_name="care_visit_duration",
        ),
    ]
