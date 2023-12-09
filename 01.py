# -*- coding: utf-8 -*-\
"""


You can also [Share] this puzzle.
@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer

    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
    repdict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    def part1(self):
        numbers = [str(''.join(filter(str.isdigit, line))) for line in self.lines]
        numbers = [num for num in numbers if len(num) > 0]
        summed = sum([int(num[0] + num[-1]) for num in numbers])
        self.time1 = timer()
        self.result1 = summed

    def translate(self, text, conversion_dict, before=None):
        """
        Translate words from a text using a conversion dictionary
    
        Arguments:
            text: the text to be translated
            conversion_dict: the conversion dictionary
            before: a function to transform the input
            (by default it will to a lowercase)
        """
        if not text:
            return text
        before = before or str.lower
        t = before(text)
        for key, value in conversion_dict.items():
            t = t.replace(key, value)
        return t
    
    def cyclethrough(self, line, repdict=repdict, start_from_left=True):
        num = 0
        if start_from_left:
            pos = 0
            while num == 0 and pos < len(line):
                if str.isdigit(line[pos]):
                    return line[pos]
                results = [line[pos:pos+len(key)] for key, val in repdict.items() if line[pos:pos+len(key)] in repdict.keys()]
                if len(results) > 0:
                    return repdict[results[0]]
                pos += 1
            return ''
        else:
            pos = len(line)-1
            while num == 0 and pos >= 0:
                if str.isdigit(line[pos]):
                    return line[pos]
                results = [line[pos-len(key)+1:pos+1] for key, val in repdict.items() if line[pos-len(key)+1:pos+1] in repdict.keys()]
                results = [res for res in results if res != '']
                for key in results:
                    if key in repdict.keys():
                        return repdict[results[0]]
                pos -= 1
            return ''
    
    def part2(self):
        repdict = self.repdict
        numbers = [ f'{self.cyclethrough(line, repdict=repdict, start_from_left=True)}{self.cyclethrough(line, repdict=repdict, start_from_left=False)}' for line in self.lines]
        summed = 0
        numbers = [num for num in numbers if len(num) > 0]
        summed = sum([int(num[0] + num[-1]) for num in numbers])
        self.time2 = timer()
        self.result2 = summed
            
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')


if __name__ == '__main__':
# prep
    today = Today(day='01', simple=True)
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
    # today.set_lines(simple=True) 
    today.lines = today.read_lines(file_path='01_simple2.txt')
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')

# hard part 2
    today.set_lines(simple=False)
    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    today.print_final()
