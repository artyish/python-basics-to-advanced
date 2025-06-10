test = 15
score = -35

if test > 0 and score > 0:
    print("both are true")
else:
    print("one or both of them are false")

if test > 0 or score > 0:
    print("one or both of them are true")
else:
    print("both are false")

test_scheduled = True 

if not test_scheduled:
    print("The test has been cancelled")
else:
    print("The test is still scheduled")


# ternary operator

num = 5
variable = "positive" if num > 3 else "negative"
# do the first one if condition is true else do the second one
print(variable , type(variable))