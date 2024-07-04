# Generated by Django 4.2.7 on 2023-12-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_subject", "0133_bloodresultsfbc_intecomm_su_subject_3bd165_idx_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="clinicalreviewbaseline",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_67b2fa_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="clinicalreviewbaseline",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_bee688_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="clinicalreviewbaseline",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_99c261_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="complicationsbaseline",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_c4ed1f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="complicationsbaseline",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_00569e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="complicationsbaseline",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_a373c1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="complicationsfollowup",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_253434_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="complicationsfollowup",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_1ed4b6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="complicationsfollowup",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_53ced3_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="concomitantmedication",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_458d49_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="concomitantmedication",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_af63b0_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="concomitantmedication",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_fa7947_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dminitialreview",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_3991f4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dminitialreview",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_095258_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dminitialreview",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_64007e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dmmedicationadherence",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_4293d2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dmmedicationadherence",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_4c6294_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dmmedicationadherence",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_85ee39_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dmreview",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_1f36e4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dmreview",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_cc428d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="dmreview",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_85821d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefilldm",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_0b732d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefilldm",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_6d0dd5_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefilldm",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_bd9a3a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefillhiv",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_9cda3f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefillhiv",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_40e598_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefillhiv",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_4e128e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefillhtn",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_d0bd13_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefillhtn",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_585432_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugrefillhtn",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_b0da16_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugsupplydm",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_9bc54e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugsupplydm",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_dcc1d5_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugsupplyhiv",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_8acc20_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugsupplyhiv",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_610af9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugsupplyhtn",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_8c1dd6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="drugsupplyhtn",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_07c10a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="eq5d3l",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_c196bb_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="eq5d3l",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_84ab2e_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="eq5d3l",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_fa1acb_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="familyhistory",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_18752d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="familyhistory",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_f196cb_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="familyhistory",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_bc400c_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="glucose",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_430194_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="glucose",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_cb66f5_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="glucose",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_ef2a1c_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomics",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_a363c6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsassets",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_b6e56a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsassets",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_f5b8ac_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsassets",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_dc9bf6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicshouseholdhead",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_812007_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicshouseholdhead",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_f79c92_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicshouseholdhead",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_2184dc_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsincome",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_61d316_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsincome",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_1cd934_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsincome",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_7164a2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicspatient",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_7b191c_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicspatient",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_d0c929_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicspatient",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_355d6b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsproperty",
            index=models.Index(
                fields=["subject_visit", "site"], name="intecomm_su_subject_8f0447_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsproperty",
            index=models.Index(
                fields=["modified", "created"], name="intecomm_su_modifie_48227b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="healtheconomicsproperty",
            index=models.Index(
                fields=["user_modified", "user_created"], name="intecomm_su_user_mo_f50e97_idx"
            ),
        ),
    ]