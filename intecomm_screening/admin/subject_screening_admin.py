from django.contrib import admin
from django.template.loader import render_to_string
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django.utils.html import format_html
from django.utils.translation import gettext as _
from django_audit_fields import audit_fieldset_tuple
from edc_constants.constants import YES
from edc_dashboard.url_names import url_names
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin
from edc_model_admin.history import SimpleHistoryAdmin
from edc_screening.utils import format_reasons_ineligible

from ..admin_site import intecomm_screening_admin
from ..eligibility import ScreeningEligibility
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening


@admin.register(SubjectScreening, site=intecomm_screening_admin)
class SubjectScreeningAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):

    form = SubjectScreeningForm
    list_per_page = 15
    post_url_on_delete_name = "screening_listboard_url"
    subject_listboard_url_name = "screening_listboard_url"

    additional_instructions = (
        "Patients must meet ALL of the inclusion criteria and NONE of the "
        "exclusion criteria in order to proceed to the final screening stage"
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "report_datetime",
                    "selection_method",
                    "hospital_identifier",
                    "initials",
                    "gender",
                    "age_in_years",
                    "ethnicity",
                    "qualifying_condition",
                    "staying_nearby_6",
                    "consent_ability",
                )
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "screening_identifier",
        "eligibility_status",
        "demographics",
        "reasons",
        "report_datetime",
        "user_created",
        "created",
    )

    list_filter = (
        "report_datetime",
        "gender",
        "eligible",
        "consented",
        "refused",
    )

    search_fields = (
        "screening_identifier",
        "subject_identifier",
        "hospital_identifier",
        "initials",
        "reasons_ineligible",
    )

    radio_fields = {
        "gender": admin.VERTICAL,
        "qualifying_condition": admin.VERTICAL,
        "consent_ability": admin.VERTICAL,
        "staying_nearby_6": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

    @staticmethod
    def demographics(obj=None):
        data = [
            f"{obj.get_gender_display()} {obj.age_in_years}yrs",
            f"Initials: {obj.initials.upper()}<BR>",
            f"Hospital ID: {obj.hospital_identifier}",
        ]
        if obj.repeat_glucose_opinion == YES:
            data.append(f"Contact #: {obj.contact_number or '--'}")
        return format_html("<BR>".join(data))

    def reasons(self, obj=None):
        if not obj.reasons_ineligible:
            return self.dashboard(obj)
        return format_reasons_ineligible(obj.reasons_ineligible)

    def eligibility_status(self, obj=None):
        eligibility = ScreeningEligibility(obj, update_model=False)
        screening_listboard_url = reverse(
            url_names.get(self.subject_listboard_url_name), args=(obj.screening_identifier,)
        )
        context = dict(
            title=_("Go to screening listboard"),
            url=f"{screening_listboard_url}?q={obj.screening_identifier}",
            label="Screening",
        )
        button = render_to_string("dashboard_button.html", context=context)
        return format_html(button + "<BR>" + eligibility.eligibility_status(add_urls=True))

    def dashboard(self, obj=None, label=None):
        try:
            url = reverse(
                self.get_subject_dashboard_url_name(),
                kwargs=self.get_subject_dashboard_url_kwargs(obj),
            )
        except NoReverseMatch:
            url = reverse(url_names.get("screening_listboard_url"), kwargs={})
            context = dict(
                title=_("Go to screening listboard"),
                url=f"{url}?q={obj.screening_identifier}",
                label=label,
            )
        else:
            context = dict(title=_("Go to subject dashboard"), url=url, label=label)
        return render_to_string("dashboard_button.html", context=context)
