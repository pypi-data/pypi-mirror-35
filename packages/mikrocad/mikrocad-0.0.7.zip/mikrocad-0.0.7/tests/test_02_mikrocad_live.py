# -*- coding: utf-8 -*-

### imports ###################################################################
import unittest

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD
from mikrocad.widgets.mikrocad_live import LiveWidget

from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

###############################################################################
class MikroCAD_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mc = MikroCAD('config\\company_mikrocad.cfg')
        
        cls.mc.initMeasurement()
        cls.mc.brightnessCam = 7
        cls.mc.projector = 1
        cls.mc.dynamicMode = 2
        cls.mc.language = 0

        cls.widget = LiveWidget()

    def test_01_init(self):
        self.assertGreater(self.widget.handle, 0)
        error = self.mc.start_live_image(self.widget.handle)
        self.assertEqual(error, 0)
        self.assertTrue(self.mc.liveOn)

        self.widget.show()
        
    def test_02_halt_live_image(self):
        liveOn = self.mc.halt_continue_live_image()
        self.assertFalse(liveOn)

    def test_03_continue_live_image(self):
        liveOn = self.mc.halt_continue_live_image()
        self.assertTrue(liveOn)

    def test_12_stop_live_image(self):
        self.mc.stop_live_image()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.mc.deinitMeasurement()
