friends_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

print("nome dos seus amigos (key):")
for name in friends_ages:
    print(name)

print("Idade dos seus amigos (value):")
for age in friends_ages.values():
    print(age)

print("Nome e idade dos seus amigos (key, value)")
for name, age in friends_ages.items():
    print(f"{name} is {age} years old.")