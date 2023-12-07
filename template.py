# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:14:11 2023

template
@author: stjse
"""

for num in range(1, 26):
    day = str(num).zfill(2)

from timeit import default_timer as timer
from pathlib import Path
import pandas as pd
import csv
import string
import numpy as np
import matplotlib.pyplot as plt
import re
start = timer()
source = Path(f'{day}_input_1.txt')

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
    
def part_1():
    pass

def part_2():
    pass
if __name__ == "__main__":
    start = timer()
    
    
    
    
    
    