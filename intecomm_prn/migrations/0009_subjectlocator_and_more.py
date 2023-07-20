# Generated by Django 4.2.3 on 2023-07-19 19:52

import uuid

import _socket
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_revision.revision_field
import edc_locator.model_mixins.locator_model_mixin
import edc_model.validators.phone
import edc_sites.model_mixins
import edc_utils.date
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("edc_action_item", "0033_alter_actionitem_managers"),
        ("edc_locator", "0032_alter_subjectlocator_managers"),
        ("sites", "0002_alter_domain_unique"),
        ("intecomm_prn", "0008_alter_endofstudy_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubjectLocator",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("edc_locator.subjectlocator",),
            managers=[
                (
                    "objects",
                    edc_locator.model_mixins.locator_model_mixin.LocatorManager(),
                ),
                ("on_site", edc_sites.model_mixins.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalSubjectLocator",
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
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
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
                ("subject_identifier", models.CharField(db_index=True, max_length=50)),
                (
                    "action_identifier",
                    models.CharField(blank=True, db_index=True, max_length=50, null=True),
                ),
                (
                    "parent_action_identifier",
                    models.CharField(
                        blank=True,
                        help_text="action identifier that links to parent reference model instance.",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "related_action_identifier",
                    models.CharField(
                        blank=True,
                        help_text="action identifier that links to related reference model instance.",
                        max_length=30,
                        null=True,
                    ),
                ),
                ("action_item_reason", models.TextField(editable=False, null=True)),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "may_call",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the participant given permission <b>to contacted by telephone or cell</b> by study staff for follow-up purposes during the study?",
                    ),
                ),
                (
                    "may_visit_home",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the participant given permission for study staff <b>to make home visits</b> for follow-up purposes?",
                    ),
                ),
                (
                    "may_sms",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        null=True,
                        verbose_name="Has the participant given permission <b>to be contacted by SMS</b> by study staff for follow-up purposes during the study?",
                    ),
                ),
                (
                    "mail_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Mailing address ",
                    ),
                ),
                (
                    "physical_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Physical address with detailed description",
                    ),
                ),
                (
                    "subject_cell",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number",
                    ),
                ),
                (
                    "subject_cell_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number (alternate)",
                    ),
                ),
                (
                    "subject_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone",
                    ),
                ),
                (
                    "subject_phone_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone (alternate)",
                    ),
                ),
                (
                    "may_contact_indirectly",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        help_text="For example a partner, spouse, family member, neighbour ...",
                        max_length=25,
                        verbose_name="Has the participant given permission for study staff <b>to contact anyone else</b> for follow-up purposes during the study?",
                    ),
                ),
                (
                    "indirect_contact_name",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Full names of the contact person",
                    ),
                ),
                (
                    "indirect_contact_relation",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        verbose_name="Relationship to participant",
                    ),
                ),
                (
                    "indirect_contact_physical_address",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=500,
                        null=True,
                        verbose_name="Full physical address ",
                    ),
                ),
                (
                    "indirect_contact_cell",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number",
                    ),
                ),
                (
                    "indirect_contact_cell_alt",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Cell number (alternative)",
                    ),
                ),
                (
                    "indirect_contact_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Telephone number",
                    ),
                ),
                (
                    "may_call_work",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Has the participant given permission to be contacted <b>at work</b>, by telephone or cell, by study staff for follow-up purposes during the study?",
                    ),
                ),
                (
                    "subject_work_place",
                    django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(
                        blank=True,
                        help_text=" (Encryption: AES local)",
                        max_length=250,
                        null=True,
                        verbose_name="Name and location of work place",
                    ),
                ),
                (
                    "subject_work_phone",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.telephone_number],
                        verbose_name="Work contact telephone",
                    ),
                ),
                (
                    "subject_work_cell",
                    django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(
                        blank=True,
                        help_text=" (Encryption: RSA local)",
                        max_length=71,
                        null=True,
                        validators=[edc_model.validators.phone.cell_number],
                        verbose_name="Work contact cell number",
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(default=edc_utils.date.get_utcnow),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
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
                    "action_item",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="edc_action_item.actionitem",
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
                    "parent_action_item",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="edc_action_item.actionitem",
                    ),
                ),
                (
                    "related_action_item",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="edc_action_item.actionitem",
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
            ],
            options={
                "verbose_name": "historical subject locator",
                "verbose_name_plural": "historical subject locators",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
