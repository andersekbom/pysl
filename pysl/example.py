#!/usr/bin/python
# -*- coding: utf-8 -*-

import pysl
import xml.etree.ElementTree as ET

pysl = pysl.PySL('2daa2d155f306f8df04de6775da6d228')
pysl.set_api('realtid')

siteID = pysl.get_site('Hägerstensåsen','xml')
siteID = ET.XML(siteID.encode('utf-8'))
siteID = siteID[1][0][0].text
deps = pysl.get_departures(siteID,'xml')


tree = ET.XML(deps.encode('utf-8'))

print tree[3][1][4].text

print tree.find('{http://www1.sl.se/realtidws/}Metros')[1][0].text

#for atype in tree.findall('Metros'):
#  print "- ", atype.get('DisplayRow1')

