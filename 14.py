# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import matplotlib.pyplot as plt


class Coords():  # spring logs
    def __init__(self, row, col):
        self.row = row
        self.col = col
            
    def __repr__(self):
      return f'[Coords: [row: {self.row}, col: {self.col}]]>'
    

class Stones():  # spring logs
    def __init__(self, row, col, fixed):
        self.row = row
        self.col = col
        self.fixed = fixed
        self.coords = Coords(row, col)
    def __repr__(self):
      return f'[Stone: [{self.row}, {self.col}]; fixed: <{self.fixed}]>'
    
    
class Today(AOC):
    def __init__(self, day, simple):
        AOC.__init__(self, day)
        self.rock = '#'
        self.roll = 'O'
    
    
    def parse_lines(self, file_path=''):
        lines = self.lines
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        return lines
    
    def part1(self):
        lines = self.parse_lines()
        columns = self.transpose_lines(lines)
        weight = 0
        for col in columns:
            stackheight = len(col)
            print(col)
            for i, char in enumerate(col):
                if char == self.rock:
                    stackheight = len(col) - (i+1)
                elif char == self.roll:
                    weight += stackheight
                    stackheight -= 1
                    
        
        self.result1 = weight
        self.time1 = timer()
        return self.result1
                
    
    def get_rock_ranks(self):
        rows = len(self.lines)
        columns = len(self.lines[0])
        rockranks = {}
        for row in range(rows):
            rockranks[(row, -1)] = [stone for stone in self.fixpos if stone.row == row]
        for col in range(columns):
            rockranks[(-1, col)] = [stone for stone in self.fixpos if stone.col == col]
        self.rockranks = rockranks
            
        
    def slide(self, direction):
        # for each possible direction, for the given rank (row or column number)
        # first get all stones on that rank
        # then move all stones as far as possible
