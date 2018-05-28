# encoding=utf-8
from multiprocessing import Process, Pool
from time import time, sleep


def f(x):
    print(x * x)
    sleep(1)
    return x * x


if __name__ == '__main__':
    pool = Pool(processes=5)
    res_list = []

    for i in range(10):
        res = pool.apply_async(f, args=(i,))
        res_list.append(res)

    pool.close()  # close the pool to stop applying
    pool.join()  # block to finish

    for res in res_list:
        print('Result:', res.get(timeout=5))
