#!/usr/bin/env python3

import threading, timeit

def countdown(n):
    while n > 0:
        n -= 1

def countdown_k(n, k):
    threads = [threading.Thread(target=countdown,args=(n//k,)) for _ in range(k)]
    [t.start() for t in threads]
    [t.join() for t in threads]

def countdown_2(n):
    t1 = threading.Thread(target=countdown,args=(n//2,))
    t2 = threading.Thread(target=countdown,args=(n//2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(6):
        k = 2 ** i
        time = timeit.timeit(lambda: countdown_k(10000000, k), number=10)
        print("{:.2f}".format(time))