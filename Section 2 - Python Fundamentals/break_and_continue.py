cars = ["ok", "ok", "faulty", "ok", "ok"]

# Exemplo onde caso encontrado um carro defeituoso o Loop é parado.
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}")
    print("Shipping new car to customer!")

# Exemplo onde caso encontrado um carro defeituoso o Loop, informa pelo log o veiculo defeituoso
# e skipa para o proximo carro
for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue
    print(f"This car is {status}")
    print("Shipping new car to customer!")