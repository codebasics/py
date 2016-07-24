import time
import multiprocessing

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(20)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(20)
        print('cube:',n*n*n)

if __name__ == "__main__":
    arr = [2,3,8,9]

    t = time.time()

    p1= multiprocessing.Process(target=calc_square, args=(arr,))
    # p2= multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()

    print("done in : ",time.time()-t)
    print("Hah... I am done with all my work now!")