nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friend = input("type the name of one friend you have: ")

# Add the name to the empty set
friend_set  = {friend}
# print(friend_set)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
nearby_friends = nearby_people.intersection(friend_set)
print(nearby_friends)