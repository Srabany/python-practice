### Multithreading With Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number}"

numbers=[1,2,3,4,5,6,7,8,9,0,1,2,3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number,numbers)

t=time.time()

for result in results:
    print(result)

finished_time=time.time()-t
print(finished_time)

'''
Output:
Number :1
Number :2
Number :3
Number :4
Number :5
Number :6
Number :7
Number :8
Number :9
Number :0
Number :1
Number :2
Number :3
0.0027060508728027344
'''

## though we put sleep of 1 second but as we are using thread pool executor with max_workers=3 that's why it took very less time to complete the task
