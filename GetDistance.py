
import math 
from math import sin, cos, sqrt, atan2, radians

import os
import pandas as pd
import numpy as np
from GPX import GPXFile

class ArrayObject:
    def __init__(self, reader, route):
        abspath = os.path.abspath(reader)
        dirname = os.path.dirname(abspath)
        os.chdir(dirname)
        files = os.listdir()
        gpx_file_path = os.path.abspath(route)
        gpxFile = GPXFile(gpx_file_path)
        gpxFile.print_info()
        gpxDF = gpxFile.get_gpx_dataframe()
        self.array = gpxDF.to_numpy()

def distance(lat1, lon1, lat2, lon2):
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    R = 6372.0
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2( sqrt(a), sqrt(1-a) )
    d = R * c
    return d

def calculatedist(point1, point2, reader, route):
    obj = ArrayObject(reader, route)
    sumdist = 0
    for i in range(point1, point2-1):
        sumdist += distance(obj.array[i][0], obj.array[i][1], obj.array[i+1][0], obj.array[i+1][1])
    return sumdist








