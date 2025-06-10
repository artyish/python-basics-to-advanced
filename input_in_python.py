# input() always returns the data as a string!

name = input("What is your name")
print(f"Hello {name}!")

age = input("What is your age? :")
print(f"You are {age} years old and the datatype is {type(age)}")
# input always returns a string

# so we should always do
age = int(input("What is your age? :"))
print(f"You are {age} years old and the datatype is {type(age)}")

# rectange area
length = float(input("Length :"))
breadth = float(input("Width :"))
area = length * breadth
print(f"The area is {area} unit²")