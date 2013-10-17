#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Python-implementation av Robin Linderborgs
PHP-bibliotek för SL:s realtidsdata:
https://github.com/Albuzz/trafiklab

Pythonifierad av Anders Ekbom (@dsrg). 
För Python 2.7.

Kräver Request för HTTP-anropen, 
se http://www.python-requests.org/en/latest/user/install/ för detaljer.

"""

import urllib       # Replaces PHP rawurlencode

import requests     # Curl replacement for Python, see python-requests.org

class PySL(object):
    def __init__(self, key):
        """ Contains users own API key """
        self.key = "key=" + str(key)
        """ Contains host """
        self.host = 'https://api.trafiklab.se/sl/'
        """ Contains one of the four APIs """
        self.api = None

    def set_api(self,api):
        """ Set API """
        api = api.lower()
        if(api=='realtid'):
            self.api = 'realtid/'
        elif(api=='trafiklaget'):
            self.api = 'trafikenjustnu/'
        elif(api=='storningsinfo'):
            self.api = 'storningsinfo/'
        elif(api=='reseplanerare'):
            self.api = 'reseplanerare'
        else:
            print 'No such API.'
      
    
    def _method(self, method, params, format=None):
        """ Generic function for methods """
        if (format != None):
          if format.lower() == 'json':
            return self._build_query(method, params, 'json');
          elif format.lower() == 'xml':
            return self._build_query(method, params, 'xml');
          else:
            print 'Invalid format'
        else:
            return self._build_query(method, params);

      
    """ Methods for the Realtid API """
    def get_site(self, stationSearch, format=None):
        params = '?stationSearch=' + urllib.quote(stationSearch) + '&'
        return self._method('GetSite', params, format)

    def get_departures(self, siteId, format=None):
        params = '?siteId=' + urllib.quote(str(siteId)) + '&'
        return self._method('GetDepartures', params, format)

    def get_dps_departures(self, siteId, timeWindow=None, format=None):
        if (timeWindow != None):
          params = '?siteId=' + urllib.quote(str(siteId)) + '&timeWindow=' + timeWindow + '&'
        else:
          params = '?siteId=' + urllib.quote(str(siteId)) + '&'
        return self._method('GetDpsDepartures', params, format)


    """ Methods for the Trafikläget API """
    def trafiken_just_nu(self, format=None):
        params = '?'
        return self._method('14448', params, format)

      
    """ Methods for the Störningsinformation API """
    def get_all_deviations(self, format=None):
        params = '?'
        return self._method('GetAllDeviations', params, format)

    def get_all_deviations_raw_data(self, format=None):
        params = '?'
        return self._method('GetAllDeviationsRawData', params, format)
      
    def get_deviations(self, fDate, tDate, mode=None, format=None):
        if (mode!=None):
          params = '?transportMode=' + mode + '&fromDate=' + fDate + '&toDate=' + tDate + '&'
        else:
          params = '?fromDate=' + fDate + '&toDate=' + tDate + '&'
        return self._method('GetDeviations', params, format)
      
    def get_deviations_raw_data(self, fDate, tDate, mode=None, format=None):
        if (mode!=None):
          params = '?transportMode=' + mode + '&fromDate=' + fDate + '&toDate=' + tDate + '&'
        else:
          params = '?fromDate=' + fDate + '&toDate=' + tDate + '&'
        return self._method('GetDeviationsRawData', params, format)
      

    """ Methods for the Reseplanerare API """
    def reseplanerare(self, format=None, **params):
        valid_params = ['S', 'SID', 
                        'Z', 'ZID', 
                        'V1', 'Date', 
                        'Time', 'Timesel', 
                        'Lang']
        paramstr = '?'
        
        for key in params:
          if key not in valid_params:
            print key + ' is not a valid parameter.'
            break
          paramstr += '&' + key + '=' + urllib.quote(params[key])
        
        paramstr += '&'
        
        return self._method('', paramstr, format)
      

    """ Build query and make Request """
    def _build_query(self, method, params, format='json'):
        url = self.host + self.api + method + '.' + format + params + str(self.key)
        r = requests.get(url)
        return r.text
