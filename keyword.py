# def firstsecondthird(first,second,third):
#     print(f"{first}, {second}, {third}")

# firstsecondthird(second = "second", first= "first", third= "third")

# to expect a varying amount of arguments
# we use *args and **kwargs
# args --> arguments, kwargs --> keyword arguments

# def add(*args): # we can name args anything we like as well! like we can write *names *nums etc etc.
#     print(type(args))
#     summation = 0
#     for arg in args:
#         summation += arg
#     print(summation)

# add(1,2,3,4)

def favourite_food(**foods):
    for name ,value in foods.items():
        print(f"{name:7} : {value}")

favourite_food(Hemank="Butter Chicken",
               Bhaiya="Pizza",
               Mummy ="Egg Biryani",
               Papa  ="Fish Curry")