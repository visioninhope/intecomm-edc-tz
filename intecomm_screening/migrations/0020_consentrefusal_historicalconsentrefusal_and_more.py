# Generated by Django 4.1.7 on 2023-04-26 12:55

import uuid

import _socket
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model_fields.fields.other_charfield
import edc_sites.models
import edc_utils.date
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("intecomm_lists", "0006_consentrefusalreasons_screeningrefusalreasons_and_more"),
        ("sites", "0002_alter_domain_unique"),
        ("intecomm_screening", "0019_healthfacility_fri_healthfacility_mon_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConsentRefusal",
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
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
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
                ("subject_identifier", models.CharField(editable=False, max_length=50)),
                ("screening_identifier", models.CharField(editable=False, max_length=50)),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow, verbose_name="Report date and time"
                    ),
                ),
                (
                    "other_reason",
                    edc_model_fields.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "reason",
                    models.ForeignKey(
                        max_length=25,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="intecomm_lists.consentrefusalreasons",
                        verbose_name="Reason for refusal to consent",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
                (
                    "subject_screening",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="intecomm_screening.subjectscreening",
                    ),
                ),
            ],
            options={
                "verbose_name": "Consent Refusal",
                "verbose_name_plural": "Consent Refusals",
            },
            managers=[
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalConsentRefusal",
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
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
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
                ("subject_identifier", models.CharField(editable=False, max_length=50)),
                ("screening_identifier", models.CharField(editable=False, max_length=50)),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow, verbose_name="Report date and time"
                    ),
                ),
                (
                    "other_reason",
                    edc_model_fields.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
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
                    "reason",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        max_length=25,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="intecomm_lists.consentrefusalreasons",
                        verbose_name="Reason for refusal to consent",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
                (
                    "subject_screening",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="intecomm_screening.subjectscreening",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Consent Refusal",
                "verbose_name_plural": "historical Consent Refusals",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(
            model_name="subjectrefusal",
            name="site",
        ),
        migrations.RemoveField(
            model_name="subjectrefusal",
            name="subject_screening",
        ),
        migrations.AddField(
            model_name="historicalpatientlog",
            name="screening_refusal_reason",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="intecomm_lists.screeningrefusalreasons",
                verbose_name="Reason subject unwilling to screen",
            ),
        ),
        migrations.AddField(
            model_name="historicalpatientlog",
            name="screening_refusal_reason_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicalpatientlog",
            name="willing_to_screen",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("tbd", "To be determined")],
                default="tbd",
                help_text="If NO, explain below",
                max_length=15,
                verbose_name="Has the patient agreed to be screened for the INTECOMM study",
            ),
        ),
        migrations.AddField(
            model_name="patientlog",
            name="screening_refusal_reason",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="intecomm_lists.screeningrefusalreasons",
                verbose_name="Reason subject unwilling to screen",
            ),
        ),
        migrations.AddField(
            model_name="patientlog",
            name="screening_refusal_reason_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="patientlog",
            name="willing_to_screen",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("tbd", "To be determined")],
                default="tbd",
                help_text="If NO, explain below",
                max_length=15,
                verbose_name="Has the patient agreed to be screened for the INTECOMM study",
            ),
        ),
        migrations.DeleteModel(
            name="HistoricalSubjectRefusal",
        ),
        migrations.DeleteModel(
            name="SubjectRefusal",
        ),
    ]
