# functions

# def say_happy_birthday(name,age):
#     print("Happy Birthday to you!")
#     print(f"Happy Birthday! {name}")
#     print(f"You are {age} years old")
#     print()

# say_happy_birthday("Adi",18)
# say_happy_birthday("Steve",19)
# say_happy_birthday("Alex",20)

# x ---------------- return statements ---------------- x

# def poweroftwo(num):
#     return pow(num,2)

# squared = poweroftwo(5)
# print(squared)

# x ---------------- default arguments ---------------- x

def final_price(price,discount=0,tax=0.08):
    return price*(1-discount)*(1+tax)

print(final_price(100))
print(f"{final_price(100,0.23,0.05):.2f}🐍")  