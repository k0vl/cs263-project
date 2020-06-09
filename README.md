# cs263-project

## project vision
Compare the performance of various Python implementations for multithreaded tasks. Investigate the performance penalty of Python global interpreter lock and its advantages and disadvantages. 

## Running tests
* install Python2/3, PyPy2/3, Jython, IronPython
* countdown.py is for CPU bound task, netop.py is for network task, diskop.py is for disk tasks, and sort.py is for quicksort.
* in diskop.py, disable countdown_read() and associated code when testing IronPython, disable countdown_write_sync() when testing IronPython and Jython. 
* in netop.py, switch to the commented out header when using Python3. 

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
* installed Hyper-V
* Installed some python distributions

#### implementations to test
* CPython - default implementation, interpreter
* Jython - compiles to JVM 
* IronPython - compiles to .NET
* PyPy - written in Python, jit compiler
* Stackless Python
* Cython? Nuitka?

### week 6
* installed docker
* installed rest of Python implementation on Docker

### week 7 
* reading about what benchmark program to use
* benchmark reference:
 * https://attractivechaos.github.io/plb/
 * https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html
 * https://en.wikipedia.org/wiki/Parallel_computing#Algorithmic_methods
 
 ### week 8
 * Still reading
 * not much progress this week
 
