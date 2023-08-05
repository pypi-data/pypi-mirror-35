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
        
        mc.projectionPattern = 0

        image_array = mc.get_camera_image()
        sharpness = np.std(image_array, axis=1)
        i_focus = np.argmax(sharpness)

        mc.brightness = 10
        mc.projectionPattern = 6
        image_array = mc.get_camera_image()

        i_list = []
        j_list = []

        for i in range(i_focus - 10, i_focus + 10):
            j = np.where(image_array[i, :] > 50)[0][0]
            i_list.append(i)
            j_list.append(j)
            
        x_edge = np.array(j_list)
        y_edge = np.array(i_list)
        
        m, n = np.polyfit(x_edge, y_edge, 1)

        plt.close('all')
        plt.imshow(image_array, origin='lower')
        
        plt.figure()
        plt.plot(image_array[i_focus, :])
        
        mc.deinitMeasurement()
