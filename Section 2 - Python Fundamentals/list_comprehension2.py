friends_ages = [22,31, 35, 37]
# create a lists with a string attached to the value your friends ages.
ages_strings = [f"My friend is {age} years old." for age in friends_ages]
print(ages_strings)

# transform which name on the list to lowercase.
names = ['Rolf', 'Bob', 'Jen']
lower = [name.lower() for name in names]
print(lower)