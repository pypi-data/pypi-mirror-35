from geography.models import Division
from demography.models import CensusEstimate
from django.core.exceptions import ObjectDoesNotExist


class WriteCounty(object):
    def write_county_estimate(self, table, variable, code, datum):
        """
        Creates new estimate from a census series.

        Data has following signature from API:
        {
            'B00001_001E': '5373',
             'NAME': 'Anderson County, Texas',
             'county': '001',
             'state': '48'
        }
        """
        try:
            division = Division.objects.get(code='{}{}'.format(
                datum['state'],
                datum['county']
            ), level=self.COUNTY_LEVEL)
            CensusEstimate.objects.update_or_create(
                division=division,
                variable=variable,
                defaults={
                    'estimate': datum[code] or 0
                }
            )
        except ObjectDoesNotExist:
            print('ERROR: {}, {}'.format(datum['NAME'], datum['state']))
