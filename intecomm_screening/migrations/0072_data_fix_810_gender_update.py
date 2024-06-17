# Generated by Django 4.2.11 on 2024-06-17 11:27

from django.db import migrations
from django.db.migrations import RunPython
from edc_constants.constants import FEMALE, MALE
from edc_utils import get_utcnow


def update_gender(apps, schema_editor):
    """Update gender from 'F' to 'M' for participant added to patient
    log (and subsequently screened and consented) with the wrong gender.

    See also:
        Redmine ticket: #810
        Protocol incident: VWFD-NPT2
    """
    for model in ["patientlog", "subjectscreening"]:
        model_cls = apps.get_model(f"intecomm_screening.{model}")
        obj = model_cls.objects.get(
            subject_identifier="107-105-0080-1",
            screening_identifier="SYKEZZEV",
            site_id=105,
            gender=FEMALE,
        )
        print(
            f"\n  * Updating {model_cls.__name__} gender for {obj.subject_identifier=} "
            f"({obj.screening_identifier=}) from '{FEMALE}' to '{MALE}' ..."
        )

        obj.modified = get_utcnow()
        obj.user_modified = __name__ if len(__name__) <= 50 else f"{__name__[:46]} ..."
        obj.gender = MALE
        obj.save_base(
            update_fields=[
                "gender",
                "modified",
                "user_modified",
            ]
        )

        print("  * Updated.")
    print("Done.")


class Migration(migrations.Migration):

    dependencies = [
        (
            "intecomm_screening",
            "0071_alter_historicalsubjectscreening_report_datetime_and_more",
        ),
    ]

    operations = [RunPython(update_gender)]
