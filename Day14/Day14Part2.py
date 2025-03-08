import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

time = 0
race_time = 2503

raindeers = dict()

for line in lines.splitlines():
    line = line.replace(' seconds.', '').replace(' seconds, but then must rest for', '').replace(' can fly', '').replace(' km/s for', '')
    (name, speed, fly_time, rest_time) = line.split()
    speed, fly_time, rest_time = map(int, (speed, fly_time, rest_time))
    raindeers.setdefault(name, dict({'speed': speed, 'fly_time': fly_time, 'rest_time': rest_time, 
                                'is_resting': False, 'endurance': fly_time, 'distance_traveled': 0, 'resting_time': 0, 'points': 0}))

while time < race_time:
    for raindeer in raindeers.values():
        #print(raindeer)
        if not raindeer['is_resting']:
            raindeer['distance_traveled'] += raindeer['speed']
            raindeer['endurance'] -= 1
            if raindeer['endurance'] == 0:
                raindeer['is_resting'] = True
                raindeer['resting_time'] = raindeer['rest_time']
        else:
            raindeer['resting_time'] -= 1
            if raindeer['resting_time'] == 0:
                raindeer['is_resting'] = False
                raindeer['endurance'] = raindeer['fly_time']

    lead_distance = 0
    for raindeer in raindeers.values():
        if raindeer['distance_traveled'] > lead_distance:
            lead_distance = raindeer['distance_traveled']
    for raindeer in raindeers.values():
        if raindeer['distance_traveled'] == lead_distance:
            raindeer['points'] += 1

    time += 1

winner_points = 0
for raindeer in raindeers.values():
    if raindeer['points'] > winner_points:
        winner_points = raindeer['points']

print(winner_points)