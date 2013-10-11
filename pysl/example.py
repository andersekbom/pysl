#!/usr/bin/python
# -*- coding: utf-8 -*-

import pysl

pysl = pysl.PySL(<API_KEY>)

pysl.set_api('realtid')

siteID = pysl.get_site('Slussen','xml')

print siteID
