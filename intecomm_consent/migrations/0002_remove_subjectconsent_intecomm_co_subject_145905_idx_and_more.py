# Generated by Django 4.1.2 on 2022-11-22 22:52

import django.core.validators
from django.db import migrations, models
import django_crypto_fields.fields.encrypted_char_field


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_consent", "0001_initial"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="subjectconsent",
            name="intecomm_co_subject_145905_idx",
        ),
        migrations.AlterUniqueTogether(
            name="subjectconsent",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="historicalsubjectconsent",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="historicalsubjectconsent",
            name="last_name",
        ),
        migrations.AddField(
            model_name="historicalsubjectconsent",
            name="familiar_name",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Ensure name consists of letters only in upper case separated by single spaces",
                        regex="^(([A-Z]+ )*[A-Z]+)?$",
                    )
                ],
                verbose_name="How should we refer to you? (if we speak to you)",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectconsent",
            name="legal_name",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                db_index=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Ensure full name consists of letters only in upper case separated by single spaces",
                        regex="^(([A-Z]+ )*[A-Z]+)?$",
                    )
                ],
                verbose_name="Full name",
            ),
        ),
        migrations.AddField(
            model_name="subjectconsent",
            name="familiar_name",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Ensure name consists of letters only in upper case separated by single spaces",
                        regex="^(([A-Z]+ )*[A-Z]+)?$",
                    )
                ],
                verbose_name="How should we refer to you? (if we speak to you)",
            ),
        ),
        migrations.AddField(
            model_name="subjectconsent",
            name="legal_name",
            field=django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                blank=True,
                help_text=" (Encryption: RSA local)",
                max_length=71,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Ensure full name consists of letters only in upper case separated by single spaces",
                        regex="^(([A-Z]+ )*[A-Z]+)?$",
                    )
                ],
                verbose_name="Full name",
            ),
        ),
        migrations.AddIndex(
            model_name="subjectconsent",
            index=models.Index(
                fields=["subject_identifier", "legal_name", "dob", "initials", "version"],
                name="intecomm_co_subject_c503bc_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="subjectconsent",
            constraint=models.UniqueConstraint(
                models.F("subject_identifier"),
                models.F("version"),
                name="unique_consent_subject_id_and_version",
                violation_error_message="A subject with this identifier has already completed this version of the consent",
            ),
        ),
        migrations.AddConstraint(
            model_name="subjectconsent",
            constraint=models.UniqueConstraint(
                models.F("subject_identifier"),
                models.F("screening_identifier"),
                name="unique_consent_subject_id_screening_id",
            ),
        ),
        migrations.AddConstraint(
            model_name="subjectconsent",
            constraint=models.UniqueConstraint(
                models.F("familiar_name"),
                models.F("dob"),
                models.F("initials"),
                models.F("version"),
                name="unique_consent_name_dob_initials",
                violation_error_message="A subject with this 'familiar' name, dob and initials has already completed this version of the consent",
            ),
        ),
        migrations.RemoveField(
            model_name="subjectconsent",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="subjectconsent",
            name="last_name",
        ),
    ]