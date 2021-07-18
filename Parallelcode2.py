#Looping with for loop and list while initiating 12 processor engagements
import multiprocessing
import time
start = time.perf_counter()

def see_movie():
    print ('Finding you one>.<')
    time.sleep(1)
    print ('Search Complete>.<')
plays=[]
for i in range(12):
 p= multiprocessing.Process(target=see_movie())
p.start()
plays.append(p)


finish = time.perf_counter()

print(f'Finished in {round(finish-start,4)}second(s)')
