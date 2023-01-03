#!/usr/bin/env python3

# Python 3.9.5

# Purpose: Measuring process times during the execution of program code using the timeit module.

# Dependencies
import timeit
import time

# timeit default command: 
timeit.timeit(stmt='', setup='', repeat='', timer=time.perf_counter, number=1, globals=None)

timeit.timeit(stmt='n+=1', setup='n=0', timer=time.perf_counter, number=1000, globals=None)

# Time measurement of a function:
def test_function():
    return [n**2 for n in range(10000)]

duration = timeit.timeit(stmt='test_function()', setup='from __main__ import test_function', number=1, globals=None)
print(duration)

duration_globals = timeit.timeit(stmt='test_function()', setup='from __main__ import test_function', number=1, globals=globals())
print(duration_globals)
