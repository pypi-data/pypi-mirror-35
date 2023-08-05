# -*- coding: utf-8 -*-

### imports ###################################################################
import logging

### imports from ##############################################################
from mikrocad.mikrocad import MikroCAD
from mikrocad.zmq_server import ZeroMQ_Server

###############################################################################
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    mc = MikroCAD('config\\company_mikrocad.cfg')
    zmq_server = ZeroMQ_Server(mc)
    zmq_server.poll()
