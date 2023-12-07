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
start = timer()
source = Path('01_1_input_1.txt')

abc = list(string.ascii_lowercase)
ABC = list(string.ascii_uppercase)
letters = abc + ABC
# 1
with open(source) as fp:
    lines = fp.readlines()
lines = [line.replace('\n', '') for line in lines]
pattern = re.compile('\d+\.[.\d]+')
numbers = [str(''.join(filter(str.isdigit, line))) for line in lines]
summed = 0
for num in numbers:
    if len(num) == 0:
        pass
    elif len(num) == 1:
        summed += int(num + num)
    else: 
        summed += int(num[0] + num[-1])
    print(num, summed)

end = timer()
# print(f'Sum of all steps: {len(positions)}')
print("{} Seconds needed for execution".format(round(end - start),1)) 



lines2 =  [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
    ]

def translate(text, conversion_dict, before=None):
    """
    Translate words from a text using a conversion dictionary

    Arguments:
        text: the text to be translated
        conversion_dict: the conversion dictionary
        before: a function to transform the input
        (by default it will to a lowercase)
    """
    # if empty:
    if not text: return text
    # preliminary transformation:
    before = before or str.lower
    t = before(text)
    for key, value in conversion_dict.items():
        t = t.replace(key, value)
    return t


repdict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def cyclethrough(line, repdict=repdict, left=True):
    #from left
    if left:
        num = 0
        pos = 0
        while num == 0 and pos < len(line):
            if str.isdigit(line[pos]):
                # print( line[pos])
                # print(line[pos])
                return line[pos]
            results = [line[pos:pos+len(key)] for key, val in repdict.items() if line[pos:pos+len(key)] in repdict.keys()]
            if len(results) > 0:
                # print(results[0])
                return repdict[results[0]]
            pos += 1
        return ''
            
    else:
        num = 0
        pos = len(line)-1
        while num == 0 and pos >= 0:
            if str.isdigit(line[pos]):
                # print( line[pos])
                return line[pos]
            results = [line[pos-len(key)+1:pos+1] for key, val in repdict.items() if line[pos-len(key)+1:pos+1] in repdict.keys()]
            # results = [line[pos-len(key)+1:pos+1] for key, val in repdict.items()]  # if line[pos-len(key)+1:pos+1] in repdict.keys()]
            results = [res for res in results if res != '']
            for key in results:
                if key in repdict.keys():
                    # print(results[0], repdict[results[0]])    
                    return repdict[results[0]]
                    
            # print(results)
            pos -= 1
        return ''

# for line in lines2:
#     print(line)
#     num = f'{cyclethrough(line, repdict=repdict, left=True)}{cyclethrough(line, repdict=repdict, left=False)}'
#     # num = f'{cyclethrough(line, repdict=repdict, left=False)}'
#     print(line, num)
#     print('------------')

numbers2 = [ f'{cyclethrough(line, repdict=repdict, left=True)}{cyclethrough(line, repdict=repdict, left=False)}' for line in lines]

# numbers2 = [str(''.join(filter(str.isdigit, line))) for line in lines]
numbers2_comp = [translate(line, repdict) for line in lines]
summed2 = 0
for num in numbers2:
    # num = f'{cyclethrough(line, repdict=repdict, left=True)}{cyclethrough(line, repdict=repdict, left=False)}'
    if len(num) == 0:
        pass
    elif len(num) == 1:
        summed2 += int(num + num)
    else: 
        summed2 += int(num[0] + num[-1])
    print(num, summed2)

end = timer()
# print(f'Sum of all steps: {len(positions)}')
print("{} Seconds needed for execution".format(round(end - start),1)) 

# repdict = {'NORTH':'N','SOUTH':'S','EAST':'E','WEST':'W'}
pattern = '|'.join(sorted(re.escape(k) for k in repdict))
address = "123 north anywhere street"
address = lines2[2]
re.sub(pattern, lambda m: repdict.get(m.group(0).upper()), address, flags=re.IGNORECASE)

numbers = [str(''.join(filter(str.isdigit, line))) for line in numbers2_comp]
translate(address, repdict)
summed = 0
for num in numbers:
    if len(num) == 0:
        pass
    elif len(num) == 1:
        summed += int(num + num)
    else: 
        summed += int(num[0] + num[-1])
    print(num, summed)
