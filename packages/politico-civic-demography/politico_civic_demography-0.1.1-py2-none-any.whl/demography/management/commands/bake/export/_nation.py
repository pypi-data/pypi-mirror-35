from geography.models import Division


class ExportNation(object):
    def export_nation(self):
        print(">> Exporting: Nation")
        data_by_states = self.aggregate_national_estimates_by_state()
        data_by_district = self.aggregate_national_estimates_by_district()

        self.upload_division("nation", "states", data_by_states)
        self.upload_division("nation", "districts", data_by_district)

        # states = [
        #     state.code
        #     for state in Division.objects.filter(level=self.STATE_LEVEL)
        # ]
        # self.export_states(states)
