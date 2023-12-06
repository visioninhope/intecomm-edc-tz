# Generated by Django 4.2.7 on 2023-12-05 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_subject", "0129_alter_bloodresultsfbc_options_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="bloodresultsfbc",
            name="intecomm_su_subject_1b56bc_idx",
        ),
        migrations.RemoveIndex(
            model_name="bloodresultsglu",
            name="intecomm_su_subject_da7231_idx",
        ),
        migrations.RemoveIndex(
            model_name="bloodresultshba1c",
            name="intecomm_su_subject_8d1ef7_idx",
        ),
        migrations.RemoveIndex(
            model_name="bloodresultsins",
            name="intecomm_su_subject_fa522d_idx",
        ),
        migrations.RemoveIndex(
            model_name="bloodresultslft",
            name="intecomm_su_subject_765b18_idx",
        ),
        migrations.RemoveIndex(
            model_name="bloodresultslipid",
            name="intecomm_su_subject_676609_idx",
        ),
        migrations.RemoveIndex(
            model_name="bloodresultsrft",
            name="intecomm_su_subject_e7a1d8_idx",
        ),
        migrations.RemoveIndex(
            model_name="clinicalnote",
            name="intecomm_su_subject_2180e7_idx",
        ),
        migrations.RemoveIndex(
            model_name="clinicalreview",
            name="intecomm_su_subject_e0c962_idx",
        ),
        migrations.RemoveIndex(
            model_name="clinicalreviewbaseline",
            name="intecomm_su_subject_669150_idx",
        ),
        migrations.RemoveIndex(
            model_name="complicationsbaseline",
            name="intecomm_su_subject_fddb9d_idx",
        ),
        migrations.RemoveIndex(
            model_name="complicationsfollowup",
            name="intecomm_su_subject_3a5d93_idx",
        ),
        migrations.RemoveIndex(
            model_name="concomitantmedication",
            name="intecomm_su_subject_d4d0fa_idx",
        ),
        migrations.RemoveIndex(
            model_name="dminitialreview",
            name="intecomm_su_subject_532279_idx",
        ),
        migrations.RemoveIndex(
            model_name="dmmedicationadherence",
            name="intecomm_su_subject_ab34b8_idx",
        ),
        migrations.RemoveIndex(
            model_name="dmreview",
            name="intecomm_su_subject_bfb20e_idx",
        ),
        migrations.RemoveIndex(
            model_name="drugrefilldm",
            name="intecomm_su_subject_2df562_idx",
        ),
        migrations.RemoveIndex(
            model_name="drugrefillhiv",
            name="intecomm_su_subject_978ed1_idx",
        ),
    ]
