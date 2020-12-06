import numpy as np
from utils import get_input

lights = np.zeros((1000, 1000))
def decode_input(input):
    split = input.split(' ')
    cmd = split[0]
    if cmd == 'toggle':
        x, y = split[1].split(',')
        coord1 = [int(x), int(y)]
        x, y = split[3].split(',')
        coord2 = [int(x), int(y)]
    elif cmd == 'turn':
        cmd = split[1]
        x, y = split[2].split(',')
        coord1 = [int(x), int(y)] 
        x, y = split[4].split(',')
        coord2 = [int(x), int(y)] 
    else:
        return None, None, None
    return cmd, coord1, coord2

def visualize_lights():
    for row in lights:
        for column in row:
            if column:
                print(chr(219), end='')
            else:
                print('.', end='')
        print('\n')

for row in get_input(6):
    cmd, coord1, coord2 = decode_input(row)
    if cmd == 'toggle':
        lights[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] += 2
    elif cmd == 'on':
         lights[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] += 1
    elif cmd == 'off':
        for idx, row in enumerate(lights[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1]):
            for column in range(len(row)):
                if lights[coord1[0] + idx][coord1[1] + column] > 0:
                    lights[coord1[0] + idx][coord1[1] + column] -= 1
         
print(lights.sum())
