# -*- coding: utf-8 -*-

### imports ###################################################################
import time
import unittest

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

class Threaded_Test(unittest.TestCase):
    parameters = {
            'brightness': 10,
            'dynamic mode': 2,
            'projector': 1,
    }

    @classmethod
    def setUpClass(cls):
        cls.mc = MikroCAD('config\\company_mikrocad.cfg')
        
    def test_00_threads(self):
        self.mc.measurement_threaded('initialise')
        self.mc.measurement_threaded('set_parameters', self.parameters)
        self.mc.measurement_threaded('measure')
        self.mc.measurement_threaded('deinitialise')
        self.mc.measurement_threaded('join')

        i = 0

        while self.mc.status != 'deinitialised':
            print(i, self.mc.status, self.mc.task_list)
            time.sleep(1)
            i += 1

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass
