from geography.models import DivisionLevel


class Attributes(object):
    def set_attributes(self):
        self.STATE_LEVEL = DivisionLevel.objects.get(name=DivisionLevel.STATE)
        self.COUNTY_LEVEL = DivisionLevel.objects.get(
            name=DivisionLevel.COUNTY
        )
        self.DISTRICT_LEVEL = DivisionLevel.objects.get(
            name=DivisionLevel.DISTRICT
        )
