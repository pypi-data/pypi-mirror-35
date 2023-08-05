# -*- coding: utf-8 -*-

import zmq

if __name__ == '__main__':
    context = zmq.Context()
    
    #  Socket to talk to server
    socket_mikrocad = context.socket(zmq.REQ)
    socket_mikrocad.connect("tcp://127.0.0.1:5555")
    
    data_dict = {"x-size": '?'}
    
    socket_mikrocad.send_json(data_dict)
    
    data_dict = socket_mikrocad.recv_json()
    print(data_dict)