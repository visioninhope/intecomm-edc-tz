# Generated by Django 4.2.7 on 2023-12-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "intecomm_subject",
            "0130_remove_bloodresultsfbc_intecomm_su_subject_1b56bc_idx_and_more",
        ),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="drugrefillhtn",
            name="intecomm_su_subject_33642b_idx",
        ),
        migrations.RemoveIndex(
            model_name="eq5d3l",
            name="intecomm_su_subject_26cbd6_idx",
        ),
        migrations.RemoveIndex(
            model_name="familyhistory",
            name="intecomm_su_subject_70b52d_idx",
        ),
        migrations.RemoveIndex(
            model_name="glucose",
            name="intecomm_su_subject_d7452b_idx",
        ),
        migrations.RemoveIndex(
            model_name="healtheconomics",
            name="intecomm_su_subject_0fa533_idx",
        ),
        migrations.RemoveIndex(
            model_name="healtheconomicsassets",
            name="intecomm_su_subject_db2b9f_idx",
        ),
        migrations.RemoveIndex(
            model_name="healtheconomicshouseholdhead",
            name="intecomm_su_subject_70ec19_idx",
        ),
        migrations.RemoveIndex(
            model_name="healtheconomicsincome",
            name="intecomm_su_subject_cd28df_idx",
        ),
        migrations.RemoveIndex(
            model_name="healtheconomicspatient",
            name="intecomm_su_subject_9f534c_idx",
        ),
        migrations.RemoveIndex(
            model_name="healtheconomicsproperty",
            name="intecomm_su_subject_46df27_idx",
        ),
        migrations.RemoveIndex(
            model_name="hivinitialreview",
            name="intecomm_su_subject_105e1e_idx",
        ),
        migrations.RemoveIndex(
            model_name="hivmedicationadherence",
            name="intecomm_su_subject_0c187e_idx",
        ),
        migrations.RemoveIndex(
            model_name="hivreview",
            name="intecomm_su_subject_330463_idx",
        ),
        migrations.RemoveIndex(
            model_name="htninitialreview",
            name="intecomm_su_subject_26645e_idx",
        ),
        migrations.RemoveIndex(
            model_name="htnmedicationadherence",
            name="intecomm_su_subject_3c2519_idx",
        ),
        migrations.RemoveIndex(
            model_name="htnreview",
            name="intecomm_su_subject_68a66a_idx",
        ),
        migrations.RemoveIndex(
            model_name="icecapa",
            name="intecomm_su_subject_9061b4_idx",
        ),
        migrations.RemoveIndex(
            model_name="locationupdate",
            name="intecomm_su_subject_2ca9cc_idx",
        ),
        migrations.RemoveIndex(
            model_name="malariatest",
            name="intecomm_su_subject_dd6f65_idx",
        ),
        migrations.RemoveIndex(
            model_name="medications",
            name="intecomm_su_subject_f7efc4_idx",
        ),
        migrations.RemoveIndex(
            model_name="nextappointment",
            name="intecomm_su_subject_877d51_idx",
        ),
        migrations.RemoveIndex(
            model_name="otherbaselinedata",
            name="intecomm_su_subject_3430b9_idx",
        ),
        migrations.RemoveIndex(
            model_name="socialharms",
            name="intecomm_su_subject_99ad70_idx",
        ),
        migrations.RemoveIndex(
            model_name="subjectrequisition",
            name="intecomm_su_subject_eb844f_idx",
        ),
        migrations.RemoveIndex(
            model_name="subjectvisitmissed",
            name="intecomm_su_subject_8770a0_idx",
        ),
        migrations.RemoveIndex(
            model_name="urinedipsticktest",
            name="intecomm_su_subject_c1ab9f_idx",
        ),
        migrations.RemoveIndex(
            model_name="urinepregnancy",
            name="intecomm_su_subject_e044a5_idx",
        ),
        migrations.RemoveIndex(
            model_name="viralloadresult",
            name="intecomm_su_subject_91aacf_idx",
        ),
        migrations.RemoveIndex(
            model_name="vitals",
            name="intecomm_su_subject_204579_idx",
        ),
    ]