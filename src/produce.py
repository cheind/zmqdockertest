import zmq
import numpy as np
import os
import time

def main(zmq_addr, byte_size, nmsg=100):
    print('Producer running', zmq_addr)
    context = zmq.Context()
    publisher = context.socket(zmq.PUSH)
    publisher.bind(zmq_addr)    
    img = (np.random.rand(byte_size)*255).astype(np.uint8)
    for i in range(nmsg):        
        img[0] = i % 255
        publisher.send_pyobj({'img':img, 'time':time.time()})
    publisher.send_pyobj(None)
    print('Producer stopping')

if __name__ == '__main__':
    ZMQ_ADDR = os.environ.get('ZMQ_ADDR', 'ipc:///tmp/test.pipe')
    BYTESIZE = int(os.environ.get('BYTESIZE'))
    MESSAGES = int(os.environ.get('MESSAGES'))
    main(ZMQ_ADDR, BYTESIZE, MESSAGES)