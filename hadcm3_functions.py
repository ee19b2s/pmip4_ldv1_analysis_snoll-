#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:20:49 2021

@author: ee19b2s
"""

## import all libraries 
import iris
import iris.quickplot as qplt
import iris.analysis.cartography
import iris.coord_categorisation
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.util import add_cyclic_point
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


def read_cube(filename, location = None, constrain_lat = None, constrain_lonW = None, constrain_lonE = None, return_time = True, return_lat = True, return_lon = True, return_data = True, amoc = False, return_depth = False):
    ''' Will always return 4 values: cube (np array unless return_data = False), time, latitude points, longitude points '''
    constrain_depth = iris.Constraint(depth=lambda z: 500 <= z <= 3500)    

    ## load the cube with no constraints, will have dimensions - (time, height, lat, lon)
    cont = True
    if location == None:
        cube = iris.load_cube(filename)
    
    if location == 'greenland':
        constrain_lat = iris.Constraint(latitude=lambda lat: 65 <= lat <= 82)
        #constrain_lat = iris.Constraint(latitude=lambda lat: 72 <= lat <= 75)
        constrain_lonW = 305
        constrain_lonE = 330
        #constrain_lonW = 320
        #constrain_lonE = 323
    elif location == 'greenland_summit':
        constrain_lat = iris.Constraint(latitude=lambda lat: 68 <= lat <= 75)
        constrain_lonW = 315
        constrain_lonE = 325
    elif location == 'europe':
        constrain_lat = iris.Constraint(latitude=lambda lat: 35 <= lat <= 60)
        constrain_lonW = -10
        constrain_lonE = 30
    elif location == 'NATL':
        constrain_lat = iris.Constraint(latitude=lambda lat: 35 <= lat <= 60)
        constrain_lonW = 300 #-60
        constrain_lonE = 360 #0
    elif location == 'NATLup':
        constrain_lat = iris.Constraint(latitude=lambda lat: 35 <= lat <= 90)
        constrain_lonW = -60
        constrain_lonE = 0
    elif location == 'NGRIP':
        constrain_lat = iris.Constraint(latitude=lambda lat: 74 <= lat <= 76)
        constrain_lonW = -43
        constrain_lonE = -41 #42.32°W, 75.01°N
    elif location == 'NW_pacific':
        constrain_lat = iris.Constraint(latitude=lambda lat: 20 <= lat <= 30)
        constrain_lonW = 130
        constrain_lonE = 140
    elif location == 'NH':
        constrain_lat = iris.Constraint(latitude= lambda lat: 0 <= lat <= 90)
        #constrain_depth = iris.Constraint(depth=lambda z: 790 <= z <= 1200)
    elif location == '26N':
        constrain_lat = iris.Constraint(latitude=lambda lat: 26 <= lat <= 27)
        constrain_depth = iris.Constraint(depth=lambda z: 500 <= z <= 3500)    
    elif location == 'north_america':
        constrain_lat = iris.Constraint(latitude=lambda lat: 35 <= lat <= 75)
        constrain_lonW = -140
        constrain_lonE = -60
    elif location == 'tropics':
        constrain_lat = iris.Constraint(latitude=lambda lat: -30 <= lat <= 30)
    elif location == 'tropics_short':
        constrain_lat = iris.Constraint(latitude=lambda lat: -25 <= lat <= 25)
    elif location == 'antarctica':
        constrain_lat = iris.Constraint(latitude=lambda lat: -76 <= lat <= -72)
    elif location == '60up':
        constrain_lat = iris.Constraint(latitude=lambda lat: 60 <= lat <= 90)
    elif location == '60down':
        constrain_lat = iris.Constraint(latitude=lambda lat: -90 <= lat <= -60)


    if constrain_lat == None:
        cube = iris.load_cube(filename)
    elif constrain_lat != None:
        if amoc == False:
            cube = iris.load_cube(filename, constrain_lat)
            if constrain_lonW == None and constrain_lonE == None:
                cube = cube
            elif constrain_lonW == None or constrain_lonE == None:
                print('Error: Need both upper and lower bound longitude components!')
                cont = False
            else:
                cube = cube.intersection(longitude=(constrain_lonW, constrain_lonE))
        elif amoc == True:
            cube = iris.load_cube(filename, constrain_lat & constrain_depth)
       
    if return_time is True:
        try:
            time = cube.coord('t').points
        except:
            time = cube.coord('time').points     
    else:
        time = None
        
    if return_lat is True:
        lat = cube.coord('latitude').points
    else:
        lat = None
        
    if return_lon is True:
        lon = cube.coord('longitude').points
    else:
        lon = None
    
    if return_depth is True:
        depth = cube.coord('depth').points
    else:
        depth = None
        
    if return_data is True:
        cube = cube.data
    else:
        cube = cube
        
    
        
    if cont is True:
        return cube, time, lat, lon, depth
    else:
        return 'Error','Error','Error','Error','Error'
    
    


def seasonal_means(inputDATA, constrain_lat = None, constrain_lonW = None, constrain_lonE = None):
    ''' FOR MONTHLY DATA ONLY '''
    
    if isinstance(inputDATA, str):
        inputDATA = read_cube(inputDATA, constrain_lat, constrain_lonW, constrain_lonE)
    else:
        inputDATA = inputDATA
        
    DJF = np.zeros((int(inputDATA.shape[0]/12), inputDATA.shape[2], inputDATA.shape[3]))
    MAM = np.zeros((int(inputDATA.shape[0]/12), inputDATA.shape[2], inputDATA.shape[3]))
    JJA = np.zeros((int(inputDATA.shape[0]/12), inputDATA.shape[2], inputDATA.shape[3]))
    SON = np.zeros((int(inputDATA.shape[0]/12), inputDATA.shape[2], inputDATA.shape[3]))
    

    j = 0
    for k in range(int(inputDATA.shape[0])-12):
        if k == 0:
            DJF[j,:,:] = DJF[j,:,:] + np.mean(inputDATA[k+11:(k+14)], axis = 0)
            j = j + 1        
        elif k%12 == 0:
            DJF[j,:,:] = DJF[j,:,:] + np.mean(inputDATA[k+11:(k+14)], axis = 0)
            j = j + 1        
    j = 0
    for k in range(int(inputDATA.shape[0])-12):
        if k == 3:
            MAM[j,:,:]= MAM[j,:,:] + np.mean(inputDATA[k+11:k+14], axis = 0)
            j = j + 1 
        elif (k-3)%12 == 0:
            MAM[j,:,:]= MAM[j,:,:] + np.mean(inputDATA[k+11:k+14], axis = 0)
            j = j + 1 
   
    j = 0    
    for k in range(int(inputDATA.shape[0])-12):
        if k == 6:
            JJA[j,:,:] = JJA[j,:,:] + np.mean(inputDATA[k+11:k+14], axis = 0)
            j = j + 1 
        elif (k-6)%12 == 0:
            JJA[j,:,:]= JJA[j,:,:] + np.mean(inputDATA[k+11:k+14], axis = 0)
            j = j + 1 

    j = 0        
    for k in range(int(inputDATA.shape[0])-12):
        if k == 9:
            SON[j,:,:]= SON[j,:,:] + np.mean(inputDATA[k+11:k+14], axis = 0)
            j = j + 1 
        elif (k-9)%12 == 0:
            SON[j,:,:]= SON[j,:,:] + np.mean(inputDATA[k+11:k+14], axis = 0)
            j = j + 1     ## call the function to find seasonal means for every dataset desired
    
    return DJF, MAM, JJA, SON


def weighted_avg(inputDATA, lat):
    ''' inputDATA must be array '''
    
    cont = True 
    
    latr = np.deg2rad(lat)
    
    weights = np.cos(latr)
    
    if len(inputDATA.shape) == 4:
        zonal_mean = np.average(inputDATA, axis = 3)
        outputDATA = np.average(zonal_mean, axis = 2, weights = weights)
        outputDATA = outputDATA[:,0]
    elif len(inputDATA.shape) == 3:
        zonal_mean = np.average(inputDATA, axis = 2)
        outputDATA = np.average(zonal_mean, axis = 1, weights = weights)
    elif len(inputDATA.shape) == 2:
        zonal_mean = np.average(inputDATA, axis = 1)
        outputDATA = zonal_mean
    else:
        return 'Error: This function only works with arrays of 3 or 4 axes in the format time, [z], lat, lon.'
        cont = False
    
    if cont is True:
        return outputDATA
    
    
def masked_weighted_avg(inputDATA, lat):#, value_to_mask):
    ''' inputDATA must be array '''
    
    cont = True 
    
    latr = np.deg2rad(lat)
    
    weights = np.cos(latr)
     
    if len(inputDATA.shape) == 4:
        zonal_mean = ma.average(inputDATA, axis = 3)
        outputDATA = ma.average(zonal_mean, axis = 2, weights = weights)
        outputDATA = outputDATA[:,0]
    elif len(inputDATA.shape) == 3:
        zonal_mean = ma.average(inputDATA, axis = 2)
        outputDATA = ma.average(zonal_mean, axis = 1, weights = weights)
    else:
        return 'Error: This function only works with arrays of 3 or 4 axes in the format time, [z], lat, lon.'
        cont = False
    
    if cont is True:
        return outputDATA
    

def nan_weighted_avg(inputDATA, lat):#, value_to_mask):
    ''' inputDATA must be array '''
    
    cont = True 
    
    latr = np.deg2rad(lat)
    
    weights = np.cos(latr)
    
    inputDATA = ma.masked_values(inputDATA, np.isnan(inputDATA))
    
    if len(inputDATA.shape) == 4:
        zonal_mean = ma.average(inputDATA, axis = 3)
        outputDATA = ma.average(zonal_mean, axis = 2, weights = weights)
        outputDATA = outputDATA[:,0]
    elif len(inputDATA.shape) == 3:
        zonal_mean = ma.average(inputDATA, axis = 2)
        outputDATA = ma.average(zonal_mean, axis = 1, weights = weights)
    else:
        return 'Error: This function only works with arrays of 3 or 4 axes in the format time, [z], lat, lon.'
        cont = False
    
    if cont is True:
        return outputDATA

    
    
def means_10yr_calc(inputDATA, step = 10):
    ''' accepts multi-dimensional array/list, returns 1-D list based on 1st axis '''
    
    outputDATA = []
    
    for j in range(len(inputDATA)):
        MEAN10yr = np.mean(inputDATA[j:j+step], axis = 0)
        if j%step == 0:
            outputDATA.append(MEAN10yr)
            
    outputDATA = np.array(outputDATA)

    return outputDATA

def means_10yr_calc_keep_dim(inputDATA, step = 10):
    ''' accepts multi-dimensional array/list, returns 1-D list based on 1st axis '''
    
    outputDATA = []
    
    for j in range(len(inputDATA)):
        MEAN10yr = np.mean(inputDATA[j:j+step,:,:], axis = 0)
        if j%step == 0:
            outputDATA.append(MEAN10yr)
    
    outputDATA = np.array(outputDATA)

    return outputDATA



def find_nearest_value(array, value, return_index = True):
    ''' for arrays '''
    absolute_val_array = np.abs(array - value)
    smallest_difference_index = absolute_val_array.argmin()
    closest_element = array[smallest_difference_index]
    if return_index == True:
        return smallest_difference_index
    else:
        return closest_element



def test_plot_iris(filename=None, input_cube=None):
    if input_cube == None:
        cube = iris.load_cube(filename)
    else:
        cube = input_cube
    try:
        cube = cube.collapsed('ht', iris.analysis.MEAN)
    except:
        pass
    lat = cube.coord('latitude').guess_bounds()
    lon = cube.coord('longitude').guess_bounds()
    grid_areas = iris.analysis.cartography.area_weights(cube)

    new_cube = cube.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=grid_areas)

    qplt.plot(new_cube)
    plt.show()
