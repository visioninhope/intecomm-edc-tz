# Generated by Django 4.2.11 on 2024-07-03 23:52

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import edc_sites.managers
import edc_utils.date


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("intecomm_reports", "0007_auto_20240702_0734"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vl",
            options={
                "managed": False,
                "verbose_name": "Viral loads",
                "verbose_name_plural": "Viral loads",
            },
        ),
        migrations.AlterModelOptions(
            name="vlsummary",
            options={
                "verbose_name": "Viral load summary (endline >= 9m)",
                "verbose_name_plural": "Viral load summary (endline >= 9m)",
            },
        ),
        migrations.AlterModelManagers(
            name="vlsummary",
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("on_site", edc_sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name="vlsummary",
            name="expected",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="vlsummary",
            name="last_vl_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="vlsummary",
            name="next_vl_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="vlsummary",
            name="offschedule_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="vlsummary",
            name="offset",
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name="VlSummary2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("subject_identifier", models.CharField(max_length=50, unique=True)),
                (
                    "report_model",
                    models.CharField(default="intecomm_reports.vlsummary", max_length=50),
                ),
                ("created", models.DateTimeField(default=edc_utils.date.get_utcnow)),
                ("baseline_date", models.DateField(null=True)),
                ("baseline_vl_date", models.DateField(null=True)),
                ("endline_vl_date", models.DateField(null=True)),
                ("baseline_vl", models.IntegerField(null=True)),
                ("endline_vl", models.IntegerField(null=True)),
                ("offschedule_date", models.DateField(null=True)),
                ("last_vl_date", models.DateField(null=True)),
                ("next_vl_date", models.DateField(null=True)),
                ("expected", models.BooleanField(null=True)),
                ("offset", models.IntegerField(null=True)),
                (
                    "site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="sites.site"
                    ),
                ),
            ],
            options={
                "verbose_name": "Viral load summary (endline >= 6m)",
                "verbose_name_plural": "Viral load summary (endline >= 6m)",
            },
            managers=[
                ("objects", django.db.models.manager.Manager()),
                ("on_site", edc_sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
