# -*- coding: utf-8 -*-

### imports ###################################################################
import logging
import time

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

###############################################################################
if __name__ == "__main__":
    # %% setup logger
    logging.basicConfig(level=logging.DEBUG)

    mc = MikroCAD('config\\company_mikrocad.cfg')
    
    if mc.initMeasurement() == 0:
        mc.start_live_image(1252983820)

        time.sleep(3)
        mc.halt_continue_live_image()
        
        time.sleep(3)
        mc.halt_continue_live_image()

        time.sleep(3)
        mc.stop_live_image()        
        mc.deinitMeasurement()

        print('Done.')
        
