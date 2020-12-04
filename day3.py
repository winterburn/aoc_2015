from utils import get_input

unique_locations = set()
unique_locations.add((0,0))
location = [0, 0] 
santa_location = [0, 0]
robot_location = [0, 0]
for instruction in get_input(3):
    for idx, move in enumerate(instruction):
        if idx % 2:
            location = santa_location
        else:
            location = robot_location
        if move == '>':
           location[0] += 1
        if move == '<':
           location[0] -= 1
        if move == '^':
           location[1] += 1
        if move == 'v':
           location[1] -= 1
        unique_locations.add(tuple(location))
print(f'houses with atleast 1 present: {len(unique_locations)}')