import os

def increment(password):
    i = len(password) - 1
    while i >= 0:
        if password[i] == ord('z'):
            password[i] = ord('a')
            i -= 1
        else:
            password[i] += 1
            break
    return password

def has_increasing_straight(password):
    for i in range(len(password) - 2):
        if password[i] + 1 == password[i+1] and password[i] + 2 == password[i+2]:
            return True
    return False

def no_forbidden_letters(password):
    forbidden = {ord('i'), ord('o'), ord('l')}
    for char in password:
        if char in forbidden:
            return False
    return True

def two_non_overlapping_pairs(password):
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i+1]:
            pairs.add(password[i])
            i += 2  # Skip the next to avoid overlapping pairs
        else:
            i += 1
    return len(pairs) >= 2

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    string = file.read().strip()

print("Initial password:", string)
password = [ord(c) for c in string]

while True:
    if no_forbidden_letters(password):
        if has_increasing_straight(password):
            if two_non_overlapping_pairs(password):
                break
    password = increment(password)

new_password = "".join(chr(c) for c in password)
print("New password:", new_password)