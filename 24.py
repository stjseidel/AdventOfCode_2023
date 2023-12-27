# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import numpy as np
from itertools import combinations


class Hailstone():
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.pos = np.array([x, y, z])
        self.speed = np.array([dx, dy, dz])
        self.pos_xy = np.array([x, y])
        self.speed_xy = np.array([dx, dy])
        self.pos2 = self.pos + self.speed
        self.pos_xy2 = self.pos_xy + self.speed_xy
        
    def __repr__(self):
        return f'[{self.pos}, {self.speed}]'
        
    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        self.hailstones = [Hailstone(*[int(x.strip()) for x in line.replace('@', ',').split(',') if not x == '@']) for line in lines]
        return lines
    
    def part1(self):
        lines = self.parse_lines()
        combos = combinations(self.hailstones, 2)
        if self.simple:
            self.minx = 7
            self.miny = 7
            self.maxx = 21
            self.maxy = 21
        else:
            self.minx = 200000000000000
            self.miny = 200000000000000
            self.maxx = 400000000000000
            self.maxy = 400000000000000
        collisions = 0
        for combo in combos:
            try:
                if self.intersect_2d(combo[0], combo[1]):
                    # print(combo)
                    collisions += 1
            except Exception as e:
                print(e, combo)
        self.result1 = collisions
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        lines = self.parse_lines()
        
        self.result2 = 'TODO'
        self.time2 = timer()
        return self.result2
        
    def intersect_2d(self, hail_a, hail_b):
        A = np.array([hail_a.pos_xy, hail_a.pos_xy2])        
        B = np.array([hail_b.pos_xy, hail_b.pos_xy2])   
        matrix = np.array([A[1]-A[0], B[0]-B[1]])
        if np.linalg.det(matrix) == 0.0:
        #     print('singular matrix')
            return False
            
        # print(np.linalg.det(np.array([A[1]-A[0], B[0]-B[1]])))
        if hail_a.dx/hail_b.dx == hail_a.dy/hail_b.dy:
            # print('paths are parralel')
            return False
        t, s = np.linalg.solve(matrix.T, B[0]-A[0])
        intersect = (1-t)*A[0] + t*A[1]
        if ((intersect[0] - hail_a.x) / hail_a.dx) < 0:  # is the intersection in the future?
            # print('first is in the past', intersect)
            return False
        if ((intersect[1] - hail_b.y) / hail_b.dy) < 0:  # is the intersection in the future?
            # print('second is in the past', intersect)
            return False

        if intersect[0] <= self.maxx and intersect[0] >= self.minx:
            if intersect[1] <= self.maxy and intersect[1] >= self.miny:
                # print('INSIDE boundary', intersect)
                return True
            # else:
            #     print('outside boundary', intersect)
        return False
        
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='24', simple=True)
    today.create_txt_files()

# simple part 1
    today.set_lines(simple=True)
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# hard part 1
    today.set_lines(simple=False)
    today.simple = False
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()

# =============================================================================
# # simple part 2
#     today.set_lines(simple=True) 
#     today.part2()
#     print(f'Part 2 <SIMPLE> result is: {today.result2}')
# 
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2()
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# 
# =============================================================================
    