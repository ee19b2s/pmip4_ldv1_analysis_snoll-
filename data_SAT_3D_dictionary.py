#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:35:50 2022

@author: ee19b2s
"""
import numpy as np
wkdir = '/nfs/mary/Users/ee19b2s'

deglg = dict(
   global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/deglg/atmos/deglg.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/deglg/atmos/deglg.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))[:,0,:,:]-273.15 
)

deglh = dict(
    global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/deglh/atmos/deglh.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/deglh/atmos/deglh.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))[:,0,:,:]-273.15
)

degli = dict(
   
)

deglj = dict(
)


tejen = dict(
    global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/tejen/atmos/tejen.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/tejen/atmos/tejen.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))[:,0,:,:]-273.15
)

tejeo = dict(
    #global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/tejeo/atmos/tejeo.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/tejeo/atmos/tejeo.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))[:,0,:,:]-273.15
)

famous = dict(
    global_3D_temp10=np.ma.masked_array(np.load('/nfs/annie/earpal/database/experiments/famous_02_deglac/atmos/famous_02_deglac.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load('/nfs/annie/earpal/database/experiments/famous_02_deglac/atmos/famous_02_deglac.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))[:,0,:,:]-273.15

)

loveclim = dict(
    global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/LOVECLIM/atmos/loveclim.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/LOVECLIM/atmos/loveclim.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))
)

iloveclim = dict(
    
 global_3D_temp10=np.ma.masked_array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/atmos/iloveclim.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/atmos/iloveclim.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))
)

iloveclim_fwf = dict(
    
 global_3D_temp10=np.ma.masked_array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/FWF/atmos/iloveclim_fwf.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/FWF/atmos/iloveclim_fwf.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))
)

iloveclim_uniform = dict(
    
 global_3D_temp10=np.ma.masked_array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/uniform/atmos/iloveclim_uniform.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/uniform/atmos/iloveclim_uniform.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))
)

iloveclim_fwf_glac = dict(   
 global_3D_temp10=np.ma.masked_array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/GLAC_1D/FWF/atmos/iloveclim_fwf_glac.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/GLAC_1D/FWF/atmos/iloveclim_fwf_glac.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))
)

iloveclim_uniform_glac = dict(
 global_3D_temp10=np.ma.masked_array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/GLAC_1D/uniform/atmos/iloveclim_uniform_glac.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/GLAC_1D/uniform/atmos/iloveclim_uniform_glac.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))
)

trace = dict(
    global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/TRACE/atmos/trace.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/TRACE/atmos/trace.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))-273.15
)

itrace = dict(
    global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/iTRACE/atmos/itrace.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iTRACE/atmos/itrace.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))-273.15
)

miroc = dict(
    global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MIROC/atmos/miroc.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MIROC/atmos/miroc.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))-273.15
)

mpi08 = dict(
    #global_3D_temp100=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0208/atmos/pmu0208.global_3D.temp_mm_1_5m.100yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0208/atmos/pmu0208.global_3D.temp_mm_1_5m.100yr.npy-mask.npy'))-273.15
)

mpi10 = dict(
    #global_3D_temp100=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0210/atmos/pmu0210.global_3D.temp_mm_1_5m.100yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0210/atmos/pmu0210.global_3D.temp_mm_1_5m.100yr.npy-mask.npy'))-273.15
   global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0210/atmos/pmu0210.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0210/atmos/pmu0210.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))-273.15
)


mpi11 = dict(
    #global_3D_temp100=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0211/atmos/pmu0211.global_3D.temp_mm_1_5m.100yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0211/atmos/pmu0211.global_3D.temp_mm_1_5m.100yr.npy-mask.npy'))-273.15
   global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0211/atmos/pmu0211.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0211/atmos/pmu0211.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))-273.15

)

mpi12 = dict(
   global_3D_temp10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0212/atmos/pmu0212.global_3D.temp_mm_1_5m.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0212/atmos/pmu0212.global_3D.temp_mm_1_5m.010yr.npy-mask.npy'))-273.15
)

uvic_short = dict(
  global_3D_temp10=np.ma.array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/UVic/shorthosing/uvic_short.temp_mm_1_5m.100yr.npy-1deg'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/UVic/shorthosing/uvic_short.temp_mm_1_5m.100yr.mask.npy-1deg'))
)

uvic_long = dict(
  global_3D_temp10=np.ma.array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/UVic/longhosing/uvic_long.temp_mm_1_5m.100yr.npy-1deg'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/UVic/longhosing/uvic_long.temp_mm_1_5m.100yr.mask.npy-1deg'))
)

