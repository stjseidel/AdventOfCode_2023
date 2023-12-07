# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:43:05 2023

@author: stjse
"""

# aoc_module.py
from timeit import default_timer as timer
from pathlib import Path
import string
import re

class AOC:
    def __init__(self, day):
        self.day = day
        self.input_file_path = Path(f'{day}.txt')
        self.simple_file_path = Path(f'{day}_simple.txt')
        self.repdict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                        'eight': '8', 'nine': '9'}
        self.start()

    def start(self):
        self.beginning = timer()
        
    def stop(self):
        self.end = timer()
        print("{} Seconds needed for execution".format(round(self.end - self.beginning))) 
    
    def read_lines(self, file_path):
        with open(file_path) as fp:
            lines = fp.readlines()
        return [line.replace('\n', '') for line in lines]

    def extract_numbers(self, lines):
        # pattern = re.compile('\d+\.[.\d]+')
        return [str(''.join(filter(str.isdigit, line))) for line in lines]

    def sum_numbers(self, numbers):
        summed = 0
        for num in numbers:
            if len(num) == 0:
                pass
            elif len(num) == 1:
                summed += int(num + num)
            else:
                summed += int(num[0] + num[-1])
            # print(num, summed)
        return summed

    def process_file(self, file_path):
        start = timer()
        lines = self.read_lines(file_path)
        numbers = self.extract_numbers(lines)
        summed = self.sum_numbers(numbers)
        end = timer()
        print("{} Seconds needed for execution".format(round(end - start), 1))
        return summed

    def translate(self, text, conversion_dict, before=None):
        before = before or str.lower
        t = before(text)
        for key, value in conversion_dict.items():
            t = t.replace(key, value)
        return t

    def cycle_through(self, line, left=True):
        if left:
            num = 0
            pos = 0
            while num == 0 and pos < len(line):
                if str.isdigit(line[pos]):
                    return line[pos]
                results = [line[pos:pos + len(key)] for key, val in self.repdict.items() if
                           line[pos:pos + len(key)] in self.repdict.keys()]
                if len(results) > 0:
                    return self.repdict[results[0]]
                pos += 1
            return ''
        else:
            num = 0
            pos = len(line) - 1
            while num == 0 and pos >= 0:
                if str.isdigit(line[pos]):
                    return line[pos]
                results = [line[pos - len(key) + 1:pos + 1] for key, val in self.repdict.items() if
                           line[pos - len(key) + 1:pos + 1] in self.repdict.keys()]
                results = [res for res in results if res != '']
                for key in results:
                    if key in self.repdict.keys():
                        return self.repdict[results[0]]
                pos -= 1
            return ''

    def process_lines(self, lines):
        numbers = [f'{self.cycle_through(line, left=True)}{self.cycle_through(line, left=False)}' for line in lines]
        summed = 0
        for num in numbers:
            if len(num) == 0:
                pass
            elif len(num) == 1:
                summed += int(num + num)
            else:
                summed += int(num[0] + num[-1])
            # print(num, summed)
        return summed


if __name__ == "__main__":
    aoc_instance = AOC('01')
    result = aoc_instance.process_file(aoc_instance.input_file_path)
    print(f"Result from processing real file: {result}")

    # Example for processing the simple file
    result = aoc_instance.process_file(aoc_instance.simple_file_path)
    print(f"Result from processing simple file: {result}")
