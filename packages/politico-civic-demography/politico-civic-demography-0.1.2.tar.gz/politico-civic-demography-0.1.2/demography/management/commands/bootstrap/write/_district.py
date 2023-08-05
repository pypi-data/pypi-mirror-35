from geography.models import Division
from demography.models import CensusEstimate
from django.core.exceptions import ObjectDoesNotExist


class WriteDistrict(object):
    def write_district_estimate(self, table, variable, code, datum):
        try:
            state = Division.objects.get(
                code=datum['state'], level=self.STATE_LEVEL
            )
            division = Division.objects.get(
                code=datum['congressional district'],
                level=self.DISTRICT_LEVEL,
                parent=state
            )
            CensusEstimate.objects.update_or_create(
                division=division,
                variable=variable,
                defaults={
                    'estimate': datum[code] or 0
                }
            )
        except ObjectDoesNotExist:
            print('ERROR: {}, {}'.format(datum['NAME'], datum['state']))
