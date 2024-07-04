# Generated by Django 4.2.9 on 2024-02-06 04:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_subject", "0141_remove_viralloadresult_requisition_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalhtninitialreview",
            name="managed_by_old",
            field=models.CharField(
                blank=True,
                choices=[
                    ("drugs", "Drugs / Medicine"),
                    ("diet_lifestyle", "Diet and lifestyle alone"),
                ],
                default="N/A",
                help_text="If patient is taking medication, complete the Drug Refill CRF.",
                max_length=15,
                verbose_name="How is the patient's hypertension managed?",
            ),
        ),
        migrations.AlterField(
            model_name="htninitialreview",
            name="managed_by_old",
            field=models.CharField(
                blank=True,
                choices=[
                    ("drugs", "Drugs / Medicine"),
                    ("diet_lifestyle", "Diet and lifestyle alone"),
                ],
                default="N/A",
                help_text="If patient is taking medication, complete the Drug Refill CRF.",
                max_length=15,
                verbose_name="How is the patient's hypertension managed?",
            ),
        ),
    ]