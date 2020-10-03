# Multiprocessing Pool

from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for i in n:
        sum += i
    return sum

if __name__ == "__main__":
    n = 10000000

    t1 = time.time()
    p = Pool(processes=3)

    # map(function_name,iterable data_variable)
    result = p.map(f,[range(n)])
    p.close()
    p.join()

    print('Pool took time =',time.time()-t1)

    t2 = time.time()
    sum = 0
    for i in range(n):
        sum += i
    
    print('Serial Processing took time =',time.time()-t2)

