# cs263-project

## project vision
Compare the performance of various Python implementations for multithreaded tasks. Investigate the performance penalty of Python global interpreter lock and its advantages and disadvantages. 

## Progress

### week 4
* researched the different python implementations and how they deal with multithreading.
  * CPython and PyPy uses GIL, whereas Jython and IronPyhton does not.
  * Stackless Python can achieve cooperative multitasking under GIL
* researched the type of tasks impacted by GIL

https://wiki.python.org/moin/GlobalInterpreterLock lists some reqirements for replacing the GIL.

TODO:
* Start writing benchmarks
* Investigate how Python with GIL handles ML tasks.

### week 5
* Installed some python distributions
* cython ?

