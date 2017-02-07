from pygranule.orbital_granule_filter import OrbitalGranuleFilter
from datetime import datetime
from datetime import timedelta


class Obs(object):
    def __init__(self):
        pass


class SatObs(Obs):
    def __init__(self):
        self.output_filenames = None
        self.filename_pattern = None
        self.granule_config = None
        self.area_of_interest = None
        self.granule_filter = None
        self.sat_name = None
        self.instrument_name = None
        self.time_step = None
        self.time_step_offset = None
        self.start_time = None
        self.end_time = None

    def find_matches(self, timestamp):
        if self.output_filenames is None:
            self.output_filenames = self.generate_match_list(self)

    def generate_match_list(self, granule_filter):
        if self.granule_config is None:
            self.granule_config = self.make_granule_config()
        if self.granule_filter is None:
            self.granule_filter = self.make_orbital_granule_filter()

    def make_granule_config(self):
        config = {'config_name': "DummySatData",
                  'sat_name': "NOAA 19",
                  'instrument': "AVHRR",
                  'protocol': "sftp",
                  'server': "sat@localhost",
                  'file_source_pattern': "avhrr_%Y%m%d_%H%M00_noaa19.hrp.bz2",
                  'granule_duration': "00:02:00",
                  'area_of_interest': "(0.0,73.0),(0.0,61.0),(-30.0,61.0)"}
        self.granule_config = config
        return config

    def make_orbital_granule_filter(self):
        granule_filter = OrbitalGranuleFilter(self.granule_config)
        # override orbital_layer with a particular TLE orbital element.
        granule_filter.orbital_layer.set_tle("1 29499U 06044A   11254.96536486  .00000092  00000-0  62081-4 0  5221",
                                      "2 29499  98.6804 312.6735 0001758 111.9178 248.2152 14.21501774254058")
        # generate some filenames
        self.output_filenames = []
        self.start_time = datetime(2014, 2, 25, 13, 30)
        self.end_time = datetime(2014, 2, 25, 13, 35)
        self.time_step = timedelta(minutes=2.0)
        t = self.start_time
        while t <= self.end_time:
            self.output_filenames += granule_filter.source_file_name_parser.filenames_from_time(t)
            t = t + self.time_step
        self.granule_filter = granule_filter
        self.granule_filter(self.output_filenames).show()

        return granule_filter
