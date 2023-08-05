# -*- coding: utf-8 -*-

### imports ###################################################################
import unittest

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

class MikroCAD_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mc = MikroCAD('config\\company_mikrocad.cfg')
        
    def test_00_init(self):
        self.mc.switchToEmulator()
        
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.mc.deinitMeasurement()
