import time
from random import randint
import threading

queue = []

def produce():
    for i in range(0,5):
        time.sleep(1)
        queue.append(randint(0,9))

def consume():
    while True:
        if len(queue) > 0:
            

if "__name__"=="__main__":
    p = threading.Thread(target=produce)
    c = threading.Thread(target=consume)

