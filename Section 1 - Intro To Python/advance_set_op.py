# Advance set operations on Sets.

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)

science_but_not_art = science_friends.difference(art_friends)

print(f"art_but_not_science: {art_but_not_science}")
print(f"science_but_not_art: {science_but_not_art}")

not_in_both_friends = art_friends.symmetric_difference(science_friends)
print(f"not_in_both_friends: {not_in_both_friends}")

art_and_science_friends = art_friends.intersection(science_friends)
print(f"art_and_science_friends: {art_and_science_friends}")

all_friends = art_friends.union(science_friends)
print(f"all_friends: {all_friends}")