# =============================================================================
#         if direction in ['north', 'south']:
#             for col in range(len(self.lines[0])):
#                 fixed = self.rockranks[(0, col)]
#                 rankstones = [stone for stone in self.loose if stone.col == col]
#         else:
#             for row in range(len(self.lines)):
#                 fixed = self.rockranks[(row, 0)]
#                 rankstones = [stone for stone in self.loose if stone.row == row]
# =============================================================================
            
        if direction in ['north', 'south']:
            for col in range(len(self.lines[0])):
                fixed = self.rockranks[(-1, col)]
                rankstones = [stone for stone in self.loose if stone.col == col]
                if direction == 'north':
                    steps = 1
                    stackheight = 0
                    reverse = False
                else:
                    steps = -1
                    stackheight = len(self.lines) -1               
                    reverse = True
                # rankstones = sorted([stone.row for stone in rankstones])
                all_rankstones = fixed + rankstones
                all_rankstones.sort(key=lambda x: x.row, reverse=reverse)  # sort by their direction 
                # print([stone.row for stone in all_rankstones])
                for i, stone in enumerate(all_rankstones):
                    if stone.fixed:
                        stackheight = stone.row + steps
                    else:
                        all_rankstones[i].row = stackheight
                        stackheight += + steps
        if direction in ['west', 'east']:
            for row in range(len(self.lines)):
                fixed = self.rockranks[(row, -1)]
                rankstones = [stone for stone in self.loose if stone.row == row]
                if direction == 'west':
                    steps = 1
                    stackheight = 0
                    reverse = False
                else:
                    steps = -1
                    stackheight = len(self.lines[0])-1       
                    reverse = True
                # rankstones = sorted([stone.row for stone in rankstones])
                all_rankstones = fixed + rankstones
                all_rankstones.sort(key=lambda x: x.col, reverse=reverse)  # sort by their direction 
                # print([stone.col for stone in all_rankstones])
                for i, stone in enumerate(all_rankstones):
                    if stone.fixed:
                        stackheight = stone.col + steps
                    else:
                        all_rankstones[i].col = stackheight
                        stackheight += + steps
        # sorted([[d.row, d.col] for d in self.loose])
        # sorted([[d.row, d.col] for d in self.fixed])
        # print(self.loose)
            
    def calc_north_weight(self):
        return sum([len(self.lines) - stone.row for stone in self.loose])
    
    def part2(self):
        lines = self.parse_lines()
        stones = []
        self.directions = ['north', 'west','south', 'east']
        
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                char = lines[row][col]
                if char != '.':
                    stones.append(Stones(row, col, fixed=char==self.rock))
        self.loose = {stone for stone in stones if not stone.fixed}
        self.fixed = {stone for stone in stones if stone.fixed}
        self.fixpos = {stone for stone in self.fixed}
        
        self.get_rock_ranks()
        weights = {}
        self.turn = -1
        self.plot_stones()
        
        for i in range(1, 4000):
            self.turn = i
            self.direction = self.directions[(i-1)%4]
            self.slide(self.direction)
            north_weight = self.calc_north_weight()
            # print(f'{i}: sliding {self.direction}. weight: {north_weight}')
            # print(north_weight)
            if self.turn % 4 == 0:
                weights[i // 4] = north_weight
            # if direction == 'east':
            # self.plot_stones()
        self.weights = weights
        self.result2 = weights
        # for i in range(1000, 1100):
        #     print(weights[i])
        # weights[]
        
        
        # weight_chunks = self.chunk_line(list(self.weights.values()), 4)
        # for chunk in weight_chunks:
        #     print(chunk)
        # picked = weight_chunks[1000]
        
        pickup = 100  # starting to watch for repetitions after 1000 
        weight = list(self.weights.values())[pickup:]
        repeated = False
        i = 5
        while not repeated and i <= len(weight)//2:
            if weight[:i] == weight[i:i*2]:
                repeated = True
                print(i, weight[:i], weight[i:i*2])
                period = i
            else:
                i += 1
            
        print(f'starting from {pickup}, the sequence repeates itself every {i} cycles') 
        
        # for i, chunk in enumerate(weight_chunks):
        #     if chunk == tenth:
        #         matched.append(i)
        # print(f'the tenth chuck repeats itself like this: {[(matched[i+1]-matched[i]) for i in range(len(matched[:-1]))]}')
        # amplitude = 7 * 4
        # starting from the tenth chuck of 4, we get a repetition after every 28 turns or 7 rotations
        length = (1000000000 - pickup) % period
        self.result2 = self.weights[pickup+length]
        
        print(today.weights[max(today.weights.keys())])
        self.time2 = timer()
        return self.result2
        
    def plot_stones(self):
        rows = len(self.lines)
        cols = len(self.lines[0])
        
        # Sample coordinates for rock and roll
        rock = [(abs(stone.col-cols), abs(stone.row-rows)) for stone in self.fixed]
        roll = [(abs(stone.col-cols), abs(stone.row-rows)) for stone in self.loose]
        
        # Extract x and y values from the lists
        x_a, y_a = zip(*rock)
        x_b, y_b = zip(*roll)
        
        # Create a scatter plot
        plt.scatter(x_a, y_a, marker='X', label='fixed')
        plt.scatter(x_b, y_b, marker='o', label='loose')
        
        # Add labels and legend
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        
        # Set equal spacing for x and y axes
        plt.axis('equal')
        if self.turn == -1:
            plt.title(f'This is turn {self.turn + 1}')
        else:
            plt.title(f'This is [Cycle {self.turn//4+1}] turn {self.turn}. Just turned {self.direction}')

        plt.xticks(range(int(min(min(x_a), min(x_b))), int(max(max(x_a), max(x_b))) + 1))
        plt.yticks(range(int(min(min(y_a), min(y_b))), int(max(max(y_a), max(y_b))) + 1))
        # Invert the x-axis
        plt.gca().invert_xaxis()
        plt.grid(True)
        
        # Show the plot
        plt.show()
        
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='14', simple=True)
    today.create_txt_files()

# =============================================================================
# # simple part 1
#     today.set_lines(simple=True)
#     today.part1()
#     print(f'Part 1 <SIMPLE> result is: {today.result1}')
#     
# # hard part 1
#     today.set_lines(simple=False)
#     today.part1()
#     print(f'Part 1 <HARD> result is: {today.result1}')
#     today.stop()
# =============================================================================


# simple part 2
    today.set_lines(simple=True) 
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')

# =============================================================================
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2()
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# 
# 
# =============================================================================
