# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import re
from math import prod

class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self):
        lines = self.lines
        self.times = [int(seed) for seed in  lines[0].split(':')[1].split(' ') if seed != '']
        self.distances = [int(seed) for seed in  lines[1].split(':')[1].split(' ') if seed != '']
        self.games = {self.times[i]:self.distances[i] for i in range(len(self.times))}
        
    def parse_lines2(self):
            lines = self.lines
            self.times = [int(self.extract_numbers_from_string(lines[0].split(':')[1]))]
            self.distances = [int(self.extract_numbers_from_string(lines[1].split(':')[1]))]
            self.games = {self.times[i]:self.distances[i] for i in range(len(self.times))}
        
        
    def does_race_win(self, time, distance, charge_time):
        # print(time, charge_time, charge_time * (time-charge_time))
        return charge_time * (time-charge_time) > distance
        
    def part1(self):
        
        wins = []
        for time, distance in self.games.items():
            win = 0
            for charge_time in range(1, time):
                if self.does_race_win(time, distance, charge_time):
                    win += 1
            wins.append(win)
            # print('winning: ', win)
        print('result: ', prod(wins))

        self.result1 = prod(wins)
        self.time1 = timer()
        return prod(wins)

    def part2(self):
        today.parse_lines2()
        result = self.part1()
        self.result2 = result
        self.time2 = timer()

    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    day = '06'
    today = Today(day, simple=True)
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
    # today.parse_lines2()
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')
    
# hard part 2
    today.set_lines(simple=False)

    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    today.print_final()
    

