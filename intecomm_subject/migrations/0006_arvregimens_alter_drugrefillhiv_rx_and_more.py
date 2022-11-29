# Generated by Django 4.1.2 on 2022-11-29 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_lists", "0002_delete_reasonsfortesting"),
        ("intecomm_subject", "0005_alter_clinicalreview_dm_reason_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArvRegimens",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("intecomm_lists.arvregimens",),
        ),
        migrations.AlterField(
            model_name="drugrefillhiv",
            name="rx",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="intecomm_subject.arvregimens",
                verbose_name="Which medicine did the patient receive today?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldrugrefillhiv",
            name="rx",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="intecomm_subject.arvregimens",
                verbose_name="Which medicine did the patient receive today?",
            ),
        ),
    ]
