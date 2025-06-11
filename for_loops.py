# for x in range(0,10):
    # print(x)

# for y in reversed(range(0,10)):
    # print(y) 

# continue to skip an iteration

# break to exit the loop

# import time

# time_sec = int(input("Input time in seconds for timer : "))
# for i in reversed(range(0,time_sec)):
    # print(i)
    # time.sleep(1)
# print("TIMES UP!!")

# nested for loops

j = int(input("Input the number of rows : "))
i = int(input("Input the number of columns : "))
character = input("Input character of your liking : ")

for x in range(0 , i):
    print()
    for y in range(0 , j):
        if(x == 0 or y == 0) :
            print(character,end="")
        elif(x == (i-1) or y == (j-1)):
            print(character,end="")
        else:
            print(" ",end="")

    