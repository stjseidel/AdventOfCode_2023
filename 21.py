# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
from collections import defaultdict
    

class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        self.blocked = set()
        self.free = set()
        self.reached = set()
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == '.':
                    self.free.add((row, col))
                elif char == '#':
                    self.blocked.add((row, col))
                else:
                    self.reached.add((row, col))
                    self.free.add((row, col))
                    
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        return lines
    
    def part1(self, steps=64):
        lines = self.parse_lines()
        step = 0
        
        while step < steps:
            step += 1
            print(step)
            working = self.reached.copy()
            self.reached = set()
            for pos in working:
                for direction in self.directions:
                    checkpos = (pos[0] + direction[0], pos[1] + direction[1])
                    if checkpos in self.free:
                        # self.free.remove(checkpos)
                        self.reached.add(checkpos)
            print('reached:', len(self.reached), self.reached)
                
            
        self.result1 = len(self.reached)
        self.time1 = timer()
        return self.result1
                
    def part2(self, steps=6):
        lines = self.parse_lines()
        step = 0
        rows = len(lines)
        cols = len(lines[0])
        reached = self.reached.copy()
        self.reached = defaultdict(int)
        stepranges = []
        for pos in reached:
            self.reached[pos] += 1 
        while step < steps:
            step += 1
            print(step)
            working = self.reached.copy()
            self.reached = defaultdict(int)
            for pos, weight in working.items():
                for direction in self.directions:
                    checkpos = (pos[0] + direction[0], pos[1] + direction[1])
                    checkpos = (checkpos[0]%rows, checkpos[1]%cols)
                    if checkpos in self.free:
                        # self.free.remove(checkpos)
                        self.reached[checkpos] += weight 
            print('reached:', sum(self.reached.values()))
            stepranges.append(sum(self.reached.values()))
            
        self.result2 = sum(self.reached.values())
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='21', simple=True)
    today.create_txt_files()

# =============================================================================
# # simple part 1
#     today.set_lines(simple=True)
#     today.part1(steps=6)
#     print(f'Part 1 <SIMPLE> result is: {today.result1}')
#     
# # hard part 1
#     today.set_lines(simple=False)
#     today.part1(steps=64)
#     print(f'Part 1 <HARD> result is: {today.result1}')
#     today.stop()
# =============================================================================


# simple part 2
    today.set_lines(simple=True) 
    today.part2(steps=50)
    print(f'Part 2 <SIMPLE> result is: {today.result2}')

# =============================================================================
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2(steps=26501365)
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# =============================================================================

