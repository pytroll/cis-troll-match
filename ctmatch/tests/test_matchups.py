import mock
import unittest
from datetime import datetime
from datetime import timedelta
from ctmatch.matchups import SatObs


class TestSatObs(unittest.TestCase):
    def setUp(self):
        config = {'config_name': "DummySatData",
                  'sat_name': "NOAA 19",
                  'instrument': "AVHRR",
                  'file_source_pattern': "avhrr_%Y%m%d_%H%M00_noaa19.hrp.bz2",
                  'granule_duration': "00:02:00",
                  'area_of_interest': "(0.0, 73.0)"}

        tle1 = "1 29499U 06044A   11254.96536486  .00000092  00000-0  62081-4 0 5221"
        tle2 = "2 29499  98.6804 312.6735 0001758 111.9178 248.2152 14.21501774254058"

        match = SatObs(config)
        match.tle = [tle1, tle2]
        match.time_step = timedelta(minutes=2.0)
        match.start_time =  datetime(2014, 2, 25, 13, 30)
        match.end_time = datetime(2014, 2, 25, 13, 40) 
        self.match = match

    def tearDown(self):
        self.match = None
    
    def test_compute_overpass_files_generates_filenames(self):
        self.match.predict_overpass_files()
        self.assertTrue(self.match.output_filenames is not None) 

    def test_generate_empty_filelist_when_aoi_isnt_covered_by_satellite_trajectory(self):
        self.match.granule_config['area_of_interest'] = "(89, 0)"
        self.match.predict_overpass_files()
        self.assertTrue(self.match.output_filenames is not None)
        self.assertTrue(len(self.match.output_filenames)==0)

    def test_generate_filelist_when_aoi_match_satellite_trajectory(self):
        self.match.granule_config['area_of_interest'] = "(0.0, 73.0)"
        self.match.predict_overpass_files()
        self.assertTrue(len(self.match.output_filenames)>0)

    def test_predict_overpass_files_returns_filelist(self):
        output_filenames_list = self.match.predict_overpass_files()
        self.assertIsNotNone(output_filenames_list)
        self.assertIsInstance(output_filenames_list, list)
