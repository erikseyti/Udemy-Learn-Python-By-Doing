primeList = []
numberChecked = int(input("Whats is the max number you want to check if is prime?"))

for n in range(2,numberChecked):
    for x in range(2,n):
        if n % x ==0:
            print(f"{n} equals {x} * {n/x}")
            break
    else:
        print(f"{n} is a prime number.")
        primeList.append(n)

print(f"This is the list of prime numbers find: {primeList}")