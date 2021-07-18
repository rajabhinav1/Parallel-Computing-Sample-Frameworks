import multiprocessing
import time
start = time.perf_counter()

def see_movie():
    print ('Finding you one>.<')
    time.sleep(0.5)
    print ('Search Complete>.<')

p1= multiprocessing.Process(target=see_movie())
p2= multiprocessing.Process(target=see_movie())
p3= multiprocessing.Process(target=see_movie())

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start,4)}second(s)')
