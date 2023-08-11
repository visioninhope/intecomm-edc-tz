# Generated by Django 4.2.3 on 2023-07-25 17:58
from django.db import migrations
from tqdm import tqdm


def update_next_appointment(apps, schema_editor):
    model_cls = apps.get_model("intecomm_subject", "nextappointment")
    subjectvisit_model_cls = apps.get_model("intecomm_subject", "subjectvisit")
    visitschedule_model_cls = apps.get_model("edc_visit_schedule", "visitschedule")
    total = model_cls.objects.all().count()
    print("\n")
    for obj in tqdm(model_cls.objects.all(), total=total):
        subject_visit = subjectvisit_model_cls.objects.get(id=obj.subject_visit_id)
        obj.visitschedule_id = visitschedule_model_cls.objects.get(
            visit_schedule_name=subject_visit.visit_schedule_name,
            schedule_name=subject_visit.schedule_name,
            visit_code=obj.best_visit_code,
        ).id
        obj.save_base(update_fields=["visitschedule_id"])
    print("\n")


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_subject", "0062_historicalclinicalnote_clinicalnote"),
    ]

    operations = [migrations.RunPython(update_next_appointment)]