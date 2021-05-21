friend = input('Enter Your friend name:')
friends = ['Rolf', 'Bob', 'Jen', 'Charlie', 'Anne']
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    # upper case for each letter of the name, and lower case by the rest.
    friend_title_cased = friend.title()
    print(f'{friend_title_cased} is one your friends.')