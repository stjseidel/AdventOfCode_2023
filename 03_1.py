# -*- coding: utf-8 -*-\
"""


You can also [Share] this puzzle.
@author: stjse
"""
from timeit import default_timer as timer
from pathlib import Path
import pandas as pd
import csv
import string
import numpy as np
import matplotlib.pyplot as plt
import re
import math
start = timer()
source = Path('03_1_input_1.txt')

abc = list(string.ascii_lowercase)
ABC = list(string.ascii_uppercase)
letters = abc + ABC
digits = string.digits
# 1
with open(source) as fp:
    lines = fp.readlines()
lines = [line.replace('\n', '') for line in lines]
pattern = re.compile('\d+\.[.\d]+')
# =============================================================================
# numbers = [str(''.join(filter(str.isdigit, line))) for line in lines]
# summed = 0
# for num in numbers:
#     if len(num) == 0:
#         pass
#     elif len(num) == 1:
#         summed += int(num + num)
#     else: 
#         summed += int(num[0] + num[-1])
#     print(num, summed)
# =============================================================================

lines2 =  [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
    ]

# lines = lines2
all_str = set(''.join(lines))
all_symbols = set([c for c in all_str if not c in digits and not c == '.'])
# all_symbols = set([c for line in lines for c in line  if c not in ([str(i) for i in range(10)] + ['.'])])
# lines = lines2
def get_numbers(line):
    numbers = {}
    num = ''
    start = -1
    end = ''
    numbing = False
    for i, c in enumerate(line):
        if c in digits:
            numbing = True
            num += c
            if start == -1:
                start = i
            end = i + 1
        elif numbing:
            numbers[(int(num), start)] = (start, end)
            numbing = False
            start = -1
            end = ''
            num = ''
    if numbing:
        if not (int(num), start) in numbers.keys():
            numbers[(int(num), start)] = (start, end)
            
            
    # if numbing and num not in numbers.keys():
    #     numbers[int(num)] = (start, end)
    # elif numbing and num in numbers.keys():
    #     if start != numbers[int(num)][0]:
    #         numbers[str(num)] = (start, end)
            
    return numbers

detected = []
failed = {}
def checkline(line, idxs, row_num):
    if type(idxs) == list:
        idxs = idxs[0]
    start, end = idxs[0], idxs[1]
    if row_num not in failed.keys():
        failed[row_num] = []
    # if start == 0 or end >= len(line):
    #     print(line)
    start = max(0, start - 1)
    end = min(end + 1, len(line))
    
    rowsstart = max(0, row_num - 1)
    rowsend = min(row_num + 2, len(lines))
    for line_to_check in lines[rowsstart:rowsend]:
        for symb in all_symbols:
            if symb in line_to_check[start:end]:
                # print(line_to_check[start:end])
                detected.append(symb)
                return True
    # print('\n')
    # for line_to_check in lines[rowsstart:rowsend]:
    #     print(line_to_check[start:end])
    positions = [i for i in range(idxs[0], idxs[1])]
    failed[row_num].extend(positions)
        
    
    return False
    
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

valid = 0
numbers = []
for row_num, line in enumerate(lines):
    # if row_num == len(lines)-1:
        # print(lines)
    # if '337' in line:
    #     print(line)
    nums = get_numbers(line)
    # print(line)
    for num_pos, indexes in nums.items():
        num = num_pos[0]
        for inds in chunks(indexes, 2):
            print(inds)
            idxs = inds
            numbers.append(int(num))
            # print(num, line[idxs[0]:idxs[1]])
            if checkline(line, idxs, row_num):
                print(f'{num} is valid, adding it ({valid} + {num} = {valid+num})')
                if num == '337' or num == 337:
                    print(numbers, num)
                valid += num
            # else:  # num < 10:
            #     print(num, idxs)
            #     print(line)
            #     print(num, 'not  valid')
            #     x = 1
        # else:
print(valid)
            
# 544327 too low
# =============================================================================


