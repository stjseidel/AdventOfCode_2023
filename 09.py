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
        
    def parse_lines(self, file_path=''):
        
        lines = self.lines
        lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        return lines
    
    def predict(self, line):
        if not set(line) == set([0]):
            next_line = [line[i+1] - line[i] for i in range(len(line)-1)]
            # print(line, next_line)
            predicted = self.predict(next_line)
            # print(predicted)
            line.append(line[-1] + predicted)
        return line[-1]
    
    def predict_backwards(self, line):
        if not set(line) == set([0]):
            next_line = [line[i+1] - line[i] for i in range(len(line)-1)]
            # print(line, next_line)
            predicted = self.predict_backwards(next_line)
            # print(predicted)
            line.insert(0, (line[0] - predicted))
        return line[0]
    
    def part1(self):
        lines = self.parse_lines()
        self.result1 = sum([self.predict(line) for line in lines])
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        lines = self.parse_lines()
        self.result2 = sum([self.predict_backwards(line) for line in lines])
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='', simple=True)
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
