import math
x = 3.14
y = -4.13
z = 5.0

var = round(x)
var = abs(y) # returns absolute value with decimal if there is
var = max(x, y, z) # returns maximum value
var = pow(3,3) # 3 to the power of 3
print(var)

print(math.pi) # for the value of pi

print(math.sqrt(9)) # returns sqrt in float

print(math.ceil(x)) # rounded up

print(math.floor(x)) # rounded down

print(round(math.pi,3)) # round float value upto 3 decimal places

# input A and B
a = float(input("Input Side A :"))
b = float(input("Input Side B :"))
hyp = math.sqrt(math.pow(a,2)+math.pow(b,2))
print(f"The side C is : {round(hyp,3)}")