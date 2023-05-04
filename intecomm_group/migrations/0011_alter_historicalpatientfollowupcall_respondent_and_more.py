# Generated by Django 4.1.7 on 2023-05-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_group", "0010_alter_patientgroup_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpatientfollowupcall",
            name="respondent",
            field=models.CharField(
                choices=[
                    ("patient", "Patient"),
                    ("family", "Family"),
                    ("friend", "friend"),
                    ("OTHER", "other"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="patientfollowupcall",
            name="respondent",
            field=models.CharField(
                choices=[
                    ("patient", "Patient"),
                    ("family", "Family"),
                    ("friend", "friend"),
                    ("OTHER", "other"),
                    ("N/A", "Not applicable"),
                ],
                default="N/A",
                max_length=15,
            ),
        ),
    ]
