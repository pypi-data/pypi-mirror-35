# -*- coding: utf-8 -*-

### imports ###################################################################
import numpy as np
import os
import unittest

### imports from ##############################################################
from mikrocad.fd3 import FD3Reader

###############################################################################
class FD3Test(unittest.TestCase):
    datadir = 'data'
    filename = 'mounting_plate.fd3'
    
    dx = 0.00305
    dy = 0.00305
    dz = 1E-4

    iy_left = 195
    iy_right = 751
    
    iz_nan = -10010
    iz_max = 9999

    m_median = -1.17745775
    n_median = 1.6845953

    m_mid = -1.17707744
    n_mid = 1.68423001
        
    Nx = 1624
    Ny = 1236

    xmin = 0.0
    xmax = 4.95352819
    
    ymin = 0.0
    ymax = 3.77131270
    
    @classmethod
    def setUpClass(cls):
        fullfile = os.path.join(cls.datadir, cls.filename)
        cls.fd3 = FD3Reader(fullfile)
    
    def test_00_FD3Reader(self):
        Nx = self.fd3.Nx
        self.assertEqual(Nx, self.Nx)
        
        Ny = self.fd3.Ny
        self.assertEqual(Ny, self.Ny)
        
        i_nan = self.fd3.i_nan
        self.assertEqual(i_nan, self.iz_nan)

        dx = self.fd3.dx
        self.assertAlmostEqual(dx, self.dx, places=5)

        dy = self.fd3.dy
        self.assertAlmostEqual(dy, self.dy, places=5)
        
        dz = self.fd3.dz
        self.assertAlmostEqual(dz, self.dz, places=4)

    def test_01_plane(self):
        dz = self.fd3.dz
        x = self.fd3.x
        y = self.fd3.y
        Nx2 = self.fd3.Nx2
        I = self.fd3.Image
        Z = self.fd3.Z

        I_min = np.min(I)
        self.assertEqual(I_min, self.iz_nan)
        
        i_max = np.max(I)
        self.assertEqual(i_max, self.iz_max)
        
        I_median = np.median(I[:-1, :], axis=0)
        
        valid_indices = np.where(I_median > -10010)[0]
        iy_left = valid_indices[0]
        iy_right = valid_indices[-1]
        
        self.assertEqual(iy_left, iy_left)
        self.assertEqual(iy_right, iy_right)

        y_vaild = y[iy_left:iy_right]
        z_median = dz * I_median[iy_left:iy_right]

        p = np.polyfit(y_vaild, z_median, 1)
        self.assertAlmostEqual(p[0], self.m_median)
        self.assertAlmostEqual(p[1], self.n_median)

        y_mid = self.fd3.y[iy_left:iy_right]
        z_mid = Z[Nx2, iy_left:iy_right]
        
        y_mid = y_mid[np.isfinite(z_mid)]
        z_mid = z_mid[np.isfinite(z_mid)]
        
        p = np.polyfit(y_mid, z_mid, 1)
        self.assertAlmostEqual(p[0], self.m_mid)
        self.assertAlmostEqual(p[1], self.n_mid)

        self.assertAlmostEqual(x[0], self.xmin)
        self.assertAlmostEqual(x[-1], self.xmax)

        self.assertAlmostEqual(y[0], self.ymin)
        self.assertAlmostEqual(y[-1], self.ymax)
