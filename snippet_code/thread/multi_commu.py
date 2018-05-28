# encoding=utf-8
from multiprocessing import Process, Queue
from time import time, sleep


def writeQ(q):
    for c in ['A', 'B', 'C', 'D', 'E']:
        print('Writing %s in Queue~' % c)
        q.put(c)
        sleep(0.5)


def readQ(q):
    while True:
        c = q.get()
        print('Reading %s in Queue~' % c)
        sleep(0.5)


if __name__ == '__main__':
    q = Queue()
    writer = Process(target=writeQ, args=(q,))
    reader = Process(target=readQ, args=(q,))
    writer.start()
    reader.start()

    reader.join(timeout=5)
    reader.terminate()
