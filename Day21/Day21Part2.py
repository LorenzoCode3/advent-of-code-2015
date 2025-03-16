import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    input_lines = file.read().splitlines()

boss_stats = {line.split(': ')[0].replace(' ', '_').lower(): int(line.split(': ')[1]) for line in input_lines}
player_stats = {"hit_points": 100, "damage": 0, "armor": 0}

shop_data = {
    "Weapons": {
        "Dagger": {"Cost": 8, "Damage": 4, "Armor": 0},
        "Shortsword": {"Cost": 10, "Damage": 5, "Armor": 0},
        "Warhammer": {"Cost": 25, "Damage": 6, "Armor": 0},
        "Longsword": {"Cost": 40, "Damage": 7, "Armor": 0},
        "Greataxe": {"Cost": 74, "Damage": 8, "Armor": 0},
    },
    "Armor": {
        "Leather": {"Cost": 13, "Damage": 0, "Armor": 1},
        "Chainmail": {"Cost": 31, "Damage": 0, "Armor": 2},
        "Splintmail": {"Cost": 53, "Damage": 0, "Armor": 3},
        "Bandedmail": {"Cost": 75, "Damage": 0, "Armor": 4},
        "Platemail": {"Cost": 102, "Damage": 0, "Armor": 5},
    },
    "Rings": {
        "Damage +1": {"Cost": 25, "Damage": 1, "Armor": 0},
        "Damage +2": {"Cost": 50, "Damage": 2, "Armor": 0},
        "Damage +3": {"Cost": 100, "Damage": 3, "Armor": 0},
        "Defense +1": {"Cost": 20, "Damage": 0, "Armor": 1},
        "Defense +2": {"Cost": 40, "Damage": 0, "Armor": 2},
        "Defense +3": {"Cost": 80, "Damage": 0, "Armor": 3},
    },
}

def fight(player_stats, boss_stats):
    while True:
        boss_stats["hit_points"] -= max(player_stats["damage"] - boss_stats["armor"], 1)
        if boss_stats["hit_points"] <= 0:
            return "Player"
        player_stats["hit_points"] -= max(boss_stats["damage"] - player_stats["armor"], 1)
        if player_stats["hit_points"] <= 0:
            return "Boss"

def calculate_stats(items):
    cost, damage, armor = 0, 0, 0
    for item in items:
        if item is not None:
            cost += item["Cost"]
            damage += item["Damage"]
            armor += item["Armor"]
    return cost, damage, armor

# Function that generate all possible combinations of items, including no item and return the cost, damage and armor
def generate_combinations(shop_data):
    combinations = []
    for weapon in shop_data["Weapons"].values():
        for armor in [None] + list(shop_data["Armor"].values()):
            for ring1 in [None] + list(shop_data["Rings"].values()):
                for ring2 in [None] + list(shop_data["Rings"].values()):
                    if ring1 == ring2 and ring1 is not None:
                        continue
                    # Calculate stats for the current combination
                    items = [weapon, armor, ring1, ring2]
                    combinations.append(calculate_stats(items))
    return combinations

# Generate all possible combinations of items
combinations = generate_combinations(shop_data)
losing_combinations = []

# Iterate over all combinations and check if the boss wins
for combination in combinations:
    player_stats["damage"] = combination[1]
    player_stats["armor"] = combination[2]
    if fight(player_stats.copy(), boss_stats.copy()) == "Boss":
        losing_combinations.append(combination)

# Find the maximum expensive combination
print(max(losing_combinations, key=lambda x: x[0])[0])