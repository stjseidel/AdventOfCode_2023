# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer

class Brick():
    settled_squares = {}
    highest_settled = 0
    brickcount = 0
    bricks = []
    bricks_dict = {}
    
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.base = [(x, y, z) for x in range(x1, x2+1) for y in range(y1, y2+1) for z in [min(z1, z2)]]
        self.top = [(x, y, z) for x in range(x1, x2+1) for y in range(y1, y2+1) for z in [max(z1, z2)]]
        self.supports = []
        self.height = max(z1, z2) - min(z1, z2) +1
        self.settled = False
        self.id = Brick.brickcount
        Brick.brickcount += 1
        self.supported_by = None
        self.tumbling = set()
        Brick.bricks.append(self)
        Brick.bricks_dict[self.id] = self
        
    def reset():
        Brick.settled_squares = {}
        Brick.bricks = []
        Brick.bricks_dict = {}
        Brick.highest_settled = 0
        Brick.brickcount = 0
        
    def settle_at(self, level):
        self.base = [(x[0], x[1], level) for x in self.base] 
        self.top = [(x[0], x[1], level+self.height-1) for x in self.top] 
        self.settled = True
        self.highest_settled = max(self.highest_settled, level)
        for square in self.top:
            Brick.settled_squares[square] = self.id
        
    def fall(self, level=None):
        level = level or self.base[0][2]
        down = level - 1
        if level == 0:
            self.settle_at(level=0)
            self.supported_by = {-1}
        if not self.settled:
            
            supported_squares = [square for square in self.base if (square[0], square[1], down) in self.settled_squares.keys()]
            supporters = {Brick.settled_squares[(square[0], square[1], down)] for square in supported_squares}
            if len(supporters) > 0:
                self.settle_at(level)
                self.supported_by = supporters
            self.fall(level=down)
            
    def desintegrate(self):
        # breakpoint()
        tumbling = {self.id}
        queue = self.supports.copy()
        while len(queue) > 0:
            brick_id = queue[0]
            next_brick = Brick.bricks_dict[brick_id]
            if next_brick.supported_by - tumbling == set():
                tumbling.add(brick_id)
                queue += next_brick.supports
            queue.pop(0)
        self.tumbling = tumbling
        if self.id in self.tumbling:
            self.tumbling.remove(self.id)
        return len(tumbling)
        
    def __iter__(self):
        return iter([self.x1, self.y1, self.z1, self.x2, self.y2, self.z2])
    
    def __repr__(self):
        return f'[({self.x1}, {self.y1}, {self.z1}), ({self.x2}, {self.y2}, {self.z2})]'

    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        Brick.reset()
        self.bricks = [Brick(*[int(lin) for lin in line.replace('~', ',').split(',')]) for line in lines]
        
        
        x_values, y_values, z_values, x2_values, y2_values, z2_values = zip(*self.bricks)

        # Get the minimum and maximum values for each dimension
        min_x, max_x = min(x_values+x2_values), max(x_values+x2_values)
        min_y, max_y = min(y_values+y2_values), max(y_values+y2_values)
        min_z, max_z = min(z_values+z2_values), max(z_values+z2_values)
        self.ground = Brick(min_x, min_y, 0, max_x, max_y, 0)
        self.bricks.append(self.ground)
        
        self.bricks = sorted(self.bricks, key=lambda brick: min(brick.z1, brick.z2))
        self.bricks_dict = {brick.id:brick for brick in self.bricks}
        return lines
    
    def settle_the_fall(self):      
        for brick in self.bricks:
            brick.fall()
            if not brick == self.ground:
                for supporter in brick.supported_by:
                    if supporter == -1:
                        self.ground.supports.append(brick.id)
                    self.bricks_dict[supporter].supports.append(brick.id)
        
    def part1(self):
        lines = self.parse_lines()
        self.settle_the_fall()
        safe_bricks = 0
        for id in range(Brick.brickcount):
            brick = self.bricks_dict[id]
            if len(brick.supports) == 0:
                safe_bricks += 1
            else:
                safe = min([len(self.bricks_dict[sup_id].supported_by) for sup_id in brick.supports]) > 1
                
                if safe:
                    safe_bricks += 1
                        
        self.result1 = safe_bricks
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        lines = self.parse_lines()
        self.settle_the_fall()
        falling = 0
        for brick in Brick.bricks: 
            if brick != self.ground:
                fall = brick.desintegrate()
                falling += fall
            
        self.result2 = falling
        self.time2 = timer()
        return self.result2
   
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='22', simple=True)
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

