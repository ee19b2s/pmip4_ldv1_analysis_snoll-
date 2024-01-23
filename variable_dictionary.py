#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:22:50 2022

@author: ee19b2s
"""

ht_mm_srf = dict(
    var_name='ht_mm_srf',
    short_name='Orog',
    long_name='Orographic Height',
    var_type='',
    label='Orographic Height (m)'
    )

iceconc_mm_srf = dict(
    var_name='iceconc_mm_srf',
    short_name='SIC',
    long_name= 'sea ice concentration',
    var_type='atmos',
    hr_timestep='monthly',
    lr_timestep='annual',
    cr_timestep='010yr',
    cmap='RdBu',
    label='SIC (%)',
    anom_vmin=-1,
    anom_vmax=1,
    abs_vmin=0,
    abs_vmax=1
    )

mixLyrDpth = dict(
    var_name='mixLyrDpth',
    short_name='MLD',
    long_name='mix layer depth',
    var_type='ocean',
    hr_timestep='monthly',
    lr_timstep='annual',
    cr_timestep='010yr',
    cmap='PiYG',
    label='MLD (m)',
    anom_vmin=-1000,
    anom_vmax=1000,
    abs_vmin=0,
    abs_vmax=5000
    )

moc = dict(
    var_name='moc',
    short_name='MOC',
    long_name='meridional overturning circulation',
    var_type='ocean',
    hr_timestep='monthly',
    lr_timestep='annual',
    cr_timestep='010yr'
    )

merid_Atlantic_ym_dpth = dict(
    var_name='merid_Atlantic_ym_dpth',
    short_name='AMOC',
    long_name='Atlantic meridional overturning circulation',
    var_type='ocean',
    timestep_had='annual',
    timestep_mpi='100yr',
    timestep='010yr',
    label='Max NH AMOC (Sv)'
    )

merid_Global_ym_dpth = dict(
    var_name='merid_Global_ym_dpth',
    short_name='GMOC',
    long_name='Global meridional overturning circulation',
    var_type='ocean',
    timestep='monthly'
    )

p_mm_msl = dict(
    var_name='p_mm_msl',
    short_name='SLP',
    long_name= 'sea level pressure',
    var_type='atmos',
    timestep='monthly',
    label='SLP (hPa)',
    cmap='bwr'
    )
   
precip_mm_srf = dict(
     var_name='precip_mm_srf',
     short_name='precip',
     long_name='total precipitation',
     var_type='atmos',
     timestep='monthly',
     cmap='BrBG',
     label='Precip (%)',
     anom_vmin=-0.5,
     anom_vmax=0.5,
     abs_vmin=0,
     abs_vmax=20
     )

salinity_ym_dpth_5 = dict(
    var_name='salinity_ym_dpth_5',
    short_name='SSS',
    long_name='sea surface salinity',
    var_type='ocean',
    timestep='monthly'
    )

snowdepth_mm_srf = dict(
    var_name='snowdepth_mm_srf',
    short_name='snow depth',
    long_name='water equivelant snow depth',
    var_type='atmos',
    timestep='monthly'
    )
    
temp_mm_1_5m = dict(
    var_name='temp_mm_1_5m',
    short_name='SAT',
    long_name= 'surface air temperature at 2m',
    var_type='atmos',
    timestep='monthly',
    cmap='bwr',
    label = 'SAT ($^\circ$C)',
    anom_vmin=-15,
    anom_vmax=15,
    abs_vmin=-10,
    abs_vmax=5    
    )

temp_mm_dpth_5 = dict(
    var_name='temp_mm_dpth_5',
    short_name='SST',
    long_name='sea surface temperature',
    var_type='ocean',
    timestep='monthly',
    cmap='bwr',
    label = 'SST ($^\circ$C)',
    anom_vmin=-15,
    anom_vmax=15,
    abs_vmin=-10,
    abs_vmax=5    
    )

temp_ym_dpth_400 = dict(
    var_name='temp_mmtential temperature at 400m',
    long_name='sub-surface temperature at 400m',
    var_type='ocean',
    timestep='monthly',
    cmap='bwr',
    label = '400m Depth Temp ($^\circ$C)'

    )

temp_ym_dpth_666 = dict(
    var_name='temp_ym_dpth_666',
    short_name='potential temperature at 666m',
    long_name='sub-surface temperature at 666m',
    var_type='ocean',
    timestep='monthly',
    cmap='bwr',
    label = '666m Depth Temp ($^\circ$C)'

    )

ucurr_ym_dpth_5 = dict(
    var_name='ucurr_ym_dpth_5',
    short_name='zonal surface currents',
    long_name='zonal surface currents',
    var_type='ocean',
    timestep='monthly',
    cmap='PuOr'
    )

u_mm_10m = dict(
    var_name='u_mm_10m',
    short_name='zonal wind',
    long_name='zonal wind at 10m',
    var_type='atmos',
    timestep='monthly',
    cmap='PuOr',
    label='Zonal wind (m/s)',
    anom_vmin=-5,
    anom_vmax=5,
    abs_vmin=-15,
    abs_vmax=15
    )

vcurr_ym_dpth_5 = dict(
    var_name='vcurr_ym_dpth_5',
    short_name='meridional surface currents',
    long_name='meridional surface currents',
    var_type='ocean',
    timestep='monthly',
    cmap='PuOr'
    )

v_mm_10m = dict(
    var_name='v_mm_10m',
    short_name='meridional wind',
    long_name='meridional wind at 10m',
    var_type='atmos',
    timestep='monthly',
    cmap='PuOr',
    label='Meridional wind (m/s)',
    anom_vmin=-5,
    anom_vmax=5,
    abs_vmin=-15,
    abs_vmax=15
    )

    
    