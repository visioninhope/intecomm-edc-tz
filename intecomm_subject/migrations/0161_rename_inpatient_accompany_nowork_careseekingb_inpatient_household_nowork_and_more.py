# Generated by Django 5.0.4 on 2024-04-10 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_subject", "0160_careseekingb_inpatient_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="careseekingb",
            old_name="inpatient_accompany_nowork",
            new_name="inpatient_household_nowork",
        ),
        migrations.RenameField(
            model_name="careseekingb",
            old_name="inpatient_accompany_nowork_days",
            new_name="inpatient_household_nowork_days",
        ),
        migrations.RenameField(
            model_name="historicalcareseekingb",
            old_name="inpatient_accompany_nowork",
            new_name="inpatient_household_nowork",
        ),
        migrations.RenameField(
            model_name="historicalcareseekingb",
            old_name="inpatient_accompany_nowork_days",
            new_name="inpatient_household_nowork_days",
        ),
    ]
