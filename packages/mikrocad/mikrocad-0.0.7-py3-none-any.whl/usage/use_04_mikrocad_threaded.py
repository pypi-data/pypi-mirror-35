# -*- coding: utf-8 -*-

### imports ###################################################################
# import multiprocessing
import logging
import time

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

mc = MikroCAD('config\\company_mikrocad.cfg')

###############################################################################
if __name__ == "__main__":
    # %% setup logger
    logging.basicConfig(
        format = '%(asctime)s %(levelname)s: %(message)s',
        level = logging.DEBUG,
        datefmt = '%Y-%m-%d %I:%M:%S'
    )


    parameters = {
            'brightness': 10,
            'dynamic mode': 2,
            'projector': 1,
    }

    mc.measurement_threaded('initialise')
    mc.measurement_threaded('set_parameters', parameters)
    mc.measurement_threaded('measure')
    mc.measurement_threaded('deinitialise')

    i = 0

    while mc.status != 'deinitialised':
        print(i, mc.status, mc.task_list)
        time.sleep(1)
        i += 1
    
    print('Done.')
        