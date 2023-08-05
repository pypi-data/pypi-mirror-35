from geography.models import Division


class GetState(object):
    def get_state_estimates_by_state(
        self, api, table, variable, estimate, state
    ):
        """
        Calls API for a state and a given estimate.
        """
        state = Division.objects.get(level=self.STATE_LEVEL, code=state)
        state_data = api.get(
            ("NAME", estimate),
            {"for": "state:{}".format(state.code)},
            year=int(table.year),
        )
        for datum in state_data:
            self.write_state_estimate(table, variable, estimate, datum)
