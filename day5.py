from collections import defaultdict
from utils import get_input
import re

double_letters = re.compile(r"(.)\1")
vowels = re.compile(r"[aeiou]")
nice_string_count = 0
input = get_input(5)
for string in input:
    if not re.search(double_letters, string):
        continue
    if len(re.findall(vowels, string)) < 3:
        continue
    for naughty_string in ['ab', 'cd', 'pq', 'xy']:
        if naughty_string in string:
            break
    else:
        nice_string_count += 1
print(f'number of nice strings: {nice_string_count}')
new_rules_count = 0
for string in input:
    good_string = False
    for idx in range(len(string)-3):
        pair = string[idx:idx+2]
        if pair in string[idx+2:]:
            good_string = True
            break
    
    in_between = False
    for idx in range(len(string)-2):
        if string[idx] == string[idx+2]:
            in_between = True
    if all([in_between, good_string]):
        new_rules_count += 1

print(f'number of nice strings with new rules {new_rules_count}')