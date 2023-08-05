class ArgumentsMethods(object):
    def add_arguments(self, parser):
        parser.add_argument(
            "states", nargs="+", help="States to export by FIPS code."
        )
