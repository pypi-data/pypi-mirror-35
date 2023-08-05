from django.core.management.base import BaseCommand

from .bake._arguments import ArgumentsMethods
from .bake._attributes import Attributes
from .bake.aggregate import Aggregator
from .bake.export import Exporter


class Command(ArgumentsMethods, Attributes, Aggregator, Exporter, BaseCommand):
    def handle(self, *args, **options):
        self.set_attributes()

        states = options["states"]

        if "00" in states:
            self.export_nation()
        else:
            self.export_states(states)

        print("Done.")
