from geography.models import Division


class GetCounty(object):
    def get_county_estimates_by_state(
        self, api, table, variable, estimate, state
    ):
        """
        Calls API for all counties in a state and a given estimate.
        """
        state = Division.objects.get(level=self.STATE_LEVEL, code=state)
        county_data = api.get(
            ("NAME", estimate),
            {"for": "county:*", "in": "state:{}".format(state.code)},
            year=int(table.year),
        )
        for datum in county_data:
            self.write_county_estimate(table, variable, estimate, datum)
