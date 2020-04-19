## Data structure tutorial exercise: Queue

For all exercises use [Queue class](https://github.com/codebasics/py/blob/master/DataStructures/6_Queue/6_queue.ipynb) implemented in main tutorial.

1. Design a food ordering system where your python program will run two threads,
    1. Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
    1. Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

    Use this video to get yourself familiar with [multithreading in python](https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=2&t=0s)

    Pass following list as an argument to place order thread,
    ```
    orders = ['pizza','samosa','pasta','biryani','burger']
    ```
    This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders.
    Use Queue class implemented in a video tutorial.

[Solution](https://github.com/codebasics/py/tree/master/DataStructures/6_Queue/Exercise/food_ordering_system.py)

2. Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial.
Binary sequence should look like,
```
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
```
Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.

[Solution](https://github.com/codebasics/py/tree/master/DataStructures/6_Queue/Exercise/binary_numbers.py)
