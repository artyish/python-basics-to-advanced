# basic print command
print("Hello World!")

# basic f-string command with variable
variable = "Guys!"
print(f"Hello {variable}")

age = 18
print(f"I am {age} years old!")

float_price = 3.99
print(f"This fruit costs ${float_price}")

# anything that is not a zero is considered TRUE even -ve values!
boolean_student = -1

if boolean_student:
    print(f"Yes I am a student : {boolean_student}")
else:
    print(f"No you are not a student")

# typecasting (one datatype ---> to another)
name = "Hemank"
age = 18
is_student = True
balance = 10.5

print(type(name), type(age), type(is_student), type(balance))
# on using 1 as is_student the datatype will be integer!

age_str = str(age)
balance_str = str(balance)
# using string concatenation 18 + 10.5 = 1810.5
print(age_str+balance_str)

balance_int = int(balance)
print(balance_int) # returns the floor value of float