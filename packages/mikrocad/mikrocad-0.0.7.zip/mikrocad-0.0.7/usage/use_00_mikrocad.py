# -*- coding: utf-8 -*-

### imports ###################################################################
import logging

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

###############################################################################
if __name__ == "__main__":
    # %% setup logger
    logging.basicConfig(level=logging.INFO)

    mc = MikroCAD('config\\company_mikrocad.cfg')
    
    if mc.initMeasurement() == 0:
        mc.projector = 1
        mc.brightness = 10
        mc.dynamic_mode = 0
        
        for i_catalog in range(mc.Nc):
            catalog_name = mc.get_meas_prog_catalog_name(i_catalog)

            Ni = mc.get_number_meas_prog_items(i_catalog)
            for i_item in range(Ni):
                item_name = mc.get_meas_prog_item_name(i_catalog, i_item)
                logging.info('%i %s %s', i_catalog, catalog_name, item_name)

        mc.deinitMeasurement()
        
    print('Done.')
        
        