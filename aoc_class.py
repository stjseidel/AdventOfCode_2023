import re
from timeit import default_timer as timer
import sys
from pathlib import Path
from datetime import datetime

from math import gcd 
from functools import reduce 
import pandas as pd



class AOC():
    def __init__(self, day='', simple=True):
        if day == '':
            try:
                day = Path(sys.modules[self.__module__].__file__).stem
            except Exception as e:
                print('Tried to set day from __file__: ', e)
                day = str(datetime.today().day).zfill(2)
        print('Working on day: ', day)
        self.beginning_of_time = timer()
        self.day = day
        self.start()
        self.input_folder = Path('input')
        self.read_both_files()
        self.set_lines(simple=simple)
        self.simple = simple
    def start(self):
        self.beginning = timer()
        
    def stop(self):
        self.end = timer()
        print(f"{round(self.end - self.beginning, 2)} Seconds needed for execution")
        self.start()

    def read_both_files(self):
        file_path = self.input_folder / f'{self.day}_simple.txt'
        if not file_path.exists():
            print('no such file: ', file_path)
            self.lines_simple = []
        else:
            self.lines_simple = self.read_lines(file_path) 
        file_path = self.input_folder / f'{self.day}.txt'
        if not file_path.exists():
            print('no such file: ', file_path)
            self.lines_real = []
        else:
            self.lines_real = self.read_lines(file_path) 
    
    def set_lines(self, simple=False):
        if simple:
            self.lines = self.lines_simple
        else:
            self.lines = self.lines_real
    
    def read_lines(self, file_path=''):
        file_path = Path(file_path) 
        if not file_path.exists():
            file_path = self.input_folder / file_path
        with open(file_path) as fp:
            lines = fp.readlines()
        self.lines = [line.replace('\n', '') for line in lines]
        self.lines = [re.sub(' +', ' ', line) for line in self.lines]  # trim doubled spaces
        return self.lines

    def chunk_lines(self, n):
        self.lines = [self.chunk_line(line, n) for line in self.lines]
        
    def chunk_line(self, line, n):
        """Yield successive n-sized chunks from lst."""
        return [line[i:i + n] for i in range(0, len(line), n)]
            
# =============================================================================
#         for i in range(0, len(line), n):
#             yield line[i:i + n]
# =============================================================================

    def extract_numbers_from_lines(self, lines):
        # pattern = re.compile('\d+\.[.\d]+')
        return [str(''.join(filter(str.isdigit, line))) for line in lines]        
    
    def extract_numbers_from_string(self, line):
        # pattern = re.compile('\d+\.[.\d]+')
        return str(''.join(filter(str.isdigit, line)))

    def replace_with_dict(self, text, conversion_dict, before=None):
        before = before or str.lower
        t = before(text)
        for key, value in conversion_dict.items():
            t = t.replace(key, value)
        return t
    
    def create_txt_files(self):
        files = [Path(f'{self.day}_simple.txt'), Path(f'{self.day}.txt')]
        for file in files:
            if not file.exists():
                file.touch()
                print('created ', file)
                
    def lcm(self, denominators):
        # return least common denominator of a list of integers
        return reduce(lambda a,b: a*b // gcd(a,b), denominators)
    
    def transpose_lines(self, lines):
        lines_split = [[char for char in line] for line in lines]  # split lines into chars
        lines_T = pd.DataFrame(lines_split).T.values.tolist() 
        lines_T = [''.join(line) for line in lines_T]  # combine the split chars to strings
        return lines_T
    
    def border_coordinates(self, x_max, y_max):
        """Return a list of all coordinates at the border of a rectangle x,y (length of lines, line)"""
        border = []
    
        # Top and bottom borders
        for x in range(x_max):
            border.append((x, 0))            # Top border
            border.append((x, y_max - 1))    # Bottom border
    
        # Left and right borders (excluding corners to avoid duplicates)
        for y in range(1, y_max - 1):
            border.append((0, y))            # Left border
            border.append((x_max - 1, y))    # Right border
        return border
    
    def border_coordinates_of_lines(self, lines=''):
        lines = lines or self.lines
        return self.border_coordinates(len(lines[0]), len(lines))

                
if __name__ == '__main__':
    today = AOC()
    today.create_txt_files()
    # today.start()
    # today.stop
