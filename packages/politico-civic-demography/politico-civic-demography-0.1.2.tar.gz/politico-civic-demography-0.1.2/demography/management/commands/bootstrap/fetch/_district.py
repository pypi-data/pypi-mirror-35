from geography.models import Division


class GetDistrict(object):
    def get_district_estimates_by_state(
        self, api, table, variable, estimate, state
    ):
        """
        Calls API for all districts in a state and a given estimate.
        """
        state = Division.objects.get(level=self.STATE_LEVEL, code=state)
        district_data = api.get(
            ("NAME", estimate),
            {
                "for": "congressional district:*",
                "in": "state:{}".format(state.code),
            },
            year=int(table.year),
        )
        for datum in district_data:
            self.write_district_estimate(table, variable, estimate, datum)
