# encoding=utf-8

from multiprocessing import Process
from time import time, sleep
import os


def f(n):
    sleep(1)
    print(n * n, 'ProcessId:%d' % (os.getpid()))


def main():
    print('ParentProcessId:%d' % os.getpid())
    ps = []
    for i in range(8):
        p = Process(target=f, args=(i,))
        p.start()
        ps.append(p)
        # p.join()  # single process
        # p.terminate()  # kill process
    for p in ps:
        p.join()


if __name__ == '__main__':
    start_time = time()
    main()
    end_time = time()
    print('Consuming time seconds:%d' % (end_time - start_time))
