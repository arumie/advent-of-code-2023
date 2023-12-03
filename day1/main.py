

import sys
import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
util_dir = os.path.join(parent_dir, 'util')
sys.path.append(util_dir)

from read_file import read_file

def find_first_last_digits(s):
    # Regular expression for numeric digits
    digits = re.findall(r'\d+', s)

    # Mapping of number words to digits
    word_to_num = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    reversed_word_to_num = {k[::-1]: v for k, v in word_to_num.items()}
    regex = r'\d|' + '|'.join(word_to_num.keys())
    b_regex = r'\d|' + '|'.join(reversed_word_to_num.keys())
    print(regex)
    print(b_regex)

    # Convert words to digits
    first_digit = re.search(regex, s).group()
    last_digit = re.search(b_regex, s[::-1]).group()[::-1]




    print(first_digit)
    print(last_digit)
    # Convert list of strings to list of int

    return (first_digit if first_digit.isdigit() else word_to_num[first_digit]) + (last_digit if last_digit.isdigit() else word_to_num[last_digit])

def partOne():
    input = read_file("input.txt")
    firstdigits = [re.search(r'\d', line).group() for line in input]
    lastdigits = [re.findall(r'\d', line)[-1] for line in input]
    combined = [ int(pair[0] + pair[1]) for pair in list(zip(firstdigits, lastdigits))]
    sum_ = sum(combined)
    return sum_

def partTwo():
    input = read_file("input.txt")
    digits = [int(find_first_last_digits(line)) for line in input]
    sum_ = sum(digits)
    [print(digits[i], input[i]) for i in range(0, len(input))]
    return sum_

if __name__ == "__main__":
    print(partTwo())

