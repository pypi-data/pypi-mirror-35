# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from mikrocad.experiment import Experiment, Sample
from mikrocad.fd3 import FD3Reader

filename = 'data/mounting_plate.fd3'
filename = 'data/wafer.fd3'

fd3 = FD3Reader(filename)
data = fd3.Image
i_NaN = fd3.i_nan
scale = fd3.scale

experiment = Experiment()
scan = experiment.read_scan_data(data=data, i_NaN=i_NaN, scale=scale)
t = scan.estimate_wafer_thickness()

Nx = fd3.Nx

Nx2 = Nx // 2

plt.close('all')
fig, axis = plt.subplots()
axis.hlines(0, -2, 2, 'r', linewidth=1)
axis.vlines(0, -1, 1, 'r', linewidth=1)
axis.scatter(scan.y, scan.Z[Nx2,:], s=1)
axis.set_aspect('equal')
axis.set_xlabel('y [mm]')
axis.set_ylabel('z [mm]')
axis.set_xlim(-2, 2)
axis.set_ylim(-1, 1)

fig.savefig('output/wafer_thickness_estimation.png', dpi=300, transparent=True)