#!/usr/bin/env python3

import threading, multiprocessing, timeit, sys, os

def countdown_write(fh, n):
    while n > 0:
        n -= 1
        fh.write(str(n) + '\n')

def countdown_read(fh, n):
    while n > 0:
        n -= 1
        line = fh.readline()

def countdown_write_sync(fh, n):
    while n > 0:
        n -= 1
        fh.write(str(n) + '\n')
        os.fsync(fh)

def run_k_threads(target, fh, n, k):
    threads = [threading.Thread(target=target,args=(fh, n//k,)) for _ in range(k)]
    [t.start() for t in threads]
    [t.join() for t in threads]

if __name__ == "__main__":
    for i in range(5):
        k = 2 ** i
        with open("tmp/{}_thread_test.out".format(k), 'w') as fh:
            time = timeit.timeit(lambda: run_k_threads(countdown_write, fh, 10000, k), number=1)
            print("countdown_write {} threads: {:.6f}".format(k, time))
            sys.stdout.flush()

    for i in range(5):
        k = 2 ** i
        with open("tmp/{}_thread_test_sync.out".format(k), 'w') as fh:
            time = timeit.timeit(lambda: run_k_threads(countdown_write_sync, fh, 10000, k), number=1)
            print("countdown_write_sync {} threads: {:.6f}".format(k, time))
            sys.stdout.flush()

    for i in range(5):
        k = 2 ** i
        with open("tmp/{}_thread_test.out".format(k), 'r') as fh:
            time = timeit.timeit(lambda: run_k_threads(countdown_read, fh, 10000, k), number=1)
            print("countdown_read {} threads: {:.6f}".format(k, time))
            sys.stdout.flush()