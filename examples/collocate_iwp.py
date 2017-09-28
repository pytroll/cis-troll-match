#!/usr/bin/env python

#from cis.data_io.ungridded_data import UngriddedData, Metadata
#from cis.data_io.Coord import Coord
import datetime as dt
import matplotlib.pyplot as plt
from satpy import Scene
from datetime import datetime
from datetime import timedelta

from pyhdf.SD import SD, SDC
import numpy as np
import argparse


def convert_to_datetime(array):
    pass


def load_calipso_iwp(filename):
    dst = SD(filename, SDC.READ)
    data = dst.select('Ice_Water_Path')[:]
    lon = dst.select('Longitude')[:,1]
    lat = dst.select('Latitude')[:,1]
    time = dst.select('Profile_UTC_Time')[:,1]
    time = np.array(map(lambda x: datetime(2015,7,11) + timedelta(days=x-int(x)), time[:]))
    data = np.mean(data, axis=1)
    data = np.ma.array(data, mask=data<0)
    return data, lat, lon, time


def load_npp_iwp(filename):
    return data, lat, lon, time


def cis_compare_npp_calipso():
    pass


def main():
    pass

if __name__ == "__main__":
    __main__()
