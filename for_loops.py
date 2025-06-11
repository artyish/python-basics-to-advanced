# for x in range(0,10):
    # print(x)

# for y in reversed(range(0,10)):
    # print(y) 

# continue to skip an iteration

# break to exit the loop

import time

time_sec = int(input("Input time in seconds for timer : "))
for i in reversed(range(0,time_sec)):
    print(i)
    time.sleep(1)
print("TIMES UP!!")