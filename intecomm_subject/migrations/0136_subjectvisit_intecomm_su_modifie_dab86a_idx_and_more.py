# Generated by Django 4.2.7 on 2023-12-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_subject", "0135_hivinitialreview_intecomm_su_subject_a055c4_idx_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="subjectvisit",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_dab86a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="subjectvisit",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_f69a2b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="subjectvisitmissed",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_4156bd_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="subjectvisitmissed",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_4811c1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="subjectvisitmissed",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_fe71a2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="urinedipsticktest",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_c286ff_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="urinedipsticktest",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_4ae4df_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="urinedipsticktest",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_e6c69a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="urinepregnancy",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_5f4648_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="urinepregnancy",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_f7bfa9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="urinepregnancy",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_a8c595_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="viralloadresult",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_c4b38b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="viralloadresult",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_ec7d6d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="viralloadresult",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_9a68e1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="vitals",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_4ab411_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="vitals",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_b2e5cb_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="vitals",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_4457e4_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="subjectrequisition",
            constraint=models.UniqueConstraint(
                fields=("panel", "subject_visit"),
                name="intecomm_subject_subjectrequisition_panel_uniq",
            ),
        ),
    ]
