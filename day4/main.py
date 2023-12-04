import sys
import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
util_dir = os.path.join(parent_dir, 'util')
sys.path.append(util_dir)

from read_file import read_file

input = read_file("input.txt")

def get_matches(card):    
    numbers = card.split(':')[1].split('|')
    your_numbers = [int(n) for n in numbers[0].split(' ') if n != '']
    winning_numbers = [int(n) for n in numbers[1].split(' ') if n != '']
    return len([n for n in your_numbers if n in winning_numbers])

def get_card_winnings(card): 
    matches = get_matches(card)
    if matches == 0:
        return 0
    return pow(2, matches - 1)


def partOne():
    winnings = sum([get_card_winnings(l) for l in input])
    return winnings

def partTwo():
    init = [1 for n in input]
    for i in range(len(input)):
        matches = get_matches(input[i])
        for j in range(matches):
            init[j + 1 + i] += init[i]
    return sum(init)

if __name__ == "__main__":
    print("Part One:", partOne())
    print("Part Two:", partTwo())

