friend = "Rolf"

user_name = input("Enter your name:")

if user_name == friend:
    print("Hello, Friend !!")
    print("This runs too")
else:
    print("Hello Stranger !")

print("This runs anyways")

# value is always True
print(bool(5))
# value is always False
print(bool(0))

# always be True
if 5:
    print("Runs")