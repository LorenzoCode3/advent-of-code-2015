import os

# Define spell details as a constant dictionary
SPELLS = {
    'Magic Missile': {'cost': 53, 'damage': 4},
    'Drain': {'cost': 73, 'damage': 2, 'heal': 2},
    'Shield': {'cost': 113, 'duration': 6, 'armor': 7},
    'Poison': {'cost': 173, 'duration': 6, 'damage': 3},
    'Recharge': {'cost': 229, 'duration': 5, 'mana': 101}
}

def solve(boss_stats, player_stats):
    # Simulate the combat using a DFS search to minimize mana spent
    # Returns the minimum mana spent to win
    boss_hp = boss_stats.get('Hit Points', 0)
    boss_damage = boss_stats.get('Damage', 0)
    player_hp = player_stats.get('Hit Points', 0)
    player_mana = player_stats.get('Mana', 0)
    best_mana = float('inf')

    def dfs(player_hp, player_mana, boss_hp,
            shield_timer, poison_timer, recharge_timer,
            mana_spent, player_turn):
        
        nonlocal best_mana

        # At the start of each player's turn, 1 hit point is lost
        if player_turn:
            player_hp -= 1
            if player_hp <= 0:
                return

        # Prune paths that have already exceeded best solution
        if mana_spent >= best_mana:
            return

        # Apply active effects at the start of the turn
        armor = 7 if shield_timer > 0 else 0
        if poison_timer > 0:
            boss_hp -= SPELLS['Poison']['damage']
        if recharge_timer > 0:
            player_mana += SPELLS['Recharge']['mana']

        # Decrement effect timers
        shield_timer = max(0, shield_timer - 1)
        poison_timer = max(0, poison_timer - 1)
        recharge_timer = max(0, recharge_timer - 1)

        # Check if boss is defeated by effects
        if boss_hp <= 0:
            best_mana = min(best_mana, mana_spent)
            return

        if player_turn:
            # Try every spell for the player's turn
            for spell_name, details in SPELLS.items():
                cost = details['cost']
                # Skip if not enough mana
                if player_mana < cost:
                    continue
                # Prevent recasting spells that have ongoing effects
                if spell_name == 'Shield' and shield_timer > 0:
                    continue
                if spell_name == 'Poison' and poison_timer > 0:
                    continue
                if spell_name == 'Recharge' and recharge_timer > 0:
                    continue

                # Copy current state for simulation
                next_player_hp = player_hp
                next_player_mana = player_mana - cost
                next_boss_hp = boss_hp
                next_shield_timer = shield_timer
                next_poison_timer = poison_timer
                next_recharge_timer = recharge_timer
                next_mana_spent = mana_spent + cost

                # Apply immediate effects
                if spell_name == 'Magic Missile':
                    next_boss_hp -= details['damage']
                elif spell_name == 'Drain':
                    next_boss_hp -= details['damage']
                    next_player_hp += details['heal']
                elif spell_name == 'Shield':
                    next_shield_timer = details['duration']
                elif spell_name == 'Poison':
                    next_poison_timer = details['duration']
                elif spell_name == 'Recharge':
                    next_recharge_timer = details['duration']

                # Next turn is the boss's turn
                dfs(next_player_hp, next_player_mana, next_boss_hp,
                    next_shield_timer, next_poison_timer, next_recharge_timer,
                    next_mana_spent, player_turn=False)
        else:
            # Boss turn: Boss deals damage considering player's armor
            damage = max(1, boss_damage - armor)
            player_hp -= damage
            if player_hp <= 0:
                return  # Player defeated, end this branch
            # Continue with player's turn
            dfs(player_hp, player_mana, boss_hp,
                shield_timer, poison_timer, recharge_timer,
                mana_spent, player_turn=True)

    # Start the simulation with initial player stats
    dfs(player_hp=player_hp, player_mana=player_mana, boss_hp=boss_hp,
        shield_timer=0, poison_timer=0, recharge_timer=0,
        mana_spent=0, player_turn=True)
    return best_mana

filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(filepath, 'r') as file:
    lines = file.read()

boss_stats = {line.split(': ')[0]: int(line.split(': ')[1]) for line in lines.split('\n')}
player_stats = {'Hit Points': 50, 'Mana': 500}

print(solve(boss_stats, player_stats))