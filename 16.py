# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer

    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
    directions = {'north':(-1, 0), 'west':(0, -1), 'south':(1, 0), 'east':(0, 1)}
    reflectors = {
        ('-', 'south'):['east', 'west'],
        ('-', 'north'):['east', 'west'],
        ('|', 'east'):['north', 'south'],
        ('|', 'west'):['north', 'south'],
        ('/','east'):['north'],
        ('/','south'):['west'],
        ('/','west'):['south'],
        ('/','north'):['east'],
        ('\\','east'):['south'],
        ('\\','south'):['east'],
        ('\\','west'):['north'],
        ('\\','north'):['west'],
               }
    energized = set()
    travelled = set()
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        self.positions = {}
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                self.positions[(row, col)] =  char
                
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        return lines
    
    def travel(self, here, direction):
        if (here, direction) in self.travelled:
            return None
        self.travelled.add((here, direction))
        change = self.directions[direction]
        next_pos = (here[0] + change[0], here[1] + change[1])
        self.energized.add(here)
        # print(here, direction, next_pos)
        if not next_pos in self.positions:
            return None
        next_char = self.positions[next_pos]
        if next_char == '.':
            self.travel(next_pos, direction)
        else:
            if (next_char, direction) in self.reflectors.keys():
                splitdirections = self.reflectors[(next_char, direction)]
                for direction in splitdirections:
                    self.travel(next_pos, direction)
            else:
                self.travel(next_pos, direction)
    
    def part1(self):
        lines = self.parse_lines()
        self.energized = set()
        self.travelled = set()
        here = (0, -1)
        direction = 'east'
        self.travel(here, direction)
        self.result1 = len(self.energized) - 1
        self.time1 = timer()
        return self.result1
                
    
            
    def part2(self):
        lines = self.parse_lines()
        border = self.border_coordinates_of_lines(lines=lines)
        maximized = 0
        for here in border:
            for direction in self.directions.keys():
                self.energized = set()
                self.travelled = set()
                change = self.directions[direction]
                origin_pos = (here[0] - change[0], here[1] - change[1])  # the starting position that caused us to be at 'here'
                self.travel(origin_pos, direction)
                if len(self.energized) - 1 > maximized:
                    maximized = len(self.energized) - 1
                    print(maximized, here, direction)
                
        self.result2 = maximized
        
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='16', simple=True)
    today.create_txt_files()

# simple part 1
# =============================================================================
#     today.set_lines(simple=True)
#     today.part1()
#     print(f'Part 1 <SIMPLE> result is: {today.result1}')
# =============================================================================
    
    
    
    import sys

# Set a new recursion limit (choose a value carefully)
    sys.setrecursionlimit(10000)
    
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

