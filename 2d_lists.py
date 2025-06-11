# good for things like grid // excel sheets

# fruits = ['apple','banana','grapes']
# vegetables = ['carrot','plant']
# meats = ['chicken','turkey','fish','egg']

# groceries = [fruits,vegetables,meats]

# # print(groceries)
# for grocery_type in groceries:
#     print()
#     for grocery in grocery_type:
#         print(grocery,end=" ")


keypad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ('*',0,'#'))

for row in keypad:
    for numbers in row:
        print(numbers,end=' ')
    print()