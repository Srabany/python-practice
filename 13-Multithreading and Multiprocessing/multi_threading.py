### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

'''
t=time.time()
print_numbers()
print_letter()
finished_time=time.time()-t
print(finished_time)

Output:
Number:0
Number:1
Number:2
Number:3
Number:3
Number:4
Letter: a
Letter: a
Letter: b
Letter: b
Letter: c
Letter: d
Letter: e
20.01611876487732
'''

##create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
## start the thread
t1.start()
t2.start()

### Wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)

'''
Output:
Number:0
Letter: a
Number:1
Letter: b
Number:2
Letter: c
Number:3
Letter: d
Number:4
Letter: e
10.0066556930542
'''
