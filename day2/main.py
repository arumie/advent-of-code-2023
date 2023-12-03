

import sys
import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
util_dir = os.path.join(parent_dir, 'util')
sys.path.append(util_dir)

from read_file import read_file

def partOne_parse_game(s):
    game_id = int(s.split(':')[0].split(' ')[1]);
    blue = sorted([int(blue.split(' blue')[0]) for blue in re.findall(r'\d+ blue', s)])[-1] <=  14
    green = sorted([int(green.split(' green')[0]) for green in re.findall(r'\d+ green', s)])[-1]  <= 13
    red = sorted([int(red.split(' red')[0]) for red in re.findall(r'\d+ red', s)])[-1] <= 12
    # print ('GAME ', game_id, 'blue:', blue, 'green:', green, 'red:', red)
    return game_id if blue and green and red else 0

def partTwo_parse_game(s):
    game_id = int(s.split(':')[0].split(' ')[1]);
    blue = sorted([int(blue.split(' blue')[0]) for blue in re.findall(r'\d+ blue', s)])[-1]
    green = sorted([int(green.split(' green')[0]) for green in re.findall(r'\d+ green', s)])[-1]
    red = sorted([int(red.split(' red')[0]) for red in re.findall(r'\d+ red', s)])[-1]
    # print ('GAME ', game_id, 'blue:', blue, 'green:', green, 'red:', red)
    return blue * green * red

def partOne():
    input = read_file("input.txt")
    print (input)
    result = sum([partOne_parse_game(line) for line in input])
    return result

def partTwo():
    input = read_file("input.txt")
    print(input)
    result = [partTwo_parse_game(line) for line in input]
    print(result)
    return sum(result)

if __name__ == "__main__":
    print(partTwo())

