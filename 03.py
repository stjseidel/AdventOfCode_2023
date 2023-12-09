# -*- coding: utf-8 -*-\
"""


You can also [Share] this puzzle.
@author: stjse
"""
from aoc_class import AOC
from timeit import default_timer as timer
import math
import string

class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
    digits = string.digits
    gear_symb = '*'
    def parse_lines(self):
        lines = self.lines
        all_str = set(''.join(lines))
        self.all_symbols = set([c for c in all_str if not c in self.digits and not c == '.'])

    def get_numbers(self, line):
        numbers = {}
        num = ''
        start = -1
        end = ''
        numbing = False
        for i, c in enumerate(line):
            if c in self.digits:
                numbing = True
                num += c
                if start == -1:
                    start = i
                end = i + 1
            elif numbing:
                numbers[(int(num), start)] = (start, end)
                numbing = False
                start = -1
                end = ''
                num = ''
        if numbing:
            if not (int(num), start) in numbers.keys():
                numbers[(int(num), start)] = (start, end)
        return numbers
    
    def checkline(self, line, idxs, row_num):
        lines = self.lines
        detected = []
        
        if type(idxs) == list:
            idxs = idxs[0]
        start, end = idxs[0], idxs[1]
        if row_num not in self.failed.keys():
            self.failed[row_num] = []
        start = max(0, start - 1)
        end = min(end + 1, len(line))
        
        rowsstart = max(0, row_num - 1)
        rowsend = min(row_num + 2, len(lines))
        for line_to_check in lines[rowsstart:rowsend]:
            for symb in self.all_symbols:
                if symb in line_to_check[start:end]:
                    detected.append(symb)
                    return True
        positions = [i for i in range(idxs[0], idxs[1])]
        self.failed[row_num].extend(positions)
        return False
        
    def part1(self):
        valid = 0
        numbers = []
        self.failed = {}
        for row_num, line in enumerate(self.lines):
            nums = self.get_numbers(line)
            for num_pos, indexes in nums.items():
                num = num_pos[0]
                for inds in self.chunk_line(indexes, 2):
                    idxs = inds
                    numbers.append(int(num))
                    if self.checkline(line, idxs, row_num):
                        valid += num
        self.result1 = valid
        self.time1 = timer()
        return self.result1
    
    def get_gears(self, line):
        numbers = {}
        num = ''
        start = -1
        end = ''
        numbing = False
        for i, c in enumerate(line):
            if c == self.gear_symb:
                numbing = True
                num += c
                if start == -1:
                    start = i
                end = i + 1
            elif numbing:
                numbers[(num, start)] = (start, end)
                numbing = False
                start = -1
                end = ''
                num = ''
        if numbing:
            if not (int(num), start) in numbers.keys():
                numbers[(num, start)] = (start, end)
        return numbers
            
    def checkgears(self, idxs, row_num, line):
        if type(idxs) == list:
            idxs = idxs[0]
        start, end = idxs[0], idxs[1]
        if row_num not in self.failed.keys():
            self.failed[row_num] = []
        start = max(0, start - 1)
        end = min(end + 1, len(line))
        gear_if_in = set(list(range(start, end)))
        rowsstart = max(0, row_num - 1)
        rowsend = min(row_num + 2, len(self.lines))
        valid_nums = []
        for line_to_check in self.lines[rowsstart:rowsend]:
            nums = self.get_numbers(line_to_check)
            for num, position in nums.items():
                numberposition = set(range(position[0], position[1]))
                if gear_if_in & numberposition:
                    valid_nums.append(num[0])
            
        if len(valid_nums) == 2:
            return math.prod(valid_nums)
        return 0
        
    def part2(self):
        lines = self.lines
        gearvals = 0
        for row_num, line in enumerate(lines):
            if self.gear_symb in line:
                gears = self.get_gears(line)
                for gear, position in gears.items():
                    gear = gear[0]
                    gearval = self.checkgears(position, row_num, line)
                    gearvals += gearval
        self.result2 = gearvals
        self.time2 = timer()
        return self.result2
                
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='03', simple=True)
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
    today.set_lines(simple=True)
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
    