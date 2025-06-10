name = "this is a string"

# result = len(name)
# result = name.find(" ") # we start with 0 while indexing
# result = name.rfind(" ") # reverse occurence (last)

# result = name.capitalize() # only capitalizes first word
# result = name.upper()
# result = name.lower()

# result = name.isdigit() # true only when only digits
# result = name.isalpha() # only alphabets no spaces no digits
# result = name.count("i") # no. of i's in the string

# result = name.replace(" ","") # replace all occurences of blank with no space or any character with any other character
# print(result)

print("Input a valid username (no spaces, no digits, less than 12 characters)")

username = input("Enter your username: ")
if(username.find(" ") != -1):
    print(f"There is a space in your username at index {username.find(' ')}")
elif(len(username) > 12):
    print("Username cannot be more than 12 characters")
elif(username.isalpha() == False):
    print("Username contains digits or special characters")
else:
    print("Username saved successfully!")
    print(f"Welcome {username}")
