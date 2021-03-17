friend_ages = {"Rolf":24, "Adam": 30, "Anne": 27}

print(f"Rolf's Age is {friend_ages['Rolf']}")

# add Value on dicionary
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25
print(f"Friend's dictionary age: {friend_ages}")

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wolfe", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

# transform a list of tuples in a dictionary.
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friends_ages = dict(friends)
print(friend_ages)