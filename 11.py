# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
from itertools import combinations


class Cell():
    def __init__(self, row, col):
        self.row = row
        self.col = int(col)
        
    def __repr__(self):
      return f'[row: <{self.row}>; col: <{self.col}]>'
  
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
# =============================================================================
#     def parse_lines(self, file_path=''):
#         lines = self.lines
#         
#         lines = [[line, line] if '#' not in line else [line] for line in lines]
#         lines = [sub for line in lines for sub in line]
#         empty = []
#         for col in range(len(lines[0])):
#             if not '#' in [line[col] for line in lines]:
#                 empty.append(col)
#         lines = [[char for char in line] for line in lines]
#         # pd.DataFrame(lines)        
# 
#         for col in empty[::-1]:
#             [line.insert(col, '.') for line in lines]
#         self.lines = lines
#         return lines
# =============================================================================
    
# =============================================================================
#     def part1(self):
#         lines = self.parse_lines()
#         galaxies = []
#         for row, line in enumerate(lines):
#             for col, char in enumerate(line):
#                 if char == '#':
#                     galaxies.append((row, col))
#         combos = combinations(galaxies, 2)
#         total_dist = 0
#         for combo in combos:
#             a, b = combo[0], combo[1]
#             dist = abs(a[0] - b[0]) + abs(a[1] - b[1]) 
#             total_dist += dist
#             print(a, b, dist)
#         self.result1 = total_dist
#         self.time1 = timer()
#         return self.result1
# 
# =============================================================================

    def parse_lines(self, file_path=''):
        lines = self.lines
        
        self.empty_rows = set([i for i, line in enumerate(lines) if '#' not in line])
        empty_cols = set()
        for col in range(len(lines[0])):
            if not '#' in [line[col] for line in lines]:
                empty_cols.add(col)
        # pd.DataFrame(lines)        
        self.empty_cols = empty_cols
        return lines
    
    def part1(self):
        lines = self.parse_lines()
        galaxies = []
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == '#':
                    galaxies.append((Cell(row, col)))
        combos = combinations(galaxies, 2)
        total_dist = 0
        distance_factor  = self.distance_factor 
        empty_rows = self.empty_rows
        empty_cols = self.empty_cols
        for combo in combos:
            a, b = combo[0], combo[1]
            row_dist = set(range(*sorted([a.row, b.row])))
            col_dist = set(range(*sorted([a.col, b.col])))

            row_dist_expanded = len(row_dist) + len(row_dist & empty_rows) * distance_factor - len(row_dist & empty_rows) 
            col_dist_expanded = len(col_dist) + len(col_dist & empty_cols) * distance_factor - len(col_dist & empty_cols) 
            dist = row_dist_expanded + col_dist_expanded
            total_dist += dist
        self.result1 = total_dist
        self.time1 = timer()
        return self.result1
    
# =============================================================================
#     def part2(self):
#         lines = self.parse_lines()
#         self.result2 = 'TODO'
#         self.time2 = timer()
#         return self.result2
# =============================================================================
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='', simple=True)
    today.create_txt_files()

# simple part 1
    today.set_lines(simple=True)
    today.distance_factor = 2
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# hard part 1
    today.set_lines(simple=False)
    today.distance_factor = 2
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()
    res1 = today.result1
    time1 = today.time1

# simple part 2
    today.set_lines(simple=True) 
    today.distance_factor = 10
    today.part1()
    print(f'Part 2 <SIMPLE> result with factor {today.distance_factor} is: {today.result1}')
    today.distance_factor = 100
    today.part1()
    print(f'Part 2 <SIMPLE> result with factor {today.distance_factor} is: {today.result1}')

# hard part 2
    today.set_lines(simple=False)
    today.distance_factor = 1000000
    today.part1()
    print(f'Part 2 <HARD> result with factor {today.distance_factor} is: {today.result1}')
    today.stop()
    today.time2 = today.time1
    today.time1 = time1
    today.result2 = today.result1
    today.result1 = res1
    today.print_final()

