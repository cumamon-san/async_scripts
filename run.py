#!/bin/python

from multiprocessing.pool import ThreadPool
from threading import Thread
import subprocess
from time import sleep

def task(count: int):
    print('Run task', count)
    res = subprocess.run(['./task.sh'], shell=True).returncode
    sleep(count)
    return res

with ThreadPool(processes=2) as pool:
    for result in pool.imap(task, [1,2,3,4,5,6,7]):
        print('Get result', result)
