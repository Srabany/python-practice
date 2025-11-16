###  Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers=[1,2,3,4,5,6,7,8,9,11,2,3,12,14]
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)

    t=time.time()

    for result in results:
        print(result)

    finished_time=time.time()-t
    print(finished_time)

'''
Output:
Square: 1
Square: 4
Square: 9
Square: 16
Square: 25
Square: 36
Square: 49
Square: 64
Square: 81
Square: 121
Square: 4
Square: 9
Square: 144
Square: 196
0.002547740936279297
'''

## though the function takes 2 seconds to execute but since we are using process pool executor with 3 workers, the total time taken is significantly reduced.
