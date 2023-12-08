# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer

class Position():
    def __init__(self, here, left, right):
        self.here = here
        self.left = left
        self.right = right
        # if here == 'ZZZ':
        #     self.left = 'ZZZ'
        #     self.right = 'ZZZ'
        
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
            print(line)
            pos = line[0]
            # if pos != 'ZZZ':
            directions = line[1].replace('(', '').replace(')', '').split(',')
            self.positions[pos] = Position(pos, directions[0], directions[1])
            # else:
            #     self.positions[pos] = Position(pos, '', '')
                
        
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
        highest_steps = 0
        starting_positions = [pos for pos in self.positions.values() if pos.here.upper()[-1] == 'A']
        all_arrived = False
        positions = starting_positions.copy()
        max_arrived = 0
        self.steps = 0
        arrivals = {}
        while not all_arrived == len(starting_positions) and self.steps < 10**6:
            turn = self.commands[self.steps % len(self.commands)]
            try:
                positions = [self.turn_to(pos, turn) for pos in positions]
            except:
                # breakpoint()
                print(positions)
            self.steps += 1
            all_arrived = sum([pos.here.upper()[-1] == 'Z' for pos in positions])
            for i, pos in enumerate(positions):
                if pos.here.upper()[-1] == 'Z':
                    arrivals[i] = self.steps
            # highest_steps = max(highest_steps, self.steps)
            if self.steps % 1000000 == 0:
                print(f'{self.steps}: {all_arrived}', positions)
            if all_arrived > max_arrived:
                max_arrived = all_arrived
                # breakpoint()
                print(f'{self.steps}: {all_arrived}', positions)
        breakpoint()
        self.arrivals = arrivals
        self.result2 = self.steps
        self.time2 = timer()
        return self.result2

    def turn_to(self, pos, turn):
        try:
            if turn == 'L':
                pos = self.positions[pos.left]
            elif turn == 'R':
                pos = self.positions[pos.right]
            else:
                print('unknown direction at :', pos)
        except:
            print(pos, turn)
        return pos
        

    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='', simple=True)
    today.create_txt_files()
    today.lines

# =============================================================================
# # simple part 1
#     today.set_lines(simple=True)
#     today.parse_lines()
#     today.part1()
#     print(f'Part 1 <SIMPLE> result is: {today.result1}')
#     
# # hard part 1
#     today.set_lines(simple=False)
#     today.parse_lines()
#     today.part1()
#     print(f'Part 1 <HARD> result is: {today.result1}')
#     today.stop()
# 
# =============================================================================

# simple part 2
    today.lines = today.read_lines(file_path='08_simple2.txt')
    # today.set_lines(simple=True)
    # today.print_games()
    today.parse_lines()
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')
    breakpoint()
# hard part 2
    today.set_lines(simple=False)
    today.parse_lines()
    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    today.print_final()
    


