# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
from shapely.geometry import Polygon
from matplotlib.path import Path
import numpy as np

class Position():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.here = (row, col)
    def __repr__(self):
      return f'row: {self.row}; col: {self.col}. [{self.here}]'
  

class Orders():
    def __init__(self, direction, length, colorcode):
        self.direction = direction
        self.length = length
        self.colorcode = colorcode
        
    def __repr__(self):
        return f'[{self.direction}, {self.length}, {self.colorcode}]'
    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        splitlines = [el.split(' ') for el in lines]
        orders = [Orders(el[0], int(el[1]), el[2][1:-1]) for el in splitlines]
        return orders
    
    def parse_lines2(self, file_path=''):
        lines = self.lines
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        splitlines = [el.split(' ') for el in lines]
        # The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.
        direc_dir = {0:'R', 1:'D', 2:'L', 3:'U'}
        orders = [Orders(direc_dir[int(el[2][-2:-1])], int(el[2][2:-2], base=16), el[2][1:-1]) for el in splitlines]
        return orders
    
    def dig(self, order):
        direction = order.direction
        length = order.length
        
        if direction == 'U':
            change = np.array([1, 0])
        elif direction == 'D':
            change = np.array([-1, 0])
        elif direction == 'L':
            change = np.array([0, -1])
        elif direction == 'R':
            change = np.array([0, 1])
        else:
            print('unknown directrion!')
            return None
        for i in range(length):
            self.here += change
            self.fringe.append((self.here[0], self.here[1]))
        
    def dig2(self):
        for order in self.orders:
            print(order, self.here)
            direction = order.direction
            length = order.length
            
            if direction == 'U':
                change = np.array([1, 0])
            elif direction == 'D':
                change = np.array([-1, 0])
            elif direction == 'L':
                change = np.array([0, -1])
            elif direction == 'R':
                change = np.array([0, 1])
            else:
                print('unknown directrion!')
            self.here += change * length
            self.fringe.append((self.here[0], self.here[1]))
        

    def part1(self):
        startpos = (0, 0)
        self.here = startpos
        self.fringe = [self.here]
        orders = self.parse_lines()
        for order in orders:
            _ = self.dig(order)
        path = Path(self.fringe)
        Bbox = path.get_extents()
        b1 = Bbox.min
        b2 = Bbox.max
        inner = set()
        for row in  range(int(b1[0]), int(b2[0]+1)):
            for col in range(int(b1[1]), int(b2[1]+1)):
                if (row, col) not in self.fringe:
                    if path.contains_point((row, col)):
                        inner.add((row, col))
        
        self.result1 = len(set(self.fringe)) + len(inner)
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        startpos = (0, 0)
        self.here = startpos
        self.fringe = [self.here]
        self.orders = self.parse_lines2()
        self.dig2()
        poly = Polygon(self.fringe)
        # poly.area contains the area within the square centers, not the outside of the squares. we add hald the fringe again.
        self.result2 = poly.area + sum([order.length for order in self.orders]) // 2 + 1
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='18', simple=True)
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

