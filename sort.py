#!/usr/bin/env python3

from threading import Thread
from multiprocessing import Process
import threading, time, random, timeit

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )

def multiprocess_qsort(arr, low, high):
    # print(f"thead {threading.current_thread()} is sorting {sets[left:right]}", flush=True)
    if low < high:
        pi = partition(arr, low, high) 
        lt = Process(target= lambda: multiprocess_qsort(arr, low, pi-1))
        rt = Process(target= lambda: multiprocess_qsort(arr, pi + 1, high))
        lt.start()
        rt.start()
        lt.join()
        rt.join()

def multithread_qsort(arr, low, high):
    # print(f"thead {threading.current_thread()} is sorting {sets[left:right]}", flush=True)
    if low < high:
        pi = partition(arr, low, high) 
        lt = Thread(target= lambda: multithread_qsort(arr, low, pi-1))
        rt = Thread(target= lambda: multithread_qsort(arr, pi + 1, high))
        lt.start()
        rt.start()
        lt.join()
        rt.join()

def half_multithread_qsort(arr, low, high):
    # print(f"thead {threading.current_thread()} is sorting {sets[left:right]}", flush=True)
    if low < high:
        pi = partition(arr, low, high) 
        lt = Thread(target= lambda: half_multithread_qsort(arr, low, pi-1))
        lt.start()
        half_multithread_qsort(arr, pi + 1, high)
        lt.join()

def singlethread_qsort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high) 
        singlethread_qsort(arr, low, pi-1)
        singlethread_qsort(arr, pi + 1, high)


def shuffle_and_sort(arr, sorter, start, end):
    random.shuffle(arr)
    sorter(arr, start, end)

if __name__ == "__main__":
    arr = list(range(100))
    time_singlethread = timeit.timeit(lambda: shuffle_and_sort(arr, singlethread_qsort, 0, len(arr)-1), number=100)
    print(f"time_singlethread: {time_singlethread:.2f}")
    time_multithread = timeit.timeit(lambda: shuffle_and_sort(arr, multithread_qsort, 0, len(arr)-1), number=100)
    print(f"time_multithread: {time_multithread:.2f}")
    time_half_multithread = timeit.timeit(lambda: shuffle_and_sort(arr, half_multithread_qsort, 0, len(arr)-1), number=100)
    print(f"time_half_multithread: {time_half_multithread:.2f}")
    time_multiprocess = timeit.timeit(lambda: shuffle_and_sort(arr, multiprocess_qsort, 0, len(arr)-1), number=100)
    print(f"time_multiprocess: {time_multiprocess:.2f}")
    # shuffle_and_sort(arr, threaded_qsort, 0, len(arr)-1)
    print(arr, flush=True)