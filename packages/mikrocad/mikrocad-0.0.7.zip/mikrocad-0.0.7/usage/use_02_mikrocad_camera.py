# -*- coding: utf-8 -*-

### imports ###################################################################
import logging
import matplotlib.pyplot as plt
import numpy as np

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD
from PIL import Image

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
        mc.projectionPattern = 0

        mc.brightness = 7

        image_array = mc.get_camera_image()
        sharpness = np.std(image_array, axis=1)
        i_focus = np.argmax(sharpness)

        image = Image.fromarray(image_array)
        image.save('image.png')

        plt.close('all')
        plt.imshow(image_array, origin='lower')
        
        plt.figure()
        plt.plot(image_array[i_focus, :])
        
        mc.deinitMeasurement()
