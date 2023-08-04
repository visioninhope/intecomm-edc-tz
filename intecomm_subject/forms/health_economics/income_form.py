from django import forms
from edc_crf.modelform_mixins import CrfSingletonModelFormMixin
from edc_he.form_validators import HealthEconomicsIncomeFormValidator

from ...models import HealthEconomicsIncome
from ..mixins import CrfModelFormMixin
from .modelform_mixins import HealthEconomicsModelFormMixin


class HealthEconomicsIncomeForm(
    CrfSingletonModelFormMixin,
    HealthEconomicsModelFormMixin,
    CrfModelFormMixin,
    forms.ModelForm,
):
    form_validator_cls = HealthEconomicsIncomeFormValidator

    def clean(self):
        self.raise_if_singleton_exists()
        return super().clean()

    class Meta:
        model = HealthEconomicsIncome
        fields = "__all__"
