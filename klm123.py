import multiprocessing
import time
start = time.perf_counter()

def see_movie():
    print ('Finding>.<')
    time.sleep(0)
    print ('Found You one>.<')
plays=[]
for i in range(2):
 p= multiprocessing.Process(target=see_movie(),args=[0])
p.start()
plays.append(p)


finish = time.perf_counter()

print(f'Finished in {round(finish-start,0)}second(s)')
print ('finished browsing, time to watch >.< , harry potter and the sorcerer stone')
