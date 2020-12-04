from utils import get_input

current_floor = 0
first_to_basement = 0
for idx, letter in enumerate(get_input(1)[0]):
    if letter == '(':
        current_floor += 1
    elif letter == ')':
        if current_floor == -1 and first_to_basement == 0:
            first_to_basement = idx
        current_floor -= 1
print(current_floor)
print(f'first to basement at {first_to_basement}')