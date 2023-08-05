# -*- coding: utf-8 -*-

### imports ###################################################################
import unittest

### imports from ##############################################################
from mikrocad.widgets.mikrocad_live import LiveWidget

from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

###############################################################################
class MikroCAD_Test(unittest.TestCase):
    item = 'notch'
    
    @classmethod
    def setUpClass(cls):
        
        cls.widget = LiveWidget(live_image=False)

    def test_01_init(self):
        self.assertEqual(self.widget.handle, 1234)

        self.widget.show()

        
    def test_02_item(self):
        self.widget.item = 'nonsense'

        self.widget.item = 'notch'
        self.assertEqual(self.widget.item, self.item)        

    def test_03_brightness(self):
        # liveOn = self.mc.halt_continue_live_image()
        # self.assertTrue(liveOn)

        for b in range(1, 21):
            self.widget.brightness = b
            self.assertEqual(self.widget.brightness, b)
        

    def test_12_stop_live_image(self):
        # self.mc.stop_live_image()

        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass
        # self.mc.deinitMeasurement()
