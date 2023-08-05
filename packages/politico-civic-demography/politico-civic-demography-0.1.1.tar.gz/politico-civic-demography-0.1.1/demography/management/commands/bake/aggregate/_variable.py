import statistics


class AggregateVariable(object):
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
