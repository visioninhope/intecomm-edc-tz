# Generated by Django 4.2.7 on 2023-12-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_ae", "0011_alter_aefollowup_options_alter_aeinitial_options_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="aefollowup",
            index=models.Index(
                fields=["subject_identifier"], name="intecomm_ae_subject_a0869e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="aefollowup",
            index=models.Index(
                fields=[
                    "action_identifier",
                    "action_item",
                    "related_action_item",
                    "parent_action_item",
                ],
                name="intecomm_ae_action__3099a7_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="aefollowup",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_ae_modifie_d686c6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="aefollowup",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_ae_user_mo_4e2aff_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="aeinitial",
            index=models.Index(
                fields=["subject_identifier"], name="intecomm_ae_subject_155c2e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="aeinitial",
            index=models.Index(
                fields=[
                    "action_identifier",
                    "action_item",
                    "related_action_item",
                    "parent_action_item",
                ],
                name="intecomm_ae_action__0c4217_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="aeinitial",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_ae_modifie_fdff72_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="aeinitial",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_ae_user_mo_4bd6c1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="aesusar",
            index=models.Index(
                fields=["subject_identifier"], name="intecomm_ae_subject_50e2e0_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="aesusar",
            index=models.Index(
                fields=[
                    "action_identifier",
                    "action_item",
                    "related_action_item",
                    "parent_action_item",
                ],
                name="intecomm_ae_action__feb740_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="aesusar",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_ae_modifie_ae0678_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="aesusar",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_ae_user_mo_927aee_idx"
            ),
        ),
    ]
