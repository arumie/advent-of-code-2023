

import sys
import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
util_dir = os.path.join(parent_dir, 'util')
sys.path.append(util_dir)

from read_file import read_file

def parse_line(s, previous_line, next_line, symbols):
    numbers = [int(m.group()) for m in re.finditer(r'\d+', s) if find_symbol(s, m.group(), m.start(), m.end(), previous_line, next_line, symbols) ]
    return numbers

def find_symbol(s, num, start_index, end_index, previous_line, next_line, symbols):
    previous_res = False
    next_res = False
    if previous_line is not None:
        previous_res = look_for_symbol(previous_line, start_index, end_index, symbols)
    if next_line is not None:
        next_res = look_for_symbol(next_line, start_index, end_index, symbols)
    neighbour_res = match_neighbours(s, start_index, end_index, symbols)
    res = previous_res or next_res or neighbour_res
    if (res == False):
        print (num, previous_res, next_res, neighbour_res, res)
        s_idx = start_index - 1 if start_index != 0 else start_index;
        e_idx = end_index + 1 if end_index != len(s) - 1 else end_index;
        if (previous_line is not None):
            print (previous_line[s_idx:e_idx])
        print (s[s_idx:e_idx])
        if (next_line is not None):
            print (next_line[s_idx:e_idx])
    return res


def match_neighbours(s, start_index, end_index, symbols):
    s_idx = start_index - 1 if start_index != 0 else start_index;
    e_idx = end_index + 1 if end_index != len(s) - 1 else end_index;
    str = s[s_idx:e_idx];
    for symbol in symbols:
        if symbol in str:
            return True
    return False

def look_for_symbol(line, start_index, end_index, symbols):
    s_idx = start_index - 1 if start_index != 0 else start_index;
    e_idx = end_index + 1 if end_index != len(line) - 1 else end_index;
    for val in line[s_idx:e_idx]:
        if val in symbols:
            return True
    return False

def find_gear(s, previous_line, next_line):
    prev_num_pairs = []
    next_num_pairs = []
    current_num_pairs = [(int(m.group()), m.start(), m.end() - 1) for m in re.finditer(r'\d+', s )]
    if previous_line is not None:
        prev_num_pairs = [(int(m.group()), m.start(), m.end() - 1) for m in re.finditer(r'\d+', previous_line )]
    if next_line is not None:
        next_num_pairs = [(int(m.group()), m.start(), m.end() - 1) for m in re.finditer(r'\d+', next_line )]
    
    potential_gears = [(m.start() - 1, m.end()) for m in re.finditer(r'\*', s)]
    print ('----------------')
    print (potential_gears)
    print (prev_num_pairs)
    print (current_num_pairs)
    print (next_num_pairs)
    gears = []
    for gear_start, gear_end in potential_gears:
        adjacent_numbers = []
        for num, num_start, num_end in prev_num_pairs:
            if (gear_start <= num_start <= gear_end or gear_start <= num_end <= gear_end):
                adjacent_numbers.append(num)
        for num, num_start, num_end in current_num_pairs:
            if (gear_start <= num_start <= gear_end or gear_start <= num_end <= gear_end):
                adjacent_numbers.append(num)
        for num, num_start, num_end in next_num_pairs:
            if (gear_start <= num_start <= gear_end or gear_start <= num_end <= gear_end):
                adjacent_numbers.append(num)
        print('adjacent_numbers', adjacent_numbers)
        if (len(adjacent_numbers) == 2):
            gears.append(adjacent_numbers[0] * adjacent_numbers[1])
    print ("gears", gears)
    print ('----------------')
    return sum(gears)


def partOne():
    input = read_file("input.txt")
    symbols = set(re.findall(r'\D', ''.join(input)))
    symbols.discard('.')
    result = [sum(parse_line(line, (input[i-1] if i != 0 else None), (input[i+1] if i != len(input)-1 else None), symbols)) for i, line in  enumerate(input)]
    print (result)
    return sum(result)

def partTwo():
    input = read_file("input.txt")
    result = [find_gear(line, (input[i-1] if i != 0 else None), (input[i+1] if i != len(input)-1 else None)) for i, line in  enumerate(input)]
    return sum(result)

if __name__ == "__main__":
    print(partTwo())

