from edc_constants.constants import NO, TBD, YES

from .subject_screening import SubjectScreening

options = dict(
    eligible_value_default=TBD,
    eligible_values_list=[YES, NO, TBD],
    is_eligible_value=YES,
)


class ScreeningPartOne(SubjectScreening):
    def save(self, *args, **kwargs):
        if self.eligible_part_one == YES:
            self.continue_part_two = TBD
        else:
            self.continue_part_two = NO
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = "Subject Screening: Part One"
        verbose_name_plural = "Subject Screening: Part One"


class ScreeningPartTwo(SubjectScreening):
    class Meta:
        proxy = True
        verbose_name = "Subject Screening: Part Two"
        verbose_name_plural = "Subject Screening: Part Two"