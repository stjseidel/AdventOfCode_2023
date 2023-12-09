# -*- coding: utf-8 -*-\
"""


You can also [Share] this puzzle.
@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import math

class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
    colors = ['red', 'blue', 'green']
    
    
    def parse_lines(self):
        lines = self.lines
        lines_split = [line.split(':') for line in lines]
        lines_dict = {int(''.join(filter(str.isdigit, line[0]))):line[1].split(';') for line in lines_split}
        return lines_dict
    
    def check_game(self, game, throwsets, valid):
        colors = self.colors
        max_cols = {'red':12, 'green':13, 'blue':14}
        valid = 0
        for throws in throwsets:
            diced = {col:0 for col in self.colors}
            for throw in throws.split(','):
                num = int(''.join(filter(str.isdigit, throw)))
                for col in colors:
                    if col in throw.lower():
                        diced[col] += num
            for col in colors:
                # print(max_cols[col], diced[col], max_cols[col] >= diced[col])
                if max_cols[col] < diced[col]:
                    return valid
        valid += game
        return valid
    
    def part1(self):
        valid = 0
        lines_dict = self.parse_lines()
        for game, throwsets in lines_dict.items():
            valid += self.check_game(game, throwsets, valid)
        self.result1 = valid
        self.time1 = timer()
        return self.result1
    
    def check_game2(self, game, throwsets, power):
        colors = self.colors
        max_cols = {col:0 for col in colors}
        diced = {col:0 for col in colors}
        for throws in throwsets:
            for throw in throws.split(','):
                num = int(''.join(filter(str.isdigit, throw)))
                for col in colors:
                    if col in throw.lower():
                        diced[col] = num
            for col in colors:
                # print(max_cols[col], diced[col], max_cols[col] >= diced[col])
                max_cols[col] = max(max_cols[col], diced[col])
        dicevals = [val for val in max_cols.values() if val > 0]
        power = math.prod(dicevals)
        return power
    
    def part2(self):
        lines_dict = self.parse_lines()
        power = 0
        for game, throwsets in lines_dict.items():
            power += self.check_game2(game, throwsets, power)
        print(power)
        self.result2 = power
        self.time2 = timer()
        return self.result2
            
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
           

if __name__ == '__main__':
# prep
    today = Today(day='02', simple=True)
    today.create_txt_files()
    today.lines

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
    