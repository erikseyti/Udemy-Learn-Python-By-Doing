age = int(input("Enter your age: "))
can_learn_programming =  age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}")
usually_working = age >=18 and age <= 65
print(f"At {age}, you are usually working: {usually_working}")

# some values in Python when convert to Python, evaluates to False ("" and 0)
# but remain vallues are True
print(bool(0))
print(bool("Biscoito"))

# Verify is one of the values are False, if any of them, bring the False value
x = 0 and 35
y = 35 and 0
print(x, y)

# Verify what value is True, if any of them, will bring you the True or first value
x = 0 or 35
y = 35 or 0
print(x, y)

# will print Mr.Smith because the name in this case is empty.
name = ""
surname = "Smith"
greeting = name or f"Mr. {surname}"
print(greeting)

name = input("Enter your name: ")
surname = input("Enter your surname: ")
greeting = name or f"Mr. {surname}"
print(greeting)

print(not True)
print(not False)
