#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:35:50 2022

@author: ee19b2s
"""
import numpy as np
wkdir = '/nfs/mary/Users/ee19b2s'

deglg = dict(
   global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/deglg/atmos/deglg.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/deglg/atmos/deglg.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]
)

deglh = dict(
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/deglh/atmos/deglh.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/deglh/atmos/deglh.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]
)

degli = dict(
   
)

deglj = dict(
)


tejen = dict(
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/tejen/atmos/tejen.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/tejen/atmos/tejen.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]
)

#tejeo = dict(
    #global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/tejeo/atmos/tejeo.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/HADCM3/tejeo/atmos/tejeo.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))-273.15
#)

famous = dict(
    global_3D_sst10=np.ma.masked_array(np.load('/nfs/annie/earpal/database/experiments/famous_02_deglac/atmos/famous_02_deglac.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load('/nfs/annie/earpal/database/experiments/famous_02_deglac/atmos/famous_02_deglac.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]

)

loveclim = dict(
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/LOVECLIM/atmos/loveclim.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/LOVECLIM/atmos/loveclim.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))
)

iloveclim = dict(
    
 global_3D_sst10=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/atmos/iloveclim.global_3D.temp_mm_dpth_5.010yr.npy')
)

iloveclim_fwf = dict(
    
 global_3D_sst10=np.ma.masked_array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/FWF/ocean/iloveclim_fwf.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/FWF/ocean/iloveclim_fwf.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))
)

iloveclim_uniform = dict(
    
 global_3D_sst10=np.ma.masked_array(data=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/uniform/ocean/iloveclim_uniform.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/ICE-6G_C/uniform/ocean/iloveclim_uniform.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))
)

iloveclim_fwf_glac = dict(
    
 global_3D_sst10=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/GLAC_1D/FWF/ocean/iloveclim_fwf_glac.global_3D.temp_mm_dpth_5.010yr.npy2')
    #,mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/GLAC_1D/FWF/ocean/iloveclim_fwf_glac.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))
)

iloveclim_uniform_glac = dict(
    
 global_3D_sst10=np.load(wkdir + '/work/data/pmip_proj_hs1/iLOVECLIM/GLAC_1D/uniform/ocean/iloveclim_uniform_glac.global_3D.temp_mm_dpth_5.010yr.npy2')
)

trace = dict(
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/TRACE/atmos/trace.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/TRACE/atmos/trace.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]
)

itrace = dict(
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/iTRACE/atmos/itrace.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/iTRACE/atmos/itrace.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]
)

miroc = dict(
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MIROC/ocean/miroc.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MIROC/ocean/miroc.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))
)

#mpi08 = dict(
    #global_3D_sst100=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0208/atmos/pmu0208.global_3D.temp_mm_dpth_5.100yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0208/atmos/pmu0208.global_3D.temp_mm_dpth_5.100yr.npy-mask.npy'))-273.15
#)

mpi10 = dict(
    #global_3D_sst100=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0210/atmos/pmu0210.global_3D.temp_mm_dpth_5.100yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0210/atmos/pmu0210.global_3D.temp_mm_dpth_5.100yr.npy-mask.npy'))[:,0,:,:]
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0210/ocean/pmu0210.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0210/ocean/pmu0210.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]
)


mpi11 = dict(
    #global_3D_sst100=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0211/atmos/pmu0211.global_3D.temp_mm_dpth_5.100yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0211/atmos/pmu0211.global_3D.temp_mm_dpth_5.100yr.npy-mask.npy'))[:,0,:,:]
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0211/ocean/pmu0211.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0211/ocean/pmu0211.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]
)

mpi12 = dict(
    global_3D_sst10=np.ma.masked_array(np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0212/ocean/pmu0212.global_3D.temp_mm_dpth_5.010yr.npy'), mask=np.load(wkdir + '/work/data/pmip_proj_hs1/MPI-ESM-CR/pmu0212/ocean/pmu0212.global_3D.temp_mm_dpth_5.010yr.npy-mask.npy'))[:,0,:,:]

)

uvic_short = dict(  
    global_3D_sst10=np.load(wkdir + '/work/data/pmip_proj_hs1/UVic/shorthosing/uvic_short.global_3D.temp_mm_dpth_5.100yr.npy')
)

uvic_long = dict(  
    global_3D_sst10=np.load(wkdir + '/work/data/pmip_proj_hs1/UVic/longhosing/uvic_long.global_3D.temp_mm_dpth_5.100yr.npy')
)