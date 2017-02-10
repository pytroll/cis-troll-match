from pygranule.orbital_granule_filter import OrbitalGranuleFilter
from datetime import datetime
from datetime import timedelta


class SatObs(object):
    def __init__(self, config_dict):
        self.granule_config = config_dict
        self.output_filenames = None
        self._granule_filter = None
        self.time_step = None
        self.end_time = None
        self.start_time = None

    @property
    def tle(self):
        return self._tle

    @tle.setter
    def tle(self, tle_list):
        self._tle = tle_list

    def predict_overpass_files(self):
        if self._granule_filter is None:
            self.make_granule_filter()
        self._compute_overpass_files()
        return self.output_filenames

    def make_granule_filter(self):
        granule_filter = OrbitalGranuleFilter(self.granule_config)
        granule_filter.orbital_layer.set_tle(self._tle[0], self._tle[1])
        self._granule_filter = granule_filter

    def _compute_overpass_files(self):
        _output_filenames = []
        t = self.start_time
        while t <= self.end_time:
            _output_filenames += self._granule_filter.source_file_name_parser.filenames_from_time(t)
            t = t + self.time_step
        # get only intersecting overpasses
        output_filenames = self._granule_filter(_output_filenames).keys()
        self.output_filenames = output_filenames
