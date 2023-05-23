from edc_crf.model_mixins import SingletonCrfModelMixin
from edc_he.model_mixins import HouseholdHeadModelMixin, HouseholdModelMixin
from edc_model.models import BaseUuidModel

from ...model_mixins import CrfModelMixin


class HealthEconomicsHouseholdHead(
    SingletonCrfModelMixin,
    HouseholdHeadModelMixin,
    HouseholdModelMixin,
    CrfModelMixin,
    BaseUuidModel,
):
    class Meta(CrfModelMixin.Meta, BaseUuidModel.Meta):
        verbose_name = "HE Baseline: Household head"
        verbose_name_plural = "HE Baseline: Household head"
