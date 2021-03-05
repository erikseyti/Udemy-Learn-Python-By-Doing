friend1 = "Rolf"
friend2 = "Bob"
friend3 = "Anne"

print(friend1)

friends = ["Rolf", "Bob", "Anne"]
friends_and_age = [["Rolf", 22], ["Bob", 32], ["Anne", 19]]

print(friends[0])
print(len(friends))
# get first list on list of lists
print(friends_and_age[0])
# get first value of a list of lists
print(friends_and_age[0][0])
# apend a new registry on the list
friends.append("Angustus")
print(friends)
# remove a elemement its value
friends.remove("Bob")
print(friends)
# In case of multiple values within a list (a complete list within another list)
# needs to the full value of the registry
friends_and_age.remove(["Anne", 19])
print(friends_and_age)

