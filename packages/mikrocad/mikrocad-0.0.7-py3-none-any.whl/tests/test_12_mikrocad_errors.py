# -*- coding: utf-8 -*-

### imports ###################################################################
from ctypes import byref, c_int
import unittest

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

class MikroCAD_Errors_Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.mc = MikroCAD('config\\company_mikrocad.cfg')
        
    def test_00_uninitialised(self):
        error = self.mc.doMeasure()
        self.assertEqual(error, -2003)

    def test_01_wrong_program_path(self):
        self.mc.programPath = '.'
        error = self.mc.initMeasurement()
        self.assertEqual(error, -2021)

    def test_02_get_wrong_parameter(self):
        wrong_id = 1234
        pointer_to_int = byref(c_int())

        error = self.mc.LMI_DLL._GFM_GetMeasParameterInt(
                wrong_id, pointer_to_int)

        self.assertEqual(error, -2031)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.mc.deinitMeasurement()
