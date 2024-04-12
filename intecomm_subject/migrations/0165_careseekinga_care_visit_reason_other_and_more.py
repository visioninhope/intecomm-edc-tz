# Generated by Django 5.0.4 on 2024-04-12 00:53

import django.core.validators
import edc_model_fields.fields.custom_django_fields
import edc_model_fields.fields.other_charfield
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("intecomm_lists", "0012_visitreasons_custom_name"),
        ("intecomm_subject", "0164_alter_careseekinga_money_source_main_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="careseekinga",
            name="care_visit_reason_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                metadata="FMEDCONDOTHER1",
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalcareseekinga",
            name="care_visit_reason_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                metadata="FMEDCONDOTHER1",
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AlterField(
            model_name="bloodresultsins",
            name="fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="care_visit_cost",
            field=edc_model_fields.fields.custom_django_fields.IntegerField2(
                help_text="In local currency. If nothing spent on healthworker and consultation fees, enter `0`",
                metadata="FFEECOST1",
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999999),
                ],
                verbose_name="How much money did you spend on healthworker and consultation fees during today’s visit?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="care_visit_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="something like 1h20m, 11h5m, etc",
                max_length=5,
                metadata="FFACTIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How much time did you spend during your visit today -- from arrival to this place until the end of your visit?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="food_cost",
            field=edc_model_fields.fields.custom_django_fields.IntegerField2(
                help_text="In local currency. If nothing spent on food, drink or other refreshments, enter `0`",
                metadata="FFOODCOST1",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999999),
                ],
                verbose_name="Thinking about yourself and anyone that accompanied you, how much did you have to pay for food, drink or other refreshments during your travel or during your visit? (e.g. food, drink, etc.)",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="med_conditions",
            field=edc_model_fields.fields.custom_django_fields.ManyToManyField2(
                blank=True,
                metadata="FMEDCOND1",
                to="intecomm_lists.conditions",
                verbose_name="What were the medicines were for?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="med_prescribed",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                metadata="FMED1",
                verbose_name="Were you prescribed any medicines during today’s visit?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="travel_cost",
            field=edc_model_fields.fields.custom_django_fields.IntegerField2(
                help_text="In local currency. If nothing spent on travel, enter `0`",
                metadata="FTRAVCOST1",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999999),
                ],
                verbose_name="Thinking about yourself and anyone that accompanied you, how much was spent on travel from your home to reach here?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="travel_time",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="something like 1h20m, 11h5m, etc",
                max_length=5,
                metadata="FTRATIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long did it take you to reach here?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="wait_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="something like 1h20m, 11h5m, etc",
                max_length=5,
                metadata="FWAITIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How much time did you spend waiting?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekinga",
            name="with_hcw_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="something like 1h20m, 11h5m, etc",
                max_length=5,
                metadata="FWORKTIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How much time did you spend with the healthcare worker?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekingb",
            name="care_visit_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="in hours and minutes (format HH:MM)",
                max_length=5,
                metadata="FOUTTIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="Roughly how much time did you spend during your last/most recent visit?",
            ),
        ),
        migrations.AlterField(
            model_name="careseekingb",
            name="travel_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="in hours and minutes (format HH:MM)",
                max_length=5,
                metadata="FOUTTRATIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long did it take you to get there?",
            ),
        ),
        migrations.AlterField(
            model_name="dminitialreview",
            name="glucose_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long did they fast (in hours and minutes)?",
            ),
        ),
        migrations.AlterField(
            model_name="dmreview",
            name="glucose_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AlterField(
            model_name="glucose",
            name="glucose_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalbloodresultsins",
            name="fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekinga",
            name="care_visit_cost",
            field=edc_model_fields.fields.custom_django_fields.IntegerField2(
                help_text="In local currency. If nothing spent on healthworker and consultation fees, enter `0`",
                metadata="FFEECOST1",
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999999),
                ],
                verbose_name="How much money did you spend on healthworker and consultation fees during today’s visit?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekinga",
            name="care_visit_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="something like 1h20m, 11h5m, etc",
                max_length=5,
                metadata="FFACTIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How much time did you spend during your visit today -- from arrival to this place until the end of your visit?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekinga",
            name="food_cost",
            field=edc_model_fields.fields.custom_django_fields.IntegerField2(
                help_text="In local currency. If nothing spent on food, drink or other refreshments, enter `0`",
                metadata="FFOODCOST1",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999999),
                ],
                verbose_name="Thinking about yourself and anyone that accompanied you, how much did you have to pay for food, drink or other refreshments during your travel or during your visit? (e.g. food, drink, etc.)",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekinga",
            name="med_prescribed",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=25,
                metadata="FMED1",
                verbose_name="Were you prescribed any medicines during today’s visit?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekinga",
            name="travel_cost",
            field=edc_model_fields.fields.custom_django_fields.IntegerField2(
                help_text="In local currency. If nothing spent on travel, enter `0`",
                metadata="FTRAVCOST1",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999999),
                ],
                verbose_name="Thinking about yourself and anyone that accompanied you, how much was spent on travel from your home to reach here?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekinga",
            name="travel_time",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="something like 1h20m, 11h5m, etc",
                max_length=5,
                metadata="FTRATIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long did it take you to reach here?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekinga",
            name="wait_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="something like 1h20m, 11h5m, etc",
                max_length=5,
                metadata="FWAITIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How much time did you spend waiting?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekinga",
            name="with_hcw_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="something like 1h20m, 11h5m, etc",
                max_length=5,
                metadata="FWORKTIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How much time did you spend with the healthcare worker?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekingb",
            name="care_visit_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="in hours and minutes (format HH:MM)",
                max_length=5,
                metadata="FOUTTIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="Roughly how much time did you spend during your last/most recent visit?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcareseekingb",
            name="travel_duration",
            field=edc_model_fields.fields.custom_django_fields.CharField2(
                help_text="in hours and minutes (format HH:MM)",
                max_length=5,
                metadata="FOUTTRATIME1",
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long did it take you to get there?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldminitialreview",
            name="glucose_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long did they fast (in hours and minutes)?",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldmreview",
            name="glucose_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalglucose",
            name="glucose_fasting_duration_str",
            field=models.CharField(
                blank=True,
                help_text="As reported by patient. Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^([0-9]{1,3}h([0-5]?[0-9]m)?)$",
                        message="Invalid format. Please insert two numeric values followed by “h” for hours, and two numeric values followed by “m” for minute. For example, 01h20m, 00h35m, and so on",
                    )
                ],
                verbose_name="How long have they fasted in hours and/or minutes?",
            ),
        ),
    ]
