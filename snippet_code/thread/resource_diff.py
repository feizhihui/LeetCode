# encoding=utf-8
from multiprocessing import Process
from threading import Thread
import threading

lock = threading.Lock()


def run(info_list, n):
    lock.acquire()
    info_list.append(n)
    lock.release()
    print('info_list=%s' % info_list)


if __name__ == '__main__':
    info_list = []
    print('=' * 10, 'multiprocessing', '=' * 10)
    for i in range(10):
        p = Process(target=run, args=(info_list, i))
        p.start()
        p.join()
    print('=' * 10, 'multithreading', '=' * 10)
    for i in range(10):
        p = Thread(target=run, args=(info_list, i))
        p.start()
        p.join()
