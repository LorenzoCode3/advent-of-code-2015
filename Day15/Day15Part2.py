import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

def generate_combinations(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for combo in generate_combinations(total - i, parts - 1):
                yield (i,) + combo

def calculate_score(combination, ingredients, names):
    scores = {'capacity': 0, 'durability': 0, 'flavor': 0, 'texture': 0, 'calories': 0}
    for i in range(len(combination)):
        for key in scores:
            scores[key] += combination[i] * ingredients[names[i]][key]
    for key in scores:
        scores[key] = max(0, scores[key])
    return scores

teaspoons = 100
names = []
ingredients = dict()

for line in lines.splitlines():
    line = line.replace(': capacity', '').replace(', durability', '').replace(', flavor', '').replace(', texture', '').replace(', calories', '')
    (name, capacity, durability, flavor, texture, calories) = line.split()
    capacity, durability, flavor, texture, calories = map(int, (capacity, durability, flavor, texture, calories))
    names.append(name)
    ingredients.setdefault(name, dict({'capacity': capacity, 'durability': durability, 'flavor': flavor, 'texture': texture, 'calories': calories}))

highest_score = 0

for combination in generate_combinations(teaspoons, len(ingredients.items())):
    scores = calculate_score(combination, ingredients, names)
    
    if scores['calories'] == 500:
        score = scores['capacity'] * scores['durability'] * scores['flavor'] * scores['texture']
        if score > highest_score:
            highest_score = score

print(highest_score)