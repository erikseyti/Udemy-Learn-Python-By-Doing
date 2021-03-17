friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

name = input("Enter your name: ")

print(bool(name))

# always verify is a name is declared by the user.
if name:
    print(f"We know your name, {name}")

if name in friends:
    print("Hello Friend")

elif name in family:
    print("Hello Family")
else:
    print("I Don't Know you")
