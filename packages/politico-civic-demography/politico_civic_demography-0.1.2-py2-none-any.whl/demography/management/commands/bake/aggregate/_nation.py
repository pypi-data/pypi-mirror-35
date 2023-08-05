from demography.models import CensusEstimate
from geography.models import Division
from tqdm import tqdm


class AggregateNation(object):
    def aggregate_national_estimates_by_state(self):
        """
        Aggregates state-level estimates for each table within the country.

        Creates data structure designed for an export in this format:
        ...{series}/{year}/{table}/states.json
        """
        data = {}
        states = Division.objects.filter(level=self.STATE_LEVEL)
        for state in tqdm(states):
            aggregated_labels = []
            estimates = CensusEstimate.objects.filter(division=state)
            for estimate in estimates:
                series = estimate.variable.table.series
                year = estimate.variable.table.year
                table = estimate.variable.table.code

                label = None
                if estimate.variable.label:
                    label = estimate.variable.label.label
                    table_label = "{}{}".format(table, label)

                code = estimate.variable.code
                if series not in data:
                    data[series] = {}
                if year not in data[series]:
                    data[series][year] = {}
                if table not in data[series][year]:
                    data[series][year][table] = {}
                if state.code not in data[series][year][table]:
                    data[series][year][table][state.code] = {}
                if label is not None:
                    if table_label not in aggregated_labels:
                        aggregated_labels.append(table_label)
                        if (
                            len(
                                CensusEstimate.objects.filter(
                                    variable=estimate.variable,
                                    division=state.id,
                                )
                            )
                            > 0
                        ):
                            data[series][year][table][state.code][
                                label
                            ] = self.aggregate_variable(estimate, state.id)
                else:
                    data[series][year][table][state.code][
                        code
                    ] = estimate.estimate

        return data

    def aggregate_national_estimates_by_district(self):
        """
        Aggregates district-level estimates for each table within the country.

        Creates data structure designed for an export in this format:
        ...{series}/{year}/{table}/districts.json
        """
        data = {}
        states = Division.objects.filter(level=self.STATE_LEVEL)
        for state in tqdm(states):
            districts = Division.objects.filter(
                level=self.DISTRICT_LEVEL, parent=state
            )
            for district in districts:
                aggregated_labels = []
                estimates = CensusEstimate.objects.filter(division=district)
                for estimate in estimates:
                    series = estimate.variable.table.series
                    year = estimate.variable.table.year
                    table = estimate.variable.table.code

                    label = None
                    if estimate.variable.label:
                        label = estimate.variable.label.label
                        table_label = "{}{}".format(table, label)

                    code = estimate.variable.code
                    if series not in data:
                        data[series] = {}
                    if year not in data[series]:
                        data[series][year] = {}
                    if table not in data[series][year]:
                        data[series][year][table] = {}
                    if state.code not in data[series][year][table]:
                        data[series][year][table][state.code] = {}
                    if (
                        district.code
                        not in data[series][year][table][state.code]
                    ):
                        data[series][year][table][state.code][
                            district.code
                        ] = {}
                    if label is not None:
                        if table_label not in aggregated_labels:
                            aggregated_labels.append(table_label)
                            if (
                                len(
                                    CensusEstimate.objects.filter(
                                        variable=estimate.variable,
                                        division=district.id,
                                    )
                                )
                                > 0
                            ):
                                data[series][year][table][state.code][
                                    district.code
                                ][label] = self.aggregate_variable(
                                    estimate, district.id
                                )
                    else:
                        data[series][year][table][state.code][district.code][
                            code
                        ] = estimate.estimate
        return data
