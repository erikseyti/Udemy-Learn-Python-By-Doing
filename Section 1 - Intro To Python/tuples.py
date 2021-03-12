short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "Bob")

tuple_in_list = [("Rolf", "Bob")]
not_a_tuple = "Rolf"

friends = ("Rolf", "Bob", "Anne")

# will generate an error because Tuples cannot be change.
# friends.append("Jen")

friends = friends + ("Jen",)
print(friends)