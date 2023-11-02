
import math 
from math import sin, cos, sqrt, atan2, radians

import os
import pandas as pd
import numpy as np
from GPX import GPXFile

class ArrayObject:
    reader = "GPX.py"
    route = "Asc21SantaFeTrail.gpx"
    maxenergy = ...
    eps = ...


    def __init__(self):
        abspath = os.path.abspath(ArrayObject.reader)
        dirname = os.path.dirname(abspath)
        os.chdir(dirname)
        files = os.listdir()
        gpx_file_path = os.path.abspath(ArrayObject.route)
        gpxFile = GPXFile(gpx_file_path)
        gpxFile.print_info()
        gpxDF = gpxFile.get_gpx_dataframe()
        self.array = gpxDF.to_numpy()
    

    #Calculate distance between two lat and lon points
    def distance(lat_1, lon_1, lat_2, lon_2, alt_1, alt_2):
        #dlon = lon2 - lon1
        #dlat = lat2 - lat1
       #R = 6372.0
        #a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        #c = 2 * atan2( sqrt(a), sqrt(1-a) )
        #d = R * c
        #return d
        lat_1 = lat_1 * (math.pi / 180)
        lon_1 = lon_1 *(math.pi / 180)

        lat_2 = lat_2 * (math.pi / 180)
        lon_2 = lon_2 * (math.pi / 180)

        r1 = (6376.5 * 1000) + alt_1 # Radius of Earth in metres
        r2 = (6376.5 * 1000) + alt_2

        x_1 = r1 * math.sin(lon_1) * math.cos(lat_1)
        y_1 = r1 * math.sin(lon_1) * math.sin(lat_1)
        z_1 = r1 * math.cos(lon_1)

        x_2 = r2 * math.sin(lon_2) * math.cos(lat_2)
        y_2 = r2 * math.sin(lon_2) * math.sin(lat_2)
        z_2 = r2 * math.cos(lon_2)

        dist = math.sqrt((x_2 - x_1) * (x_2 - x_1) + (y_2 - y_1) *    
                                    (y_2 - y_1) + (z_2 - z_1) * (z_2 - z_1))
        
        return dist


    #Determine change in distance between two points using points in between
    def calculatedist(point1, point2):
        obj = ArrayObject()
        sumdist = 0
        for i in range(point1, point2-1):
            sumdist += ArrayObject.distance(obj.array[i][0], obj.array[i][1], obj.array[i+1][0], obj.array[i+1][1], obj.array[i][2], obj.array[i+1][2])
        return sumdist
    
    #Find energy drain between two points using average speed over that time
    def energyDrain(point1, point2, averageSpeed):
        return (ArrayObject.calculatedist(point1, point2) * averageSpeed)/(ArrayObject.eps)
    
    #according to energy change between two points, determine max speed
    def maxSpeed(point1, point2, en1, en2):
        engchange = en1-en2
        dist = ArrayObject.calculatedist(point1, point2)
        return (dist/engchange) * ArrayObject.eps
    
    










