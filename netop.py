#!/usr/bin/env python3

import threading, multiprocessing, timeit, sys, os, http.client

def http_conn(n):
    for _ in range(n):
        conn = http.client.HTTPConnection('www.python.org')
        conn.request("HEAD","/index.html")
        conn.close()

def run_k_threads(target, n, k):
    threads = [threading.Thread(target=target,args=(n//k,)) for _ in range(k)]
    [t.start() for t in threads]
    [t.join() for t in threads]

if __name__ == "__main__":
    for i in range(5):
        k = 2 ** i
        time = timeit.timeit(lambda: run_k_threads(http_conn, 100, k), number=1)
        print("http_conn {} threads: {:.2f}".format(k, time))
        sys.stdout.flush()
