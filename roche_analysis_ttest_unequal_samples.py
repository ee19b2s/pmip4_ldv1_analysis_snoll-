import cartopy

import iris
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import numpy as np
import pandas as pd
import os

import math

import sys
sys.path.insert(0,'/nfs/mary/Users/ee19b2s/work/chapter1/hs1_pmip_proj/classes/')
from simulations import simulation
import models
import simulation_dictionary as sdict
from simulation_dictionary import tejen, tejeo, deglg, deglh, degli, deglj, loveclim, iloveclim, iloveclim_fwf, iloveclim_uniform, iloveclim_fwf_glac, iloveclim_uniform_glac, itrace, trace, famous, miroc, mpi08, mpi10, mpi11, mpi12
import variable_dictionary as vdict
sys.path.insert(0,'/nfs/mary/Users/ee19b2s/work/chapter1/hs1_pmip_proj/modules/')
import hadcm3_functions as hf
import loveclim_functions as lf
import itrace_functions as itf
import iloveclim_functions as ilf
from functions_for_comparisons import calc_anom_from_lgm, lapse_rate_correct, calc_change_between_timesteps, find_lgm_control, split_run, split_run_by_index
from sklearn import linear_model
expts = [tejen, loveclim, itrace, trace, deglg, mpi10, iloveclim_uniform, iloveclim_uniform_glac, deglh, mpi11, mpi12, iloveclim_fwf, iloveclim_fwf_glac, famous, miroc]

import scipy.stats as stats



## define file names for each simulation

variable = vdict.temp_mm_1_5m
if_precip = False
is_absolute = False

