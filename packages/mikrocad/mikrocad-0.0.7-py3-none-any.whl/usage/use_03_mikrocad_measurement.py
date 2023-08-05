# -*- coding: utf-8 -*-

### imports ###################################################################
import logging
import matplotlib.pyplot as plt
import numpy as np

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

###############################################################################
if __name__ == "__main__":
    # %% setup logger
    logging.basicConfig(
        format = '%(asctime)s %(levelname)s: %(message)s',
        level = logging.DEBUG,
        datefmt = '%Y-%m-%d %I:%M:%S'
    )

    mc = MikroCAD('config\\company_mikrocad.cfg')
    
    if mc.initMeasurement() == 0:
        mc.projector = 1
        mc.brightness = 8

        mc.doMeasure()
        mc.save('output/use_03_mikrocad_measurement.fd3')

        Nx = mc.x_size
        Ny = mc.y_size

        data = mc.data
        y = mc.y

        fig, ax = plt.subplots(2, 1)

        ax[0].imshow(np.rot90(data))
        ax[0].set_aspect('equal')

        ax[1].scatter(y, data[1500,:], s=1)
        ax[1].set_xlabel('y')
        ax[1].set_ylabel('z')
        
        fig.tight_layout()

        mc.deinitMeasurement()
        print('Done.')
        
        