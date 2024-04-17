#!/usr/local/bin/python3

import os
import random
import multiprocessing
from multiprocessing import Pool

# caculate the number of points in the unit circle
# out of n points
def monte_carlo_pi_part(n):
    count = 0
    for i in range(int(n)):
        x=random.random()
        y=random.random()
        # if it is within the unit circle
        if x*x + y*y <= 1:
            count=count+1
    #return
    return count


if __name__=='__main__':

    np1 = multiprocessing.cpu_count()
    print('Possible: {0:1d} CPUs'.format(np1))
    
    np = int(os.getenv('CORECHOICE'))
    print(f'   Using: {np} CPUs')

    # Nummber of points to use for the Pi estimation
    n = 1000000000

    print(f' Running: {n} point estimation')

    # iterable with a list of points to generate in each worker
    # each worker process gets n/np number of points to calculate Pi from

    part_count=[n/np for i in range(np)]

    #Create the worker pool
    # http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
    pool = Pool(processes=np)

    # parallel map
    count=pool.map(monte_carlo_pi_part, part_count)

    print("Estimated value of Pi: ", sum(count)/(n*1.0)*4)
