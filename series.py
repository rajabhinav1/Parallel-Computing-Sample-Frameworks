#SerialProgram 1
import time
start = time. perf_counter()

def see_movie():
    print ('Finding you one>.<')
    time.sleep(0.5)
    print ('Search Complete>.<')
    

see_movie()
see_movie()
see_movie()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)}second(s)')
