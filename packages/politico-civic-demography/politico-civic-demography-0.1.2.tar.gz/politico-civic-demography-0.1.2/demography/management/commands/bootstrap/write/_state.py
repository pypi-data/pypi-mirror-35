from geography.models import Division
from demography.models import CensusEstimate
from django.core.exceptions import ObjectDoesNotExist


class WriteState(object):
    def write_state_estimate(self, table, variable, code, datum):
        try:
            division = Division.objects.get(
                code=datum['state'],
                level=self.STATE_LEVEL
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
