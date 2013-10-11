import Trafiklab

lab = Trafiklab.Trafiklab(<API_KEY>)

lab.setAPI(self,api):

lab.method(self, method, params, format=None):

lab.getSite(self, stationSearch, format=None):

lab.getDepartures(siteId, format=None):

lab.getDpsDepartures(siteId, timeWindow=None, format=None):

lab.trafikenJustNu(self,format=None):

lab.getAllDeviations(format=None):

lab.getAllDeviationsRawData():

lab.getDeviations(fDate, tDate, mode=None, format=None):
  
lab.getDeviationsRawData(fDate, tDate, mode=None, format=None):

lab.reseplanerare(params=[], format=None):

lab.buildQuery(method, params, format):
