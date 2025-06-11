# [] list
# {} set
# () tuple

# fruit_bowl = ['apple','banana','pear','grapes']
# print(fruit_bowl)
# for fruit in fruit_bowl:
    # print(fruit,end=" ")
# print()


# print("apple" in fruit_bowl)

# fruit_bowl.append("orange")
# print(fruit_bowl)
# fruit_bowl.remove("orange")
# print(fruit_bowl)
# fruit_bowl.insert(0,"orange")
# print(fruit_bowl)
# fruit_bowl.sort()
# print(fruit_bowl)

# print(fruit_bowl.index("grapes"))

# sets are unordered hence we cant do indexing

# fruit_bowl = {'apple','banana','pear','grapes'}
# fruit_bowl.add('apple') # does not add because duplicates arent allowed
# print(fruit_bowl)

# fruit_bowl.add('testing')
# print(fruit_bowl)

# fruit_bowl.remove('testing')
# print(fruit_bowl)

# fruit_bowl.pop() # remove first
# print(fruit_bowl)

cart = []
bill_list = []
flag = True

while flag == True:
    food_name = input("Input a food to buy (Or q to exit) : ")
    if food_name == 'q':
        break
    cart.append(food_name)
    price = float(input("Input price for that food : "))
    bill_list.append(price)

total_sum = 0
for i in range(len(cart)):
    print(f"Food Name: {cart[i]} & Price : ${bill_list[i]}")
    total_sum += bill_list[i]

print(f"Your total bill is ${total_sum}")