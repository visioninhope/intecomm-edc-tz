# Generated by Django 4.2.4 on 2023-08-30 21:32
import sys

from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations
from django.db.migrations import RunPython
from edc_constants.constants import YES
from edc_utils import get_utcnow


def update_willing_to_screen_for_tz(apps, schema_editor):
    """Update any patientlog instance in a group where
    `willing_to_screen` and `stable` is not YES and the patient
    has already been added to a group.
    """
    patient_group_cls = apps.get_model("intecomm_group.patientgroup")
    for patient_group in patient_group_cls.objects.all().order_by("site__id", "name"):
        total = patient_group.patients.all().count()
        if total > 0:
            n = 0
            for patientlog in patient_group.patients.all():
                try:
                    patientlog.subjectscreening
                except ObjectDoesNotExist:
                    patientlog.willing_to_screen = YES
                    patientlog.stable = YES
                    patientlog.user_modified = "erikvw"
                    patientlog.modified = get_utcnow()
                    patientlog.comment = "[auto-updated] willing_to_screen=YES"
                    patientlog.save()
                    n += 1
            if n > 0:
                sys.stdout.write(
                    f"\nUpdated {patient_group.site.id} {patient_group.name} "
                    f"{patient_group.status} {n}/{total}\n"
                )


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_screening", "0061_historicalpatientlog_comment_and_more"),
    ]

    operations = [RunPython(update_willing_to_screen_for_tz)]
