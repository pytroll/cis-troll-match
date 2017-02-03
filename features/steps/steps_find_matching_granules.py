from trollsched import spherical
from ctmatch import matchups

import numpy as np
import datetime

@when(u'we have a single point measurement')
def step_impl(context):

    lon = np.array([30])
    lat = np.array([60])

    point_coordinate = spherical.SCoordinate(lon, lat)

@when(u'we have an object that describes satellite observations')
def step_impl(context):
    match = matchups.SatObs()
    context.match = match

@when(u'we look for the closest overpass to the current timestamp')
def step_impl(context):
    context.timestamp = datetime.datetime.utcnow()
    context.match.find_matches(context.timestamp)

@then(u'we receive a filename')
def step_impl(context):
    assert context.match.output_filenames is not None
