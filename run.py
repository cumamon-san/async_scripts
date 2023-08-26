#!/bin/python

from multiprocessing.pool import ThreadPool
from threading import Thread
import subprocess
from time import sleep

def task(count: int):
    print('Run task', count)
    return subprocess.run(['./task.sh', str(count)]).returncode

with ThreadPool(processes=2) as pool:
    for result in pool.imap(task, [1,2,3,4,5,6,7]):
        print('Get result', result)
