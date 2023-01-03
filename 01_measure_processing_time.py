#!/usr/bin/env python3

# Python 3.9.5

# 01_measure_processing_time.py

# Purpose: Measuring process times during the execution of program code using the timeit module.

# Dependencies
import timeit
import time

# __________________________________________________________________________________________________________________
# timeit default command: 
timeit.timeit(stmt='', setup='', repeat='', timer=time.perf_counter, number=1, globals=None)

timeit.timeit(stmt='n+=1', setup='n=0', timer=time.perf_counter, number=1000, globals=None)

# __________________________________________________________________________________________________________________
# Time measurement of a function:
def test_function():
    return [n**2 for n in range(10000)]

duration = timeit.timeit(stmt='test_function()', setup='from __main__ import test_function', number=1, globals=None)
print(duration)

# __________________________________________________________________________________________________________________
# Time measurement of a function with a global variable:
import random
N = 1000000

def normal_variation(N):
    return [random.normalvariate(0, 1) for n in range(N)]

duration_globals = timeit.timeit(stmt='normal_variation(N)', setup='from __main__ import normal_variation', timer=time.perf_counter, number=1, globals=globals())

print(duration_globals)
