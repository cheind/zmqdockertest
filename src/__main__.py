
import multiprocessing as mp
from . import consume
from . import produce


def main():
    procs = [
        mp.Process(target=produce.main, args=('tcp://0.0.0.0:30000', 10000000, 1000)),
        mp.Process(target=consume.main, args=('tcp://127.0.0.1:30000',)),
    ]
    [p.start() for p in procs]
    [p.join() for p in procs]

if __name__ == '__main__':
    main()