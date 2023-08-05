from geography.models import Division


class ExportState(object):
    def export_states(self, states):
        for fips in states:
            st8 = Division.objects.get(level=self.STATE_LEVEL, code=fips)
            print(">> Exporting: {}".format(st8.code))
            data_by_county = self.aggregate_state_estimates_by_county(st8)
            data_by_district = self.aggregate_state_estimates_by_district(st8)

            self.upload_division(st8, "counties", data_by_county)
            self.upload_division(st8, "districts", data_by_district)
