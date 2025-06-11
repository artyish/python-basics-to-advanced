# print("Do you agree?")

# choice = input()

# while choice != "Yes":
    # print("You need to agree")
    # choice = input()

choice = input("Enter your favourite food (q to quit): ")
stash = []

while not choice == "q":
    stash.append(choice)
    choice = input("Enter your favourite food (q to quit): ")

print(stash)