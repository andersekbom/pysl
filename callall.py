#!/usr/bin/python
# -*- coding: utf-8 -*-

import pysl

pysl = pysl.PySL(<API_KEY>)

## Realtid ################################################################
pysl.set_api('realtid')
#print pysl.get_site('Slussen', 'xml')
#print pysl.get_departures(9192, 'xml')
#print pysl.get_dps_departures(9192, '60', 'xml')

## Trafikäget just nu #####################################################
pysl.set_api('trafiklaget')
#print pysl.trafiken_just_nu('xml')

## Störningsinfo ##########################################################
pysl.set_api('storningsinfo')
#print pysl.get_all_deviations('xml')
#print pysl.get_all_deviations_raw_data()
#print pysl.get_deviations('2013-10-10', '2013-10-11', 'metro', 'xml')
#print pysl.get_deviations_raw_data('2013-10-10', '2013-10-11', 'metro', 'xml')

## Reseplanerare ###########################################################
pysl.set_api('reseplanerare')
params = {'S':'Hornstull','Z':'Slussen','V1':'T-centralen'}
#print pysl.reseplanerare('xml',**params)
