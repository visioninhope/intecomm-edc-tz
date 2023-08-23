# Generated by Django 4.2.4 on 2023-08-16 21:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_lists", "0008_medicationshortagereasons"),
        ("intecomm_subject", "0104_historicallocationupdate_locationupdate"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicallocationupdate",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Location update",
                "verbose_name_plural": "historical Location updates",
            },
        ),
        migrations.AlterModelOptions(
            name="locationupdate",
            options={
                "default_manager_name": "objects",
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Location update",
                "verbose_name_plural": "Location updates",
            },
        ),
        migrations.AddField(
            model_name="dmmedicationadherence",
            name="meds_missed_in_days",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you miss taking your medication",
            ),
        ),
        migrations.AddField(
            model_name="dmmedicationadherence",
            name="meds_shortage_in_days",
            field=models.IntegerField(
                blank=True,
                help_text="That is, your supply of medication was finished",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you NOT HAVE medication to take",
            ),
        ),
        migrations.AddField(
            model_name="dmmedicationadherence",
            name="meds_shortage_reason",
            field=models.ManyToManyField(
                blank=True,
                to="intecomm_lists.medicationshortagereasons",
                verbose_name="Reasons for not having medications (supply/shortage)",
            ),
        ),
        migrations.AddField(
            model_name="historicaldmmedicationadherence",
            name="meds_missed_in_days",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you miss taking your medication",
            ),
        ),
        migrations.AddField(
            model_name="historicaldmmedicationadherence",
            name="meds_shortage_in_days",
            field=models.IntegerField(
                blank=True,
                help_text="That is, your supply of medication was finished",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you NOT HAVE medication to take",
            ),
        ),
        migrations.AddField(
            model_name="historicalhivmedicationadherence",
            name="meds_missed_in_days",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you miss taking your medication",
            ),
        ),
        migrations.AddField(
            model_name="historicalhivmedicationadherence",
            name="meds_shortage_in_days",
            field=models.IntegerField(
                blank=True,
                help_text="That is, your supply of medication was finished",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you NOT HAVE medication to take",
            ),
        ),
        migrations.AddField(
            model_name="historicalhtnmedicationadherence",
            name="meds_missed_in_days",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you miss taking your medication",
            ),
        ),
        migrations.AddField(
            model_name="historicalhtnmedicationadherence",
            name="meds_shortage_in_days",
            field=models.IntegerField(
                blank=True,
                help_text="That is, your supply of medication was finished",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you NOT HAVE medication to take",
            ),
        ),
        migrations.AddField(
            model_name="hivmedicationadherence",
            name="meds_missed_in_days",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you miss taking your medication",
            ),
        ),
        migrations.AddField(
            model_name="hivmedicationadherence",
            name="meds_shortage_in_days",
            field=models.IntegerField(
                blank=True,
                help_text="That is, your supply of medication was finished",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you NOT HAVE medication to take",
            ),
        ),
        migrations.AddField(
            model_name="hivmedicationadherence",
            name="meds_shortage_reason",
            field=models.ManyToManyField(
                blank=True,
                to="intecomm_lists.medicationshortagereasons",
                verbose_name="Reasons for not having medications (supply/shortage)",
            ),
        ),
        migrations.AddField(
            model_name="htnmedicationadherence",
            name="meds_missed_in_days",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you miss taking your medication",
            ),
        ),
        migrations.AddField(
            model_name="htnmedicationadherence",
            name="meds_shortage_in_days",
            field=models.IntegerField(
                blank=True,
                help_text="That is, your supply of medication was finished",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(180),
                ],
                verbose_name="Since we last saw you, for how many days did you NOT HAVE medication to take",
            ),
        ),
        migrations.AddField(
            model_name="htnmedicationadherence",
            name="meds_shortage_reason",
            field=models.ManyToManyField(
                blank=True,
                to="intecomm_lists.medicationshortagereasons",
                verbose_name="Reasons for not having medications (supply/shortage)",
            ),
        ),
    ]
