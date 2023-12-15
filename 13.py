# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import pandas as pd


class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        areas = {}
        i = 0
        areas[i] = []
        for line in lines:
            if line == '':
                i += 1
                areas[i] = []
            else:
                areas[i].append(line)
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        return areas
    

    def check_mirror(self, lines):
        linerows = lines
        linecols = self.transpose_lines(lines)
        factors = [100, 1]
        # strings = [f'doing line rows [len: {len(lines)}]', f'doing columns, a.k.a. the transposed lines [len: {len(linecols)}]']
        
        for i, lines in enumerate([lines, linecols]):
            # print(strings[i])
            # print('---- current result: ', self.result1, '-------')
            factor = factors[i]
            for start in range(1, len(lines)//2+1):
                checklines = lines[0:start*2]
                rows = len(checklines) // 2
                if checklines[:rows][::-1] == checklines[rows:]:
                    # print(f'found a result with {rows}, starting from front. first line was {linerows[0]}')
                    return rows * factor
            if len(lines) % 2 != 0:
                for start in range(1, len(lines)//2+1):
                    checklines = lines[start*2-1:]
                    rows = len(checklines) // 2
                    if checklines[:rows][::-1] == checklines[rows:]:
                        print(f'found a result with {rows}, starting from back, adding 1. first line was {linerows[0]}')
                        return (len(lines)-rows) * factor
        print('NO RESULT!', linerows)
        return 0
    
    def check_mirror2(self, lines):
        linerows = lines
        linecols = self.transpose_lines([[char for char in line] for line in lines])
        factors = [100, 1]
        # strings = [f'doing line rows [len: {len(lines)}]', f'doing columns, a.k.a. the transposed lines [len: {len(linecols)}]']
        
        for i, lines in enumerate([lines, linecols]):
            # print(strings[i])
            # print('---- current result: ', self.result1, '-------')
            factor = factors[i]
            for start in range(1, len(lines)//2+1):
                checklines = lines[0:start*2]
                rows = len(checklines) // 2
                left = checklines[:rows][::-1]
                right = checklines[rows:]
                diffs = [(left[i], right[i]) for i in range(rows) if left[i] != right[i]]
                if len(diffs) == 1:
                    leftc, rightc = diffs[0][0], diffs[0][1]
                    diffchars = [leftc[i]+rightc[i] for i in range(len(leftc)) if leftc[i] != rightc[i]]
                    if len(diffchars) == 1:
                        # print(f'found a result with {rows}, starting from front. first line was {linerows[0]}')
                        print(rows, diffchars, leftc, rightc, left, right)
                        return rows * factor
                    
            for start in range(1, len(lines)//2+1):
                checklines = lines[start*2-1:]
                rows = len(checklines) // 2
                left = checklines[:rows][::-1]
                right = checklines[rows:]
                diffs = [(left[i], right[i]) for i in range(rows) if left[i] != right[i]]
                if len(diffs) == 1:
                    left, right = diffs[0][0], diffs[0][1]
                    diffchars = [(left[i], right[i]) for i in range(rows) if left[i] != right[i]]
                    if len(diffchars) == 1:
                        # print(f'found a result with {rows}, starting from front. first line was {linerows[0]}')
                        print(f'found a result with {rows}, starting from back, adding 1. first line was {linerows[0]}')
                        return (len(lines)-rows) * factor
        print('NO RESULT!', linerows)
        return 0
            # starting from row 0 until row -1, see if there is a reflecting that stretches up to the upper fringe
        
    def part1(self):
        areas = self.parse_lines()
        self.result1 = 0
        for area, lines in areas.items():
            # if area % 2 == 1:
            # lines = [''.join(line) for line in lines_split]
            line_result = self.check_mirror(lines=lines)
            self.result1 += line_result
            print(area, line_result, self.result1)
        self.result1 = self.result1    
        self.time1 = timer()
        return self.result1
            
                
    def part2(self):
        areas = self.parse_lines()
        self.result2 = 0
        for area, lines in areas.items():
            # if area % 2 == 1:
            # lines = [''.join(line) for line in lines_split]
            line_result = self.check_mirror2(lines=lines)
            if line_result == 0:
                line_result = self.check_mirror(lines=lines)
            self.result2 += line_result
            print(area, line_result, self.result1)
        self.result2 = self.result2
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='13', simple=True)
    today.create_txt_files()

# simple part 1
    today.set_lines(simple=True)
    today.part1()
    # today.part1_attempt_slice()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# hard part 1
    today.set_lines(simple=False)
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()
    # too high: 33432
    # too low: 21830 
    today.result1 = 0

# simple part 2
    today.set_lines(simple=True) 
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')

# hard part 2
    today.set_lines(simple=False)
    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    # 55026 too high
    # 51892 too high
    # 54658 too high
    # today.print_final()

