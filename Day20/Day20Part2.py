import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    line = file.read()

def sum_of_divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if (n // i) <= 50:
                total += i
            if i != (n // i) and (n // (n // i)) <= 50:
                total += (n // i)
    return total

threshold = int(line)
house = 1

while True:
    presents = 11 * sum_of_divisors(house)
    if presents >= threshold:
        break
    house += 1

print(house)