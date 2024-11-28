# Generated by Django 5.0.8 on 2024-08-27 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "intecomm_reports",
            "0018_alter_eos_options_alter_subjectstransferred_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="diagnoses",
            options={
                "default_manager_name": "objects",
                "default_permissions": ("view", "export", "viewallsites"),
                "verbose_name": "Current Conditions",
                "verbose_name_plural": "Current Conditions",
            },
        ),
        migrations.AlterModelOptions(
            name="missingvldrawdates",
            options={
                "default_permissions": ("view", "export", "viewallsites"),
                "verbose_name": "Viral load: Missing draw date",
                "verbose_name_plural": "Viral load: Missing draw dates",
            },
        ),
        migrations.AlterModelOptions(
            name="vlsummary6m",
            options={
                "default_permissions": ("view", "export", "viewallsites"),
                "verbose_name": "Viral load summary (endline >= 6m)",
                "verbose_name_plural": "Viral load summary (endline >= 6m)",
            },
        ),
        migrations.AlterModelOptions(
            name="vlsummary9m",
            options={
                "default_permissions": ("view", "export", "viewallsites"),
                "verbose_name": "Viral load summary (endline >= 9m)",
                "verbose_name_plural": "Viral load summary (endline >= 9m)",
            },
        ),
    ]