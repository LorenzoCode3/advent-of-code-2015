import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    line = file.read()

def sum_of_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)

threshold = int(line)
house = 1

while True:
    presents = 10 * sum_of_divisors(house)
    if presents >= threshold:
        break
    house += 1

print(house)