fn_tejen = os.path.join(sdict.tejen['path2expt'], variable['var_type'], sdict.tejen['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')

fn_deglg = os.path.join(sdict.deglg['path2expt'], variable['var_type'], sdict.deglg['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
fn_deglh = os.path.join(sdict.deglh['path2expt'], variable['var_type'], sdict.deglh['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
fn_famous = os.path.join(sdict.famous['path2expt'], 'monthly', sdict.famous['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')

fn_loveclim = os.path.join(sdict.loveclim['path2expt'], variable['var_type'], sdict.loveclim['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
#fn_iloveclim = os.path.join(sdict.iloveclim['path2expt'], variable['var_type'], sdict.iloveclim['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
fn_iloveclim_fwf = os.path.join(sdict.iloveclim_fwf['path2expt'], variable['var_type'], sdict.iloveclim_fwf['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
fn_iloveclim_uni = os.path.join(sdict.iloveclim_uniform['path2expt'], variable['var_type'], sdict.iloveclim_uniform['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
fn_iloveclim_fwf_glac = os.path.join(sdict.iloveclim_fwf_glac['path2expt'], variable['var_type'],sdict.iloveclim_fwf_glac['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
fn_iloveclim_uni_glac = os.path.join(sdict.iloveclim_uniform_glac['path2expt'], variable['var_type'], sdict.iloveclim_uniform_glac['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')

fn_itrace = os.path.join(sdict.itrace['path2expt'], variable['var_type'], sdict.itrace['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')

fn_trace = os.path.join(sdict.trace['path2expt'], variable['var_type'], sdict.trace['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')

fn_miroc = os.path.join(sdict.miroc['path2expt'], variable['var_type'], sdict.miroc['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')

fn_mpi10 = os.path.join(sdict.mpi10['path2expt'], variable['var_type'], sdict.mpi10['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
fn_mpi11 = os.path.join(sdict.mpi11['path2expt'], variable['var_type'], sdict.mpi11['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')
fn_mpi12 = os.path.join(sdict.mpi12['path2expt'], variable['var_type'], sdict.mpi12['expt_name'] + '.' + variable['var_name'] + '.annual.nc-1deg')


## read cube of each simulation and convert to numpy array 
location=None
tejen_data, _, _, _, _ = hf.read_cube(fn_tejen, location=location, return_time=False, return_lat=False, return_lon=False)
deglg_data, _, lat_had, lon_had, _ = hf.read_cube(fn_deglg, location=location, return_time=False)
deglh_data, _, _, _, _ = hf.read_cube(fn_deglh, location=location, return_time=False, return_lat=False, return_lon=False)
famous_data, _, lat_famous, lon_famous, _ = lf.read_cube(fn_famous, location=location, return_time=False)
loveclim_data,_,lat_loveclim,lon_loveclim, _ = lf.read_cube(fn_loveclim, location=location, return_time=False)
iloveclim_data,_,lat_ilove,lon_ilove = lf.read_cube(fn_iloveclim, location=location, return_time=False)
iloveclim_fwf_data,_,lat_ilove,lon_ilove, _ = lf.read_cube(fn_iloveclim_fwf, location=location, return_time=False)
iloveclim_uni_data,_,lat_ilove,lon_ilove, _ = lf.read_cube(fn_iloveclim_uni, location=location, return_time=False)
iloveclim_fwf_glac_data,_,lat_ilove,lon_ilove, _ = lf.read_cube(fn_iloveclim_fwf_glac, location=location, return_time=False)
iloveclim_uni_glac_data,_,lat_ilove,lon_ilove, _ = lf.read_cube(fn_iloveclim_uni_glac, location=location, return_time=False)
itrace_data, _, lat_itrace, lon_itrace, _ = lf.read_cube(fn_itrace, location=location, return_time=False)
trace_data, _, lat_trace, lon_trace, _ = lf.read_cube(fn_trace, location=location, return_time=False)
miroc_data, _, lat_miroc, lon_miroc, _ = lf.read_cube(fn_miroc, location=location, return_time=False)
mpi10_data, _, _, _, _ = lf.read_cube(fn_mpi10, location=location, return_time=False, return_lat=False, return_lon=False)
mpi11_data, _, _, _, _ = lf.read_cube(fn_mpi11, location=location, return_time=False, return_lat=False, return_lon=False)
mpi12_data, _, _, _, _ = lf.read_cube(fn_mpi12, location=location, return_time=False, return_lat=False, return_lon=False)


## make list of all simulations that you want to run the linear regression for 

expts = [mpi11,mpi12] #tejen,itrace,deglg,deglh,famous,loveclim,iloveclim_fwf,iloveclim_uniform,iloveclim_fwf_glac, iloveclim_uniform_glac,trace,miroc,mpi10,
expts_data = [mpi11_data,mpi12_data] #tejen_data,itrace_data,deglg_data,deglh_data,famous_data,loveclim_data,iloveclim_fwf_data,iloveclim_uni_data,iloveclim_fwf_glac_data,iloveclim_uni_glac_data,trace_data,miroc_data,mpi10_data,


lon = np.load('/nfs/annie/ee19b2s/work/data/pmip_proj_hs1/1degree_lon.npy')
lat = np.load('/nfs/annie/ee19b2s/work/data/pmip_proj_hs1/1degree_lat.npy')

alpha = 0.01


## split numpy array for each simulation into 100 yr samples (split_run_by_index function creates a list of 100 yr samples)
expts_lgm = []
expts_samples = []
lgm_def = 21
start_time = 20.5
end_time = 13
for expt,data in zip(expts, expts_data):
    expts_lgm.append(find_lgm_control(data,expt['time1'],timestep='annual',sample_time=500,lgm_def=lgm_def))
    expts_samples.append(split_run_by_index(data,expt['time1'],sample_time=100,lgm_def=start_time,end_time=end_time))
        

## for each simulation, run through each 100 yr sample and take a one-sided student t-test at each grid point to test if significantly warmer than control
for sim in range(len(expts)):
    expt = expts_samples[sim]
    lgm = expts_lgm[sim]
    p_values = []
    for sample in expt:
        out = np.zeros((lgm.shape[1], lgm.shape[2]))
        for i in range(lgm.shape[1]):
            for j in range(lgm.shape[2]):
                control = lgm[:,i,j]
                test = sample[:,i,j]
                ## check if variances are similar enough using F-test
                control_var = np.var(control)
                test_var = np.var(test)
                
                F = test_var/control_var
                p_value_test_var = stats.f.cdf(F, len(test)-1, len(control)-1)
                ## if not similar enough than run t-test with equal_var=False, otherwise with equal_var=True
                if p_value_test_var > 0.05:
                    t,p = stats.ttest_ind(test,control, equal_var=False, alternative='greater', random_state=42)
                else:
                    t,p = stats.ttest_ind(test,control, equal_var=True, alternative='greater', random_state=42)
                ## put p-value for each grid point in new array
                out[i,j]=p
        p_values.append(out)
   
        
    time = expts[sim]['time1'][hf.find_nearest_value(expts[sim]['time1'],start_time):hf.find_nearest_value(expts[sim]['time1'],end_time)]
    out_times = np.zeros((p_values[0].shape[0], p_values[0].shape[1]))
       
    ## loop through new array for each sample and see if p-value is statistically significant, if significant than the year of that sample is added to a new array for each grid point 
    for x in range(len(p_values)):
        for i in range(p_values[0].shape[0]):
            for j in range(p_values[0].shape[1]):
                if out_times[i,j] == 0:
                    if p_values[x][i,j] <= alpha:
                        out_times[i,j] = time[x*100]-0.05
                    else:
                        pass
                else:
                    pass

    for i in range(p_values[0].shape[0]):
            for j in range(p_values[0].shape[1]):
                if out_times[i,j] == 0:
                    out_times[i,j] = np.nan
    
    
 
    np.save('/nfs/mary/Users/ee19b2s/work/data/pmip_proj_hs1/roche_analysis_new_for_review/' + expts[sim]['expt_name'] + '.roche_analysis_ttest_greater_SAT_99conf_500yr_earlyLGM.100yr.npy',out_times.data)
    print('saved ' + expts[sim]['expt_name'])
    
print('DONE')
