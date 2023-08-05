# -*- coding: utf-8 -*-

#
#   ZMQ client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "getHandle" to server, expects integer handle to live widget back
#

### imports ###################################################################
import logging
import zmq

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD

###############################################################################
def getHandle():
    ###  create socket to talk to live widget server
    logging.debug("Connecting to live widget")
    context = zmq.Context()
    socket_live_image = context.socket(zmq.REQ)
    socket_live_image.connect("tcp://127.0.0.1:5556")

    ### send handle request
    data_dict = {'handle': '?'}
    socket_live_image.send_json(data_dict)
    
    ### receive handle request
    handle = socket_live_image.recv_json()['handle']
    logging.debug("Handle to live image: %i" % handle)

###############################################################################
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    ### init 3D scanner
    mc = MikroCAD('config\\company_mikrocad.cfg')
    mc.initMeasurement()

    # start live image widget
    # use_20_mikrocad_live_widget.py
             
    # import subprocess
    # subprocess.Popen('use_live_widget.bat') # !!! not working yet !!!

    ### get handle to live image
    # handle = getHandle()
    
    # mc.start_live_image(handle)

    '''
        time.sleep(3)
        mc.halt_continue_live_image()
        
        time.sleep(3)
        mc.halt_continue_live_image()

        time.sleep(3)
        mc.stop_live_image()        
        mc.deinitMeasurement()

        print('Done.')
    '''
