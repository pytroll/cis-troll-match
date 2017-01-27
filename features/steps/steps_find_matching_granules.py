from trollsched import spherical
import numpy as np

@when(u'we have a single point measurement')
def step_impl(context):

    lon = np.array([30])
    lat = np.array([60])

    point_coordinate = spherical.SCoordinate(lon, lat)

@when(u'we look for the closest overpass to the particular timestamp')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we look for the closest overpass to the particular timestamp')

@then(u'we receive a filename')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we receive a filename')
