import requests
import json
def get_input(day):
    with open('./config.json', 'r') as f:
        config = json.load(f)
    input = requests.get(f'https://adventofcode.com/2015/day/{day}/input',
                         cookies={'session': config.get('session')})
    return input.text.split('\n')