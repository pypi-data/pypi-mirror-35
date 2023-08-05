# -*- coding: utf-8 -*-

### imports ###################################################################
import logging

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
    
    parameter_id_list = [
            11, 12, 13, 14, 15, 16, 21, 22,
            111, 112, 113, 114, 115,
            201, 202,
    ]
    
    if mc.initMeasurement() == 0:
        for i in parameter_id_list:
            print(i, mc.measParameterAvailable(i))

        mc.brightness = 9       
        print('Brightness:', mc.brightness)        
        
        mc.deinitMeasurement()
        print('Done.')
        
