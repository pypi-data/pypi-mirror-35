class GetSeries(object):
    def get_series(self, series):
        """
        Returns a census series API handler.
        """
        if series == "acs1":
            return self.census.acs1dp
        elif series == "acs5":
            return self.census.acs5
        elif series == "sf1":
            return self.census.sf1
        elif series == "sf3":
            return self.census.sf3
        else:
            return None
