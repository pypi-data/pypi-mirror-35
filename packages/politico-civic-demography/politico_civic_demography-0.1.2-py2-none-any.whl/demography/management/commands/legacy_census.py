import json
import os
import statistics
import pprint

from tqdm import tqdm

import boto3
from census import Census

from demography.models import CensusEstimate, CensusTable, CensusVariable
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from geography.models import Division, DivisionLevel

census = Census(settings.CENSUS_API_KEY)

OUTPUT_PATH = os.path.join(settings.AWS_S3_UPLOAD_ROOT, "data/us-census")


def get_bucket():
    session = boto3.session.Session(
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    s3 = session.resource("s3")
    return s3.Bucket(settings.AWS_S3_BUCKET)


class Command(BaseCommand):
    help = (
        "After modeling your desired census tables and estimates in Django, "
        "this command will bootstrap estimates from the Census API and then "
        "create and upload state-level JSON files to S3."
    )

    @staticmethod
    def get_series(series):
        """
        Returns a census series API handler.
        """
        if series == "acs1":
            return census.acs1dp
        elif series == "acs5":
            return census.acs5
        elif series == "sf1":
            return census.sf1
        elif series == "sf3":
            return census.sf3
        else:
            return None

    def write_district_estimate(self, table, variable, code, datum):
        try:
            state = Division.objects.get(
                code=datum["state"], level=self.STATE_LEVEL
            )
            division = Division.objects.get(
                code=datum["congressional district"],
                level=self.DISTRICT_LEVEL,
                parent=state,
            )
            CensusEstimate.objects.update_or_create(
                division=division,
                variable=variable,
                defaults={"estimate": datum[code] or 0},
            )
        except ObjectDoesNotExist:
            print("ERROR: {}, {}".format(datum["NAME"], datum["state"]))

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
            division = Division.objects.get(
                code="{}{}".format(datum["state"], datum["county"]),
                level=self.COUNTY_LEVEL,
            )
            CensusEstimate.objects.update_or_create(
                division=division,
                variable=variable,
                defaults={"estimate": datum[code] or 0},
            )
        except ObjectDoesNotExist:
            print("ERROR: {}, {}".format(datum["NAME"], datum["state"]))

    def write_state_estimate(self, table, variable, code, datum):
        try:
            division = Division.objects.get(
                code=datum["state"], level=self.STATE_LEVEL
            )
            CensusEstimate.objects.update_or_create(
                division=division,
                variable=variable,
                defaults={"estimate": datum[code] or 0},
            )
        except ObjectDoesNotExist:
            print("ERROR: {}, {}".format(datum["NAME"], datum["state"]))

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

    def fetch_census_data(self, states):
        """
        Fetch census estimates from table.
        """
        print("Fetching census data")
        for table in CensusTable.objects.all():
            api = self.get_series(table.series)
            for variable in table.variables.all():
                estimate = "{}_{}".format(table.code, variable.code)
                print(
                    ">> Fetching {} {} {}".format(
                        table.year, table.series, estimate
                    )
                )
                for state in tqdm(states):
                    self.get_state_estimates_by_state(
                        api=api,
                        table=table,
                        variable=variable,
                        estimate=estimate,
                        state=state,
                    )
                    self.get_county_estimates_by_state(
                        api=api,
                        table=table,
                        variable=variable,
                        estimate=estimate,
                        state=state,
                    )
                    self.get_district_estimates_by_state(
                        api=api,
                        table=table,
                        variable=variable,
                        estimate=estimate,
                        state=state,
                    )

    @staticmethod
    def aggregate_variable(estimate, id):
        """
        Aggregate census table variables by a custom label.
        """
        estimates = [
            variable.estimates.get(division__id=id).estimate
            for variable in estimate.variable.label.variables.all()
        ]
        method = estimate.variable.label.aggregation
        if method == "s":
            aggregate = sum(estimates)
        elif method == "a":
            aggregate = statistics.mean(estimates)
        elif method == "m":
            aggregate = statistics.median(estimates)
        else:
            aggregate = None
        return aggregate

    def aggregate_national_estimates_by_state(self):
        """
        Aggregates state-level estimates for each table within the country.

        Creates data structure designed for an export in this format:
        ...{series}/{year}/{table}/states.json
        """
        data = {}
        fips = "00"
        aggregated_labels = []
        states = Division.objects.filter(level=self.STATE_LEVEL)
        estimates = CensusEstimate.objects.filter(
            division__level=self.STATE_LEVEL
        )
        for estimate in estimates:
            series = estimate.variable.table.series
            year = estimate.variable.table.year
            table = estimate.variable.table.code
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
                    data[series][year][table][fips][label] = [
                        self.aggregate_variable(estimate, division.id)
                        for division in states
                        if len(
                            CensusEstimate.objects.filter(
                                variable=estimate.variable,
                                division=division.id,
                            )
                        )
                        > 0
                    ]
            else:
                if code in data[series][year][table][fips]:
                    data[series][year][table][fips][code].append(
                        estimate.estimate
                    )
                else:
                    data[series][year][table][fips][code] = [estimate.estimate]
        # print(data)
        return data

    def aggregate_national_estimates_by_district(self):
        """
        Aggregates district-level estimates for each table within the country.

        Creates data structure designed for an export in this format:
        ...{series}/{year}/{table}/districts.json
        """
        data = {}
        fips = "00"
        aggregated_labels = []
        states = Division.objects.filter(level=self.DISTRICT_LEVEL)
        estimates = CensusEstimate.objects.filter(
            division__level=self.DISTRICT_LEVEL
        )
        for estimate in estimates:
            series = estimate.variable.table.series
            year = estimate.variable.table.year
            table = estimate.variable.table.code
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
                    # c= {**a, **b}
                    aggregated_labels.append(table_label)
                    data[series][year][table][fips][label] = [
                        self.aggregate_variable(estimate, division.id)
                        for division in states
                        if len(
                            CensusEstimate.objects.filter(
                                variable=estimate.variable,
                                division=division.id,
                            )
                        )
                        > 0
                    ]
            else:
                if code in data[series][year][table][fips]:
                    data[series][year][table][fips][code].append(
                        estimate.estimate
                    )
                else:
                    data[series][year][table][fips][code] = [estimate.estimate]
        # print(data)
        return data

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
        # print(data)
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

    @staticmethod
    def bake_data(bucket, division, subdivision_level, data):
        for series in data.keys():
            for year in data[series].keys():
                for table in data[series][year].keys():
                    key = os.path.join(
                        OUTPUT_PATH,
                        series,
                        year,
                        table,
                        division.code,
                        "{}.json".format(subdivision_level),
                    )
                    bucket.put_object(
                        Key=key,
                        ACL=settings.AWS_ACL,
                        Body=json.dumps(data[series][year][table]),
                        CacheControl=settings.AWS_CACHE_HEADER,
                        ContentType="application/json",
                    )

    def export_by_state(self, states):
        bucket = get_bucket()
        for fips in states:
            state = Division.objects.get(level=self.STATE_LEVEL, code=fips)
            print(">> Exporting: {}".format(state.code))
            # state_data = self.aggregate_state_estimates_by_county(state)
            # self.export_state_files(bucket, state, state_data)
            self.aggregate_state_estimates_by_district(state)

    def add_arguments(self, parser):
        parser.add_argument(
            "states", nargs="+", help="States to export by FIPS code."
        )

    def handle(self, *args, **options):
        self.STATE_LEVEL = DivisionLevel.objects.get(name=DivisionLevel.STATE)
        self.COUNTY_LEVEL = DivisionLevel.objects.get(
            name=DivisionLevel.COUNTY
        )
        self.DISTRICT_LEVEL = DivisionLevel.objects.get(
            name=DivisionLevel.DISTRICT
        )

        states = options["states"]
        self.fetch_census_data(states)

        self.aggregate_national_estimates_by_state()
        self.aggregate_national_estimates_by_district()

        self.export_by_state(states)
        print("Done.")
