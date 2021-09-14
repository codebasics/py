import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)
        #time, sleep function is used to add delay in the execution of a program.
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(1)
        print('cube:',n*n*n)

arr = [2,3,8,9]
#time.time() returns the time as a floating point number expressed in seconds since the epoch, in UTC.
t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
