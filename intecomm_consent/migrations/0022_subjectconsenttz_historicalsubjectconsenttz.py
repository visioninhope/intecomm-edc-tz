# Generated by Django 5.0 on 2024-01-28 23:28

import uuid

import _socket
import django.contrib.sites.managers
import django.core.validators
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_crypto_fields.fields.identity_field
import django_crypto_fields.fields.lastname_field
import django_revision.revision_field
import edc_consent.validators
import edc_model.validators.date
import edc_model_fields.fields.date_estimated
import edc_protocol.validators
import simple_history.models
from django.conf import settings
from django.db import migrations, models

import intecomm_consent.models.subject_consent


class Migration(migrations.Migration):
    dependencies = [
        ("intecomm_consent", "0021_remove_subjectreconsent_action_item_and_more"),
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SubjectConsentTz",
            fields=[],
            options={
                "verbose_name": "Subject Consent (Tanzania)",
                "verbose_name_plural": "Subject Consents (Tanzania)",
                "abstract": False,
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("intecomm_consent.subjectconsent",),
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", intecomm_consent.models.subject_consent.ConsentObjectsManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalSubjectConsentTz",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                        verbose_name="Hostname created",
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                        verbose_name="Hostname modified",
                    ),
                ),
                (
                    "device_created",
                    models.CharField(blank=True, max_length=10, verbose_name="Device created"),
                ),
                (
                    "device_modified",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Device modified"
                    ),
                ),
                (
                    "locale_created",
                    models.CharField(
                        blank=True,
                        help_text="Auto-updated by Modeladmin",
                        max_length=10,
                        null=True,
                        verbose_name="Locale created",
                    ),
                ),
                (
                    "locale_modified",
                    models.CharField(
                        blank=True,
                        help_text="Auto-updated by Modeladmin",
                        max_length=10,
                        null=True,
                        verbose_name="Locale modified",
                    ),
                ),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "legal_name",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
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
                (
                    "familiar_name",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text="Should be a name. Do NOT use MR, MRS, MISS, SIR, MADAM and other such titles. (Encryption: RSA local)",
                        max_length=71,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ensure name consists of letters only in upper case separated by single spaces",
                                regex="^(([A-Z]+ )*[A-Z]+)?$",
                            )
                        ],
                        verbose_name="By what NAME should we refer to you? (if we speak to you)",
                    ),
                ),
                (
                    "initials",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Ensure initials consist of letters only in upper case, no spaces.",
                                regex="^[A-Z]{2,3}$",
                            )
                        ],
                    ),
                ),
                ("subject_identifier", models.CharField(max_length=50)),
                (
                    "subject_identifier_as_pk",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "subject_identifier_aka",
                    models.CharField(
                        editable=False,
                        help_text="track a previously allocated identifier.",
                        max_length=50,
                        null=True,
                        verbose_name="Subject Identifier a.k.a",
                    ),
                ),
                (
                    "citizen",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=3,
                        verbose_name="Is the participant a Botswana citizen? ",
                    ),
                ),
                (
                    "legal_marriage",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                        default="N/A",
                        help_text="If 'No', participant may not be consented.",
                        max_length=3,
                        null=True,
                        verbose_name="If not a citizen, is the participant legally married to a Botswana citizen?",
                    ),
                ),
                (
                    "marriage_certificate",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                        default="N/A",
                        help_text="If 'No', participant may not be consented.",
                        max_length=3,
                        null=True,
                        verbose_name="[Interviewer] Has the participant produced the marriage certificate as proof? ",
                    ),
                ),
                (
                    "marriage_certificate_no",
                    models.CharField(
                        blank=True,
                        help_text="e.g. 000/YYYY",
                        max_length=9,
                        null=True,
                        verbose_name="What is the marriage certificate number?",
                    ),
                ),
                (
                    "identity",
                    django_crypto_fields.fields.identity_field.IdentityField(
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        verbose_name="Identity number",
                    ),
                ),
                (
                    "identity_type",
                    models.CharField(
                        choices=[
                            ("country_id", "Country ID number"),
                            ("drivers", "Driver's license"),
                            ("passport", "Passport"),
                            ("hospital_no", "Hospital number"),
                            ("country_id_rcpt", "Country ID receipt"),
                            ("mobile_no", "Mobile number"),
                            ("OTHER", "Other"),
                        ],
                        max_length=25,
                        verbose_name="What type of identity number is this?",
                    ),
                ),
                (
                    "confirm_identity",
                    django_crypto_fields.fields.identity_field.IdentityField(
                        help_text="Retype the identity number (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                    ),
                ),
                ("dob", models.DateField(null=True, verbose_name="Date of birth")),
                (
                    "is_dob_estimated",
                    edc_model_fields.fields.date_estimated.IsDateEstimatedField(
                        choices=[
                            ("-", "No"),
                            ("D", "Yes, estimated the Day"),
                            ("MD", "Yes, estimated Month and Day"),
                            ("YMD", "Yes, estimated Year, Month and Day"),
                        ],
                        help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                        max_length=25,
                        null=True,
                        verbose_name="Is date of birth estimated?",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("U", "Undetermined")],
                        max_length=1,
                        null=True,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "guardian_name",
                    django_crypto_fields.fields.lastname_field.LastnameField(
                        blank=True,
                        help_text="Required only if participant is a minor.<BR>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_consent.validators.FullNameValidator()],
                        verbose_name="Guardian's last and first name",
                    ),
                ),
                ("subject_type", models.CharField(max_length=25)),
                (
                    "consent_reviewed",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="If no, participant is not eligible.",
                        max_length=3,
                        null=True,
                        validators=[edc_consent.validators.eligible_if_yes],
                        verbose_name="I have reviewed the consent with the participant",
                    ),
                ),
                (
                    "study_questions",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="If no, participant is not eligible.",
                        max_length=3,
                        null=True,
                        validators=[edc_consent.validators.eligible_if_yes],
                        verbose_name="I have answered all questions the participant had about the study",
                    ),
                ),
                (
                    "assessment_score",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="If no, participant is not eligible.",
                        max_length=3,
                        null=True,
                        validators=[edc_consent.validators.eligible_if_yes],
                        verbose_name="I have asked the participant questions about this study and the participant has demonstrated understanding",
                    ),
                ),
                (
                    "consent_signature",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="If no, participant is not eligible.",
                        max_length=3,
                        null=True,
                        validators=[edc_consent.validators.eligible_if_yes],
                        verbose_name="I have verified that the participant has signed the consent form",
                    ),
                ),
                (
                    "consent_copy",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("Declined", "Yes, but subject declined copy"),
                        ],
                        help_text="If declined, return copy with the consent",
                        max_length=20,
                        null=True,
                        validators=[edc_consent.validators.eligible_if_yes_or_declined],
                        verbose_name="I have provided the participant with a copy of their signed informed consent",
                    ),
                ),
                (
                    "may_store_genetic_samples",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Does the participant agree that a portion of the blood sample that is taken be stored for genetic analysis?",
                    ),
                ),
                (
                    "may_store_samples",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=3,
                        verbose_name="Does the participant agree to have samples stored after the study has ended",
                    ),
                ),
                ("is_verified", models.BooleanField(default=False, editable=False)),
                ("is_verified_datetime", models.DateTimeField(editable=False, null=True)),
                ("verified_by", models.CharField(editable=False, max_length=25, null=True)),
                (
                    "is_incarcerated",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="( if 'Yes' STOP participant cannot be consented )",
                        max_length=3,
                        null=True,
                        validators=[edc_consent.validators.eligible_if_no],
                        verbose_name="Is the participant under involuntary incarceration?",
                    ),
                ),
                (
                    "is_literate",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="If 'No' provide witness's name on this form and signature on the paper document.",
                        max_length=3,
                        verbose_name="Is the participant literate?",
                    ),
                ),
                (
                    "witness_name",
                    django_crypto_fields.fields.lastname_field.LastnameField(
                        blank=True,
                        help_text="Required only if participant is illiterate.<br>Format is 'LASTNAME, FIRSTNAME'. All uppercase separated by a comma. (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_consent.validators.FullNameValidator()],
                        verbose_name="Witness's last and first name",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("sw", "Swahili"),
                            ("en-gb", "British English"),
                            ("en", "English"),
                            ("mas", "Maasai"),
                            ("ry", "Runyakitara"),
                            ("lg", "Ganda"),
                            ("rny", "Runyankore"),
                        ],
                        help_text="The language used for the consent process will also be used during data collection.",
                        max_length=25,
                        verbose_name="Language of consent",
                    ),
                ),
                (
                    "version",
                    models.CharField(
                        editable=False,
                        help_text="See 'Consent Type' for consent versions by period.",
                        max_length=10,
                        verbose_name="Consent version",
                    ),
                ),
                ("updates_versions", models.BooleanField(default=False)),
                (
                    "model_name",
                    models.CharField(
                        editable=False,
                        help_text="label_lower of this model class. Will be different if instance has been added/edited via a proxy model",
                        max_length=50,
                        null=True,
                        verbose_name="model",
                    ),
                ),
                (
                    "consent_datetime",
                    models.DateTimeField(
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Consent date and time",
                    ),
                ),
                ("report_datetime", models.DateTimeField(editable=False, null=True)),
                (
                    "sid",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Used for randomization against a prepared rando-list.",
                        max_length=15,
                        null=True,
                        verbose_name="SID",
                    ),
                ),
                (
                    "comment",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=250,
                        null=True,
                        verbose_name="Comment",
                    ),
                ),
                (
                    "dm_comment",
                    models.CharField(
                        editable=False,
                        help_text="see also edc.data manager.",
                        max_length=150,
                        null=True,
                        verbose_name="Data Management comment",
                    ),
                ),
                (
                    "consent_identifier",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="A unique identifier for this consent instance",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        db_index=True,
                        default="",
                        editable=False,
                        help_text="a field used for quick search",
                        max_length=250,
                        null=True,
                    ),
                ),
                (
                    "screening_identifier",
                    models.CharField(
                        db_index=True,
                        max_length=50,
                        validators=[django.core.validators.RegexValidator("^[A-Z0-9]+$")],
                        verbose_name="Screening identifier",
                    ),
                ),
                (
                    "screening_datetime",
                    models.DateTimeField(
                        editable=False, null=True, verbose_name="Screening datetime"
                    ),
                ),
                ("group_identifier", models.CharField(max_length=50, null=True)),
                (
                    "ethnicity",
                    models.CharField(
                        default="black",
                        editable=False,
                        help_text="fromm screening",
                        max_length=15,
                        null=True,
                    ),
                ),
                (
                    "completed_by_next_of_kin",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        editable=False,
                        max_length=10,
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Subject Consent (Tanzania)",
                "verbose_name_plural": "historical Subject Consents (Tanzania)",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
