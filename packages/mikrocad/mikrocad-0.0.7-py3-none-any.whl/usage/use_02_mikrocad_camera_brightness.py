# -*- coding: utf-8 -*-

### imports ###################################################################
import logging
import os
import time

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

    item = 'wafer_surface'
    mc = MikroCAD('config\\company_mikrocad.cfg')
          
    if mc.initMeasurement() == 0:
        mc.projector = 1
        mc.projectionPattern = 0

        for i in range(20):
            brightness = i + 1
            mc.brightness = brightness

            time.sleep(1)

            image_array = mc.get_camera_image()
            method = Image.FLIP_TOP_BOTTOM
            image = Image.fromarray(image_array).transpose(method)

            brightness_str = '%02i' % brightness
            filename = item + '__brightness_' + brightness_str + '.png'
            fullfile = os.path.join('output', filename)
            image.save(fullfile)
        
        mc.deinitMeasurement()