gear_symb = '*'

def get_gears(line):
    numbers = {}
    num = ''
    start = -1
    end = ''
    numbing = False
    for i, c in enumerate(line):
        if c == gear_symb:
            numbing = True
            num += c
            if start == -1:
                start = i
            end = i + 1
        elif numbing:
            numbers[(num, start)] = (start, end)
            numbing = False
            start = -1
            end = ''
            num = ''
    if numbing:
        if not (int(num), start) in numbers.keys():
            numbers[(num, start)] = (start, end)
            
            
    # if numbing and num not in numbers.keys():
    #     numbers[int(num)] = (start, end)
    # elif numbing and num in numbers.keys():
    #     if start != numbers[int(num)][0]:
    #         numbers[str(num)] = (start, end)
            
    return numbers

        
def checkgears(idxs, row_num):
    if type(idxs) == list:
        idxs = idxs[0]
    start, end = idxs[0], idxs[1]
    if row_num not in failed.keys():
        failed[row_num] = []
    # if start == 0 or end >= len(line):
    #     print(line)
    start = max(0, start - 1)
    end = min(end + 1, len(line))
    gear_if_in = set(list(range(start, end)))
    
    rowsstart = max(0, row_num - 1)
    rowsend = min(row_num + 2, len(lines))
    valid_nums = []
    for line_to_check in lines[rowsstart:rowsend]:
        nums = get_numbers(line_to_check)
        for num, position in nums.items():
            numberposition = set(range(position[0], position[1]))
            if gear_if_in & numberposition:
                valid_nums.append(num[0])
        
    if len(valid_nums) == 2:
        return math.prod(valid_nums)
    return 0

lines = lines

gearvals = 0
for row_num, line in enumerate(lines):
    
    if gear_symb in line:
        gears = get_gears(line)
        for gear, position in gears.items():
            gear = gear[0]
            gearval = checkgears(position, row_num)
            gearvals += gearval
            print(gearvals)
print(gearvals)
                
                
            
            
        

# from tabulate import tabulate
# 
# table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]
# 
# print(tabulate(table, tablefmt='html'))
# changed_result = []
# for row_num, line in enumerate(lines):
#     change = failed[row_num]
#     changed_line = ''
#     for i, c in enumerate(line):
#         if i in change:
#             changed_line += f'<font color="green">{c}</font>'
#         else:
#             changed_line += c
#     changed_result.append(changed_line + '<br>')
# 
# Html_file= open("3.html","w")
# # print(tabulate(changed_result, tablefmt='html'))
# Html_file.write(''.join(changed_result))
# # Html_file.write(tabulate(changed_result, tablefmt='html'))
# Html_file.close()
# 
# =============================================================================
# =============================================================================
# def render_highlighted_text(file_path, highlights):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
# 
#     for line_number, positions in highlights.items():
#         line = lines[line_number - 1]  # Adjusting for 0-based indexing in lists
#         highlighted_line = list(line.rstrip('\n'))
# 
#         for position in positions:
#             highlighted_line[position - 1] = '\033[48;5;226m' + highlighted_line[position - 1] + '\033[0m'
# 
#         print(''.join(highlighted_line))
# =============================================================================
# =============================================================================
# import colorama
# from colorama import Fore, Back, Style
# 
# colorama.init(autoreset=True)
# 
# def render_highlighted_text(file_path, highlights):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
# 
#     for line_number, positions in highlights.items():
#         line = lines[line_number]  # Adjusting for 0-based indexing in lists
#         highlighted_line = list(line.rstrip('\n'))
# 
#         for position in positions:
#             highlighted_line[position] = Back.YELLOW + highlighted_line[position] + Style.RESET_ALL
# 
#         print(''.join(highlighted_line))
# 
# render_highlighted_text(source, failed)
# =============================================================================
end = timer()
# print(f'Sum of all steps: {len(positions)}')
print("{} Seconds needed for execution".format(round(end - start),1)) 
