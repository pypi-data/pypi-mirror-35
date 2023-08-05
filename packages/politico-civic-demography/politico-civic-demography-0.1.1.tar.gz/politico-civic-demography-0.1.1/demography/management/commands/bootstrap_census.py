from django.core.management.base import BaseCommand

from .bootstrap._arguments import ArgumentsMethods
from .bootstrap._attributes import Attributes
from .bootstrap.fetch import Fetcher
from .bootstrap.write import Writer


class Command(ArgumentsMethods, Attributes, Fetcher, Writer, BaseCommand):
    def handle(self, *args, **options):
        self.set_attributes()

        states = options["states"]

        if "00" in states:
            self.fetch_nation_data()
        else:
            self.fetch_state_data(states)

        print("Done.")
