# Calculator
import math 
a = int(input("Enter a :"))
b = int(input("Enter b :"))
print("Input your choice: 1.Addition 2.Subtraction 3.Multiplication 4.Power 5.Division")
choice = int(input("Your choice : "))

if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice == 4:
    print(a**b)
elif choice == 5:
    print(a/b)
