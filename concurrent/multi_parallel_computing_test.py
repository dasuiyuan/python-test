# -*- coding: utf-8 -*-
# @Time: 2025/8/7 14:34
# @Author: Sui Yuan
# @Software: PyCharm
# @Desc:

import time
import math
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

N = 1000
K = 10000


def cpu_task(i):
    s = 0.0
    for _ in range(K):
        s += math.sin(i) * math.cos(i)
    return s


def io_test():
    time.sleep(0.01)


def serial():
    return [cpu_task(i) for i in range(N)]


def multi_thread(workers=4):
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = []
        futures = [pool.submit(cpu_task, i) for i in range(N)]
        for fut in as_completed(futures):
            results.append(fut.result())
        return results


def multi_process(workers=4):
    with ProcessPoolExecutor(max_workers=workers) as pool:
        results = []
        futures = [pool.submit(cpu_task, i) for i in range(N)]
        for fut in as_completed(futures):
            results.append(fut.result())  # 如果此处包含print，会导致结果回传主进程导致耗时，可以内部打印
        return results


def multi_process_map(workers=4):
    with ProcessPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(cpu_task, range(N)))


if __name__ == '__main__':
    start_time = time.time()
    res = serial()
    print(res)
    serial_cost = time.time() - start_time

    workers = multiprocessing.cpu_count()
    print(f"workers:{workers}")
    start_time = time.time()
    res = multi_thread(workers)
    print(res)
    thread_cost = time.time() - start_time

    start_time = time.time()
    res = multi_process_map(workers)
    print(res)
    process_cost = time.time() - start_time

    print(f"ser cost:{serial_cost} thr cost:{thread_cost} pro cost:{process_cost}")

    # import timeit
    #
    # for name, fn in [('serial', serial),
    #                  ('thread', thread),
    #                  ('process', run_process)]:
    #     t = timeit.timeit(fn, number=1)
    #     print(f"{name:7}: {t:.2f} s")
