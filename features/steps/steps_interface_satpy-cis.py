from cis.parse_datetime import parse_datetimestr_delta_to_float_days
import satpy
from satpy import projectable
import numpy as np
from cis.data_io.ungridded_data import UngriddedData, Metadata
from cis.data_io.Coord import Coord
from mock import MagicMock
from cis.time_util import PartialDateTime
from copy import deepcopy

@when(u'there satpy scene is available')
def step_impl(context):
    lats = np.arange(8)
    lons = np.arange(8)
    scene = satpy.scene.Scene()
    area = MagicMock()
    area.lats = lats
    area.lons = lons

    ds = projectable.Projectable(np.arange(8),
                                 name='Name',
                                 area=area,
                                 units='Units')

    scene['ds'] = ds
    context.scene = scene

@when(u'satpy scene contains dataset')
def step_impl(context):
    assert isinstance(context.scene['ds'], projectable.Projectable)

@then(u'make CIS Ungridded dataset out of it')
def step_impl(context):

    data = context.scene['ds']
    area = data.info['area']
    units = data.info['units']

    lats = Coord(area.lats,
            Metadata(standard_name='latitude', units='degrees'),
            'y')
    lons = Coord(area.lons,
            Metadata(standard_name='longitude', units='degrees'),
            'x')
    time = Coord(np.arange(8)[::-1],
            Metadata(standard_name='time', units='days since 1970-1-1'),
            axis='t')
    ug = UngriddedData(data, Metadata(name=data.info['name'],
        units=data.info['units']), [lats, lons, time])

    context.ug = ug

@then(u'collocate ungrided dataset with itself')
def step_impl(context):
    ungrided_sample_1 = deepcopy(context.ug)
    ungrided_sample_2 = deepcopy(context.ug)
    ungrided_sample_2.coord(standard_name='time').data = np.arange(8)
    ungrided_sample_1.collocated_onto(ungrided_sample_2)
    context.ug_3 = ungrided_sample_2

@then(u'ungrided dataset with itself with 15 minutes time constraint')
def step_impl(context):
    time_interval = 'P2DT1H0M30S'
    ungrided_sample_1 = deepcopy(context.ug)
    ungrided_sample_2 = deepcopy(context.ug)
    ungrided_sample_2.coord(standard_name='time').data = np.arange(8) + 8
    context.matchup = ungrided_sample_1.collocated_onto(ungrided_sample_2, t_sep=time_interval)
    print(context.matchup[0].data.sum())
