from nose.tools import *
import pysl.pysl

lab = pysl.pysl.Trafiklab('123')

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
