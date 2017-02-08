from ctmatch import matchups
from datetime import datetime
from datetime import timedelta
import numpy as np


@when(u'we have a single point measurement')
def step_impl(context):

    lon = 30
    lat = 60 
    context.aoi = "({}, {})".format(lon, lat)

@when(u'we have an object that describes satellite observations')
def step_impl(context):

    config = {'config_name': "DummySatData",
              'sat_name': "NOAA 19",
              'instrument': "AVHRR",
              'file_source_pattern': "avhrr_%Y%m%d_%H%M00_noaa19.hrp.bz2",
              'granule_duration': "00:02:00",
              'area_of_interest': "(0.0,73.0)"}

    tle1 = "1 29499U 06044A   11254.96536486  .00000092  00000-0  62081-4 0 5221"
    tle2 = "2 29499  98.6804 312.6735 0001758 111.9178 248.2152 14.21501774254058"

    match = matchups.SatObs(config)
    match.tle = [tle1, tle2]
    match.time_step = timedelta(minutes=2.0)
    match.start_time =  datetime(2014, 2, 25, 13, 30)
    match.end_time = datetime(2014, 2, 25, 13, 40) 
    context.match = match

@when(u'we look for the closest overpass to the current timestamp')
def step_impl(context):
    context.timestamp = datetime.utcnow()
    context.match.find_matches(context.timestamp)

@then(u'we receive a list of overpassing granule filenames')
def step_impl(context):
    assert isinstance(context.match.output_filenames, list) 
    assert len(context.match.output_filenames) >= 1
