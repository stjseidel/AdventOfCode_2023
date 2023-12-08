# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
# import math


class Position():
    def __init__(self, here, left, right):
        self.here = here
        self.left = left
        self.right = right
        
    def __repr__(self):
      return f'here: {self.here}; left: {self.left}; right: {self.right}'
  
    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        
        lines = self.lines
        self.commands = lines[0]
        self.positions = {}
        lines = [line.replace(' ', '').split('=') for line in lines[1:] if line != '']
        for line in lines:
            pos = line[0]
            directions = line[1].replace('(', '').replace(')', '').split(',')
            self.positions[pos] = Position(pos, directions[0], directions[1])
        
    def part1(self):
        self.steps = 0
        pos = 'AAA'
        pos = self.positions[pos]
        while not pos.here == 'ZZZ':
            turn = self.commands[self.steps % len(self.commands)]
            if turn == 'L':
                pos = self.positions[pos.left]
            elif turn == 'R':
                pos = self.positions[pos.right]
            else:
                print('unknown direction at :', pos)
            self.steps += 1
        self.result1 = self.steps
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        starting_positions = [pos for pos in self.positions.values() if pos.here.upper()[-1] == 'A']
        positions = starting_positions.copy()
        arrivals = []
        # while not all_arrived == len(starting_positions) and self.steps < 10**6:
        for start_pos in positions:
            self.steps = 0
            pos = start_pos
            arrived = False
            while not arrived:
                turn = self.commands[self.steps % len(self.commands)]
                pos = self.turn_to(pos, turn)
                self.steps += 1
                if pos.here.upper()[-1] == 'Z':
                    arrivals.append(self.steps)
                    arrived = True
            
        self.result2 = self.lcm(arrivals)
        self.time2 = timer()
        return self.result2

    def turn_to(self, pos, turn):
        if turn == 'L':
            pos = self.positions[pos.left]
        elif turn == 'R':
            pos = self.positions[pos.right]
        else:
            print('unknown direction at :', pos)
        return pos
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='', simple=True)
    today.create_txt_files()
    today.lines

# simple part 1
    today.set_lines(simple=True)
    today.parse_lines()
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# hard part 1
    today.set_lines(simple=False)
    today.parse_lines()
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()


# simple part 2
    today.lines = today.read_lines(file_path='08_simple2.txt')
    # today.set_lines(simple=True)
    today.parse_lines()
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')

# hard part 2
    today.set_lines(simple=False)
    today.parse_lines()
    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    today.print_final()
    