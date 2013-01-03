'''
Created on Jan 2, 2013

@author: Oberron
v0.1: first version working with the ical version = "0.6.1v"
'''


import unittest

import u_icalParser
import u_icalGen
import u_icalCompute


suite1 = u_icalParser.suite()
suite2 = u_icalGen.suite()
suite3 = u_icalCompute.suite()

suite = unittest.TestSuite()

suite.addTest(suite1)
suite.addTest(suite2)
suite.addTest(suite3)

unittest.TextTestRunner(verbosity=2).run(suite)
