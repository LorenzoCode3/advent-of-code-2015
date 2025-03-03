import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    string = file.read()

def look_and_say(sequence, iterations):
    for i in range(iterations):
        count = 1
        previous_char = sequence[0]
        new_string = ''
        for char in sequence[1:]:
            if char == previous_char:
                count += 1
            else:
                new_string = new_string + (f'{count}{previous_char}')
                previous_char = char
                count = 1
        new_string = new_string + (f'{count}{previous_char}')
        sequence = new_string
    return sequence

print(len(look_and_say(string, 40)))