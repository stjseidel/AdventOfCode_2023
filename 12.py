# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
from math import prod


class Splogs():  # spring logs
    def __init__(self, springs, damaged):
        self.springs = springs
        self.damaged = damaged
        
    def __repr__(self):
      return f'[springs: <{self.springs}>; damaged: <{self.damaged}]>'
    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        splogs = [Splogs(*line.split(' ')) for line in lines]
        for splog in splogs:
            splog.springs = [sp for sp in splog.springs.split('.') if not sp == '']
            splog.damaged = [int(sp) for sp in splog.damaged.split(',') if not sp == '']
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        
        return splogs
    
    def part1(self):
        splogs = self.parse_lines()
        for splog in splogs:
            springs = splog.springs
            damaged = splog.damaged
            splog_choices = []
            splog_result = 0
            if len(springs) == len(damaged):
                for i in range(len(springs)):
                    sp, da = springs[i], damaged[i]
                    choices = len(sp) - da + 1
                    splog_choices.append(choices)
                splog_result = prod(splog_choices)
            # else:
                
            print(springs, damaged, splog_choices, splog_result)
                

            
        self.result1 = 'TODO'
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
    today = Today(day='12', simple=True)
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
