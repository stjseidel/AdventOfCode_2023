# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
from itertools import combinations

class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        
        lines = [[line, line] if '#' not in line else [line] for line in lines]
        lines = [sub for line in lines for sub in line]
        empty = []
        for col in range(len(lines[0])):
            if not '#' in [line[col] for line in lines]:
                empty.append(col)
        lines = [[char for char in line] for line in lines]
        # pd.DataFrame(lines)        

        for col in empty[::-1]:
            # print('inserting in: ', col)
            [line.insert(col, '.') for line in lines]
        self.lines = lines
        return lines
    
    def part1(self):
        lines = self.parse_lines()
        galaxies = []
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == '#':
                    galaxies.append((row, col))
        combos = combinations(galaxies, 2)
        total_dist = 0
        for combo in combos:
            a, b = combo[0], combo[1]
            dist = abs(a[0] - b[0]) + abs(a[1] - b[1]) 
            total_dist += dist
            print(a, b, dist)
        self.result1 = total_dist
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        lines = self.parse_lines()
        self.result2 = 'TODO'
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='', simple=True)
    today.create_txt_files()

# simple part 1
    today.set_lines(simple=True)
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# hard part 1
    today.set_lines(simple=False)
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()

# =============================================================================
# 
# # simple part 2
#     today.set_lines(simple=True) 
#     today.part2()
#     print(f'Part 2 <SIMPLE> result is: {today.result2}')
# 
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2()
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# 
# =============================================================================
