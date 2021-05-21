# create a new list with multiples by 2.

numbers = [0,1,2,3,4]
doubled_numbers = []

# a more simple way with a for loop
# for number in numbers:
#     doubled_numbers.append(number *2)

# print(doubled_numbers)

# with list comprehension:
doubled_numbers = [number *2 for number in numbers]
print(doubled_numbers)

# using range of numbers:
doubled_numbers = [number *2 for number in range(5)]
print(doubled_numbers)

# You can use any number on the parameter that will be in the for loop of the list comprehension
# obviously the word number is not used, in this context
doubled_numbers = [5 for number in range(5)]
# In cases like this you can see programmers using a _ on the name of the variable
# doubled_numbers = [5 for _ in range(5)]
print(doubled_numbers)