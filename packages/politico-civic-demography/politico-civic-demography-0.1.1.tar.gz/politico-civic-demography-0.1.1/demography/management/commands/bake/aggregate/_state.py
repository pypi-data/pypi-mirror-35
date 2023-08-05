from tqdm import tqdm

from geography.models import Division


class AggregateState(object):
    def aggregate_state_estimates_by_county(self, parent):
        """
        Aggregates county-level estimates for each table within a given state.

        Creates data structure designed for an export in this format:
        ...{series}/{year}/{table}/{state_fips}/counties.json
        """
        data = {}
        for division in tqdm(
            Division.objects.filter(level=self.COUNTY_LEVEL, parent=parent)
        ):
            fips = division.code
            id = division.id
            aggregated_labels = []  # Keep track of already agg'ed variables
            for estimate in division.census_estimates.all():
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
                if fips not in data[series][year][table]:
                    data[series][year][table][fips] = {}
                if label is not None:
                    if table_label not in aggregated_labels:
                        aggregated_labels.append(table_label)
                        data[series][year][table][fips][
                            label
                        ] = self.aggregate_variable(estimate, id)
                else:
                    data[series][year][table][division.code][
                        code
                    ] = estimate.estimate
        return data

    def aggregate_state_estimates_by_district(self, state):
        """
        Aggregates district-level estimates for each table within a
        given state.

        Creates data structure designed for an export in this format:
        ...{series}/{year}/{table}/{state_fips}/districts.json
        """
        data = {}
        for division in tqdm(
            Division.objects.filter(level=self.DISTRICT_LEVEL, parent=state)
        ):
            fips = division.code
            id = division.id
            aggregated_labels = []  # Keep track of already agg'ed variables
            for estimate in division.census_estimates.all():
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
                if fips not in data[series][year][table]:
                    data[series][year][table][fips] = {}
                if label is not None:
                    if table_label not in aggregated_labels:
                        aggregated_labels.append(table_label)
                        data[series][year][table][fips][
                            label
                        ] = self.aggregate_variable(estimate, id)
                else:
                    data[series][year][table][division.code][
                        code
                    ] = estimate.estimate
        return data
