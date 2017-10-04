#!/usr/bin/env python
from cis.data_io import ungridded_data
from cis.data_io.ungridded_data import UngriddedData, Metadata
from cis.data_io.Coord import Coord, CoordList
from cis.data_io.ungridded_data import UngriddedCoordinates, UngriddedData
from cis.collocation.col_implementations import nn_time, sum, mean, nn_horizontal_kdtree, nn_horizontal
from matplotlib import pyplot
import os
import glob
import datetime as dt
import matplotlib.pyplot as plt
from satpy import Scene
from datetime import datetime
from datetime import timedelta
import h5py
from netCDF4 import date2num

from pyhdf.SD import SD, SDC
import numpy as np
import argparse

from pyresample.utils import get_area_def

def load_calipso_cth(filename):
    dst = SD(filename, SDC.READ)
    data = dst.select('Layer_Top_Altitude')[:]
    lon = dst.select('Longitude')[:,0]
    lat = dst.select('Latitude')[:,0]
    time = dst.select('Profile_UTC_Time')[:,0]
    time = np.array(map(lambda x: datetime(2015,7,11) + timedelta(days=x-int(x)), time[:]))
    time = date2num(time, 'days since 2015-07-11')
    data = np.mean(np.ma.array(data, mask=data<-1), axis=1)

    lats = Coord(lat, Metadata(standard_name='latitude', units='degrees'), 'y')
    lons = Coord(lon, Metadata(standard_name='longitude', units='degrees'), 'x')
    time = Coord(time, Metadata(standard_name='time', units='days since 2015-07-11'), axis='t')
    ungridded_sample =  UngriddedData(data,
                                      Metadata(name='cth_msg', units='km'),
                                      CoordList([lats, lons, time]))

    return ungridded_sample


def load_npp_cth(filename):
    basename = os.path.basename(filename)
    basedir = os.path.dirname(filename)
    pps_filename = glob.glob(os.path.join(basedir,'..','..', 'import', 'PPS_data', 'remapped', '*_{}'.format(basename.split('_')[-1]) ))[0]
    pps_dst = h5py.File(pps_filename)
    lat = pps_dst['where']['lat']['data'][:]*0.001
    lon = pps_dst['where']['lat']['data'][:]*0.001
    cth_dst = h5py.File(filename)
    cth = cth_dst['ctth_alti'][:] * float(cth_dst['ctth_alti'].attrs[u'scale_factor']) + float(cth_dst['ctth_alti'].attrs[u'add_offset']) / 1000.
    data = cth
    lats = Coord(lat, Metadata(standard_name='latitude', units='degrees'), 'y')
    lons = Coord(lon, Metadata(standard_name='longitude', units='degrees', 'x')

    ungridded_sample = UngriddedData(data,
                                     Metadata(name='cth_npp', units='km'),
                                     CoordList([lats, lons]))
    return ungridded_sample

def load_msg_cth(filename):
    dst = h5py.File(filename, 'r')
    cth = dst['CTTH_HEIGHT']
    offset = float(cth.attrs['OFFSET'])
    sf = float(cth.attrs['SCALING_FACTOR'])
    data = (cth[:] * sf + offset)/1000.


    area_extent = (float(dst.attrs['XGEO_UP_LEFT']),
                    float(dst.attrs['YGEO_LOW_RIGHT']),
                    float(dst.attrs['XGEO_LOW_RIGHT']),
                    float(dst.attrs['YGEO_UP_LEFT']))
    proj_str = dst.attrs['PROJECTION'] + " units=km"
    ncols = data.shape[1]
    nrows = data.shape[0]
    area = get_area_def('foo', 'bar', 'moo', proj_str, ncols, nrows, area_extent)
    lon, lat = area.get_lonlats()
    date = datetime.strptime(dst.attrs['IMAGE_ACQUISITION_TIME'], '%Y%m%d%H%M')
    time = np.ones(data.shape) * date2num(date, 'days since 2015-07-11')

    lats = Coord(lat, Metadata(standard_name='latitude', units='degrees'), 'y')
    lons = Coord(lon, Metadata(standard_name='longitude', units='degrees'), 'x')
    time = Coord(time, Metadata(standard_name='time', units='days since 2015-07-11'), axis='t')
    ungridded_sample =  UngriddedData(data, Metadata(name='cth_caliop', units='km'), CoordList([lats, lons, time]))

    return ungridded_sample


def cis_compare_npp_calipso(m1, m2):
    time_interval = 'PT3M30S'
    return m1.collocated_onto(m1, t_sep=time_interval)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--input-caliop")
    p.add_argument("-m", "--input-msg")
    p.add_argument("-n", "--input-npp")
    args = p.parse_args()


    msg = load_msg_cth(args.input_msg)
    calipso = load_calipso_cth(args.input_caliop)
    npp = load_npp_cth(args.input_npp)

    lon_range = [45, 50]
    lat_range = [60, 64]
    h_sep = '1km'
    t_sep = 'PT220M'
    msg_sub = msg.subset(x=lon_range, y=lat_range)
    cal_sub = calipso.subset(x=lon_range, y=lat_range)
    res1 = cal_sub.sampled_from(msg_sub, h_sep=h_sep, t_sep=t_sep, kernel=nn_horizontal())
    cal_df = cal_sub.as_data_frame()
    res1df = res1[0].as_data_frame()

    df = cal_df.merge(res1df, right_index=True, left_index=True,
                      how='outer').reset_index()
    df.plot(kind='scatter', x='cth_caliop', y='cth_msg')
    print df.corr()
    pyplot.savefig('scatter.png')
    # import ipdb; ipdb.set_trace()

if __name__ == "__main__":
    main()
