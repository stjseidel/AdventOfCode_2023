# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import re

class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def part1(self):
        for line in self.lines:
            this_line = line.split(':')
            game = self.extract_numbers_from_string(this_line[0])
            numbers = this_line[1]
            
        self.result1 = 0
        self.time1 = timer()

    def part2(self):
        for line in self.lines:
            this_line = line.split(':')
            game = self.extract_numbers_from_string(this_line[0])
            numbers = this_line[1]
        self.result2 = 0
        self.time2 = timer()

    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time2, 2)})')
        

if __name__ == '__main__':
# prep
    day = '05'
    today = Today(day, simple=True)
    today.lines
    # today.chunk_lines(3)

# simple part 1
    today.set_lines(simple=True)
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')

# hard part 1
    today.set_lines(simple=False)
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()


# simple part 2
    today.set_lines(simple=True)
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')
    
# hard part 2
    today.set_lines(simple=False)
    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    today.print_final()
    
