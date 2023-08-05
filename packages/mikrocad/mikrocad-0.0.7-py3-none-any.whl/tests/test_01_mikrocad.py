# -*- coding: utf-8 -*-

### imports ###################################################################
import time
import unittest

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

class MikroCAD_Test(unittest.TestCase):
    
    Ny, Nx = shape = 1236, 1624
    
    # invalid_value = -32768
    invalid_value = -10010
    language = 0
    
    max_projection_area_x_size = 1.608
    max_projection_area_y_size = 1.787

    ### measurement catalog
    Nc = 1 # number of measurement catalogs
    catalog_name = 'Standard'
    Ni = 1
    item_name = 'Standard'
    
    x_scale = 0.00305 # mm
    y_scale = 0.00305 # mm
    z_scale = 1E-4 # mm
    
    @classmethod
    def setUpClass(cls):
        cls.mc = MikroCAD('config\\company_mikrocad.cfg')
        
    def test_00_init(self):        
        self.assertEqual(self.mc.initMeasurement(), 0)

    def test_01_available_parameters(self):
        parameter_id_dict = {
                11: True,
                12: True,
                13: False,
                14: False,
                15: False,
                16: True,
                21: True,
                22: True,
                111: True,
                112: True,
                113: True,
                114: True,
                115: True,
                201: True,
                202: True,
        }
        
        for parameter_id, value in parameter_id_dict.items():
            available = self.mc.measParameterAvailable(parameter_id)
            
            self.assertEqual(available, value)

    def test_02_language(self):
        self.mc.language = self.language
        self.assertEqual(self.mc.language, self.language)
        
    def test_03_brightness(self):
        self.mc.brightness = 7
        self.assertEqual(self.mc.brightness, 7)
        
    def test_04_projector(self):
        self.mc.projector = 0
        self.assertEqual(self.mc.projector, 0)
        
        self.mc.projector = 1
        self.assertEqual(self.mc.projector, 1)

    def test_05_dynamic_mode(self):
        self.mc.dynamic_mode = 2
        self.assertEqual(self.mc.dynamic_mode, 2)
        
    def test_06_image_size(self):
        self.assertEqual(self.mc.x_size, self.Nx)
        self.assertEqual(self.mc.y_size, self.Ny)

    def test_07_scale(self):
        scale = self.mc.scale
        
        self.assertAlmostEqual(scale[0], self.x_scale, places=5)
        self.assertAlmostEqual(scale[1], self.y_scale, places=5)
        self.assertAlmostEqual(scale[2], self.z_scale, places=5)

        self.assertAlmostEqual(self.mc.x_scale_ref, self.x_scale, places=5)
        self.assertAlmostEqual(self.mc.y_scale_ref, self.y_scale, places=5)

    def test_08_projection(self):
        self.assertAlmostEqual(
                self.mc.max_projection_area_x_size,
                self.max_projection_area_x_size, places=3)
        
        self.assertAlmostEqual(
                self.mc.max_projection_area_y_size,
                self.max_projection_area_y_size, places=3)

        for pattern in range(13):
            self.mc.projectionPattern = pattern
            time.sleep(0.5)
            self.assertEqual(self.mc.projectionPattern, pattern)

        self.mc.projectionPattern = 0

    def test_09_measurement_program_catalog(self):
        self.assertEqual(self.mc.Nc, self.Nc)

        catalog_name = self.mc.get_meas_prog_catalog_name(0)
        self.assertEqual(catalog_name, self.catalog_name)
        
        Ni = self.mc.get_number_meas_prog_items(0)
        self.assertEqual(Ni, self.Ni)
        
        item_name = self.mc.get_meas_prog_item_name(0, 0)
        self.assertEqual(item_name, self.item_name)
        
    def test_10_measure(self):
        error = self.mc.doMeasure()
        self.assertEqual(error, 0)
        
        self.assertEqual(self.mc.invalidValue, self.invalid_value)

    def test_11_save(self):
        error = self.mc.save()
        self.assertEqual(error, 0)
        
        error = self.mc.saveScan('output/test.fd3')
        self.assertEqual(error, 0)

    def test_12_camera(self):
        M = self.mc.get_camera_image()
        self.assertTupleEqual(self.shape, M.shape)

    def test_13_save_camera(self):
        error = self.mc.saveCam('output/test.jpg')
        self.assertEqual(error, 0)

    def test_97_set_wrong_parameter(self):
        error = self.mc.setParameter('brightness', 100)
        self.assertEqual(error, -2031)

    def test_98_project_image(self):
        self.mc.projectImage()

    def test_99_projection_area(self):
        self.mc.set_projection_area()
        self.mc.reset_projection_area()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.mc.deinitMeasurement()
