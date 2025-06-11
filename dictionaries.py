# # dictionary {key: value} pairs

# favourite_food = {"Hemank" : "Butter Chicken",
#                   "Bhaiya" : "Pizza",
#                   "Papa" : "Chole Bhature"}

# print(favourite_food.get("Hemank")) # Hemank here is key and my value is But. Chkn.
# # None returned if not found

# if favourite_food.get('NotInDictionary'): # true if found None if not found goes to the else statement
#     print("Found!")
# else:
#     print("Not found in this dictionary!")

# favourite_food.update({"Mummy" : "Chai"})
# print(favourite_food)

# # .pop("key_name") to remove that key : value pair 
# # .pop item will remove the latest one
# # .clear will clear the whole dictionary

# # get all keys (no values) dictionary.keys

# keys = favourite_food.keys()
# print(keys)
# values = favourite_food.values()
# print(values)


# # for both key values dictionary.items() returns a 2d tuple

# for key, values in favourite_food.items():
#     print(f"{key} : {values}")

menu = {}
while True:
    food_item = input("Input Food Item (q to quit) :")

    if food_item == 'q':
        break

    price = input("Price :$")

    menu.update({food_item : price})

for key , value in menu.items():
    print(f"{key:7} : ${value}")