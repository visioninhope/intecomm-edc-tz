# Generated by Django 4.2.11 on 2024-06-18 04:21
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations
from django.db.migrations import RunPython
from edc_constants.constants import FEMALE, MALE
from edc_utils import get_utcnow


def update_gender(apps, schema_editor):
    """Update gender from 'M' to 'F' for participant added to patient
    log (and subsequently screened and consented) with the wrong gender.

    See also:
        Redmine ticket: #812
        Protocol incident: F2DV-PMTV
    """
    for model in ["patientlog", "subjectscreening"]:
        model_cls = apps.get_model(f"intecomm_screening.{model}")
        try:
            obj = model_cls.objects.get(
                subject_identifier="107-110-0045-4",
                screening_identifier="SU2VXC66",
                site_id=110,
                gender=MALE,
            )
        except ObjectDoesNotExist:
            print("Matching object does not exist. Skipping ...")
            break
        else:
            print(
                f"\n  * Updating {model_cls.__name__} gender for {obj.subject_identifier=} "
                f"({obj.screening_identifier=}) from '{MALE}' to '{FEMALE}' ..."
            )

            obj.modified = get_utcnow()
            obj.user_modified = __name__ if len(__name__) <= 50 else f"{__name__[:46]} ..."
            obj.gender = FEMALE
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
        ("intecomm_screening", "0072_data_fix_810_gender_update"),
        ("intecomm_consent", "0026_data_fix_810_gender_update"),
    ]

    operations = [RunPython(update_gender)]