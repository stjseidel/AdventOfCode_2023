# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
from math import prod

class Lense(): 
    def __init__(self, label, focal):
        self.label = label
        self.focal = focal
            
    def __repr__(self):
      return f'{self.label} {self.focal}'
    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        lines = ''.join(lines).split(',')  #ignore newlines
        return lines
    
    def decode_command(self, comm):
        current_value = 0
        for char in comm:
            current_value += ord(char)
            current_value *= 17
            current_value = current_value % 256
        return current_value
    
    def part1(self):
        commands = self.parse_lines()
        result1 = sum([self.decode_command(comm) for comm in commands])
            
        self.result1 = result1
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        commands = self.parse_lines()
        boxes = {i:[] for i in range(256)}
        # boxes = {0:[], 1:[], 3:[]}
        box = 0
        for command in commands:
            # box = self.decode_command(command)
            if '=' in command:
                lst = command.split('=')
                label, focal = lst[0], int(lst[1])
                add = True
            else:
                lst = command.split('-')
                label = lst[0]
                add = False
            box = self.decode_command(label)
            present = {lense.label:i for i, lense in enumerate(boxes[box])}
            if add:
                if label in present.keys():
                    boxes[box][present[label]] = Lense(label, focal)
                else:
                    boxes[box].append(Lense(label, focal))
            else:
                if label in present.keys():
                        boxes[box].pop(present[label])
        focusing_power = 0
        for key, box in boxes.items():
            for nth, lense in enumerate(box, 1):
                power = prod([key+1, nth, lense.focal])
                focusing_power += power
            
        self.result2 = focusing_power
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='15', simple=True)
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


