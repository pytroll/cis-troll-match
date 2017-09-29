#!/usr/bin/env python

from cis.data_io.ungridded_data import UngriddedData, Metadata
from cis.data_io.Coord import Coord
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


class MatchMember(object):
    def __init__(self, data, lon, lat, time):
        self.data = data
        self.lon = lon
        self.lat = lat
        self.time = time 


def load_calipso_cth(filename):
    dst = SD(filename, SDC.READ)
    data = dst.select('Layer_Top_Altitude')[0:10]
    lon = dst.select('Longitude')[0:10,1]
    lat = dst.select('Latitude')[0:10,1]
    time = dst.select('Profile_UTC_Time')[0:10,1]
    time = np.array(map(lambda x: datetime(2015,7,11) + timedelta(days=x-int(x)), time[:]))
    time = date2num(time, 'days since 2015-07-11')
    data = np.mean(data, axis=1)
    #data  = np.ma.array(data, mask=data<0)

    lats = Coord(lat, Metadata(standard_name='latitude', units='degrees'), 'y')
    lons = Coord(lon, Metadata(standard_name='longitude', units='degrees'), 'x')
    time = Coord(time, Metadata(standard_name='time', units='days since 2015-07-11'), axis='t')
    ungridded_sample =  UngriddedData(data, Metadata(name='Caliop CTH', units='m'), [lats, lons]) 

    return MatchMember(ungridded_sample, lons, lats, time)


def load_msg_cth(filename):
    dst = h5py.File(filename, 'r')
    data = dst['CT'][:]
    area_extent = (float(dst.attrs['XGEO_UP_LEFT']),
                    float(dst.attrs['YGEO_LOW_RIGHT']),
                    float(dst.attrs['XGEO_LOW_RIGHT']),
                    float(dst.attrs['YGEO_UP_LEFT'])) 
    proj_str = dst.attrs['PROJECTION'] + " units=km"
    ncols = data.shape[1]
    nrows = data.shape[0]
    area = get_area_def('foo', 'bar', 'moo', proj_str, nrows, ncols, area_extent)
    lon, lat = area.get_lonlats()
    date = datetime.strptime(dst.attrs['IMAGE_ACQUISITION_TIME'], '%Y%m%d%H%M')
    time = np.ones(data.shape) * date2num(date, 'days since 2015-07-11')

    lats = Coord(lat, Metadata(standard_name='latitude', units='degrees'), 'y')
    lons = Coord(lon, Metadata(standard_name='longitude', units='degrees'), 'x')
    time = Coord(time, Metadata(standard_name='time', units='days since 2015-07-11'), axis='t')
    ungridded_sample =  UngriddedData(data, Metadata(name='Caliop CTH', units='m'), [lats, lons]) 

    return MatchMember(ungridded_sample, lons, lats, time)


def cis_compare_npp_calipso(m1, m2):
    time_interval = 'PT3M30S'
    import ipdb; ipdb.set_trace()
    return m1.data.collocated_onto(m2.data, t_sep=time_interval)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--input-caliop")
    p.add_argument("-m", "--input-msg")
    args = p.parse_args()

    msg = load_msg_cth(args.input_msg)
    calipso = load_calipso_cth(args.input_caliop)
    cis_compare_npp_calipso(calipso, calipso)

if __name__ == "__main__":
    main()
