# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import ast

class Xmas_Part():
    def __init__(self, x, m, a, s):
        self.x = int(x)
        self.m = int(m)
        self.a = int(a)
        self.s = int(s)
    def __repr__(self):
        return f'(x={self.x}, m={self.m}, a={self.a}, s={self.s})'
    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        self.blueprints = {}
        self.xmas_parts = []
        blueprintlines = lines[:lines.index('')]
        xmas_part_lines = lines[lines.index('')+1:]
        for line in blueprintlines:
            bplen = line.index('{')
            self.blueprints[line[:bplen]] = line[bplen+1:-1].split(',')
        for line in xmas_part_lines:
            bplen = line.index('{')
            # self.xmas_parts.append(line[bplen+1:-1].split(','))
            self.xmas_parts.append(Xmas_Part(*[x.split('=')[1] for x in line[1:-1].split(',')]))
        
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        return lines
    
    def calc_xmas_part_dims(self):
        xs = sum([part.x for part in self.accepted])
        ms = sum([part.m for part in self.accepted])
        aas = sum([part.a for part in self.accepted])
        ss = sum([part.s for part in self.accepted])
        return sum([xs, ms, aas, ss])
    
    def check_xmas_part(self, xmas_part, blueprint):
        print(xmas_part, blueprint)
        if blueprint == 'R':
            self.rejected.append(xmas_part)
            return None
        elif blueprint == 'A':
            self.accepted.append(xmas_part)
            return None
        bp = self.blueprints[blueprint]
        print(bp)
        for check in bp:
            if check in ['R', 'A'] or ':' not in check:
                self.check_xmas_part(xmas_part, check)
                return None
            evalcheck, target = check.split(':')[0], check.split(':')[1]
            for char in ['<', '>', '=']:
                if char in evalcheck:
                    dim, value = evalcheck.split(char)[0], evalcheck.split(char)[1]
                    if eval(f"xmas_part.{dim} {char.replace('=', '==')} {int(value)}"):
                        self.check_xmas_part(xmas_part, target)
                        return None
    
    def part1(self):
        self.accepted = []
        self.rejected = []
        lines = self.parse_lines()
        for xmas_part in self.xmas_parts:
            self.check_xmas_part(xmas_part, 'in')
        self.result1 = self.calc_xmas_part_dims()
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        # lines = self.parse_lines()
        lines = self.parse_lines()
        for bp in self.blueprints:
            print(bp, self.blueprints[bp])
        self.result2 = 'TODO'
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='19', simple=True)
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

# =============================================================================
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2()
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# =============================================================================

