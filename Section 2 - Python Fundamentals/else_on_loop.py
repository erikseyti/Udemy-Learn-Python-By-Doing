cars = ["ok", "ok", "ok", "ok"]

# Exemplo onde caso encontrado um carro defeituoso o Loop é parado.
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}")
    print("Shipping new car to customer!")
else:
    print("All cars built sucessfully. No fault cars!")