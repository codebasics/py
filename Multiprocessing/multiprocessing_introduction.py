import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        time.sleep(0.5) ##Putting Cpu in ideal mode while this program will sleep 0.5s. then calc_cube will be running.
        print("Square of {} is {}".format(n,n**2))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.5) ##Putting Cpu in ideal mode while this program will sleep 0.5s. then calc_Square will be running.
        print("Cube of {} is {}".format(n,n**3))

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")
