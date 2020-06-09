#!/usr/bin/env python3

import httplib as client
# import http.client
import threading, timeit, sys, os

def http_conn(n):
    for _ in range(n):
        conn = client.HTTPConnection('www.python.org')
        conn.request("HEAD","/index.html")
        conn.close()

def run_k_threads(target, n, k):
    threads = [threading.Thread(target=target,args=(n//k,)) for _ in range(k)]
    [t.start() for t in threads]
    [t.join() for t in threads]

if __name__ == "__main__":
    for i in range(1):
        k = 2 ** i
        time = timeit.timeit(lambda: run_k_threads(http_conn, 100, k), number=1)
        print("http_conn {} threads: {:.4f}".format(k, time))
        sys.stdout.flush()
