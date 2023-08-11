# Generated by Django 4.2.3 on 2023-08-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "intecomm_subject",
            "0084_alter_healtheconomicsassets_external_wall_material_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="healtheconomicsassets",
            name="external_wall_material",
            field=models.CharField(
                choices=[
                    ("1", "Thatch, Straw"),
                    ("2", "Mud and poles"),
                    ("3", "Timber"),
                    ("OPTION_RETIRED", "Un-burnt bricks"),
                    ("5", "Bricks with mud"),
                    ("6", "Bricks with cement"),
                    ("7", "Cement blocks"),
                    ("8", "Stone"),
                    ("OTHER", "Other, specify ..."),
                ],
                max_length=25,
                verbose_name="What is the major construction material of the external wall?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicsassets",
            name="iron",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], max_length=15, verbose_name="Flat iron"
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicsassets",
            name="external_wall_material",
            field=models.CharField(
                choices=[
                    ("1", "Thatch, Straw"),
                    ("2", "Mud and poles"),
                    ("3", "Timber"),
                    ("OPTION_RETIRED", "Un-burnt bricks"),
                    ("5", "Bricks with mud"),
                    ("6", "Bricks with cement"),
                    ("7", "Cement blocks"),
                    ("8", "Stone"),
                    ("OTHER", "Other, specify ..."),
                ],
                max_length=25,
                verbose_name="What is the major construction material of the external wall?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicsassets",
            name="iron",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], max_length=15, verbose_name="Flat iron"
            ),
        ),
    ]