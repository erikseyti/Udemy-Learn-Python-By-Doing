age = 34
# print("You are " + str(age))
print(f"You are {age}")

name = "Erik"
# created once the value of greeeting with name erik
greeting = f"How are you, {name}?"
print(greeting)
name = "Bob"
# will still print "How are you, Erik?"
print(greeting)
name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)
bob_greeting = final_greeting.format("Bob")
print(bob_greeting)

print(final_greeting.format("Adastolfo Mateus"))
f_greeting = "How are you {name}?"
print(f_greeting.format(name=name))
