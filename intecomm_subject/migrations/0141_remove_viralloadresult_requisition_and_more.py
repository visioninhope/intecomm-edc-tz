# Generated by Django 4.2.9 on 2024-02-01 15:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_subject", "0140_historicalhivreview_drawn_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="viralloadresult",
            name="requisition",
        ),
        migrations.RemoveField(
            model_name="viralloadresult",
            name="site",
        ),
        migrations.RemoveField(
            model_name="viralloadresult",
            name="subject_visit",
        ),
        migrations.DeleteModel(
            name="HistoricalViralLoadResult",
        ),
        migrations.DeleteModel(
            name="ViralLoadResult",
        ),
    ]
