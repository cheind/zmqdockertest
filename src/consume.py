import zmq
import sys
import numpy as np
import os
import time
from itertools import count

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def main(zmq_addr):
    print('Consumer running', zmq_addr)
    print('ZMQ version', zmq.__version__)
    print('Python version', sys.version_info)
    context = zmq.Context()    
    subscriber = context.socket(zmq.PULL)
    subscriber.connect(zmq_addr)
    tfirst = None
    tbytes = 0
    lastb = 0
    for idx in count(1):
        obj = subscriber.recv_pyobj()
        if obj is None:
            break
        if tfirst is None:
            tfirst = obj['time']   
        else:
            assert obj['img'][0] != lastb
        tbytes += obj['img'].nbytes
        lastb = obj['img'][0]
        
    elapsed = (time.time() - tfirst)
    bytes_per_sec = tbytes / elapsed

    print(f'throughput {sizeof_fmt(bytes_per_sec)}/sec, consumed {idx-1}')
    print('Consumer stopping')

if __name__ == '__main__':
    ZMQ_ADDR = os.environ.get('ZMQ_ADDR', 'ipc:///tmp/test.pipe')
    main(ZMQ_ADDR)