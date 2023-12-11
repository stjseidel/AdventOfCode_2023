# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import numpy as np
from matplotlib.path import Path

class Position():
    def __init__(self, here, row, col):
        self.here = here
        self.row = row
        self.col = col
        
    def __repr__(self):
      return f'here: {self.here}; left: {self.left}; right: {self.right}'
  
    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)

    def make_conventions(self):
        self.valid_connectors = {
            'north':['|', '7', 'F'],
            'east':['-', 'J', '7'],
            'south':['|', 'J', 'L'],
            'west':['-', 'L', 'F']
            }
        self.changes = {
            'north':[-1, 0],
            'east':[0, 1],
            'south':[1, 0],
            'west':[0, -1]
            }
        self.next_directions = {
            'north':{'|':'north', '7':'west', 'F':'east'},
            'east':{'-':'east', 'J':'north', '7':'south'},
            'south':{'|':'south', 'J':'west', 'L':'east'},
            'west':{'-':'west', 'L':'north', 'F':'south'}
            }
        self.directions = list(self.valid_connectors.keys())
        self.coming_froms = {self.directions[i%4]:self.directions[(i+2)%4] for i in range(len(self.directions))}
        self.start_symbol = 'S'
        
# =============================================================================
#     def parse_lines(self, file_path=''):
#         # self.translate_file()
#         self.lines = self.read_lines(file_path=f'{self.day}_{self.simp}.txt')
#         lines = self.lines
# =============================================================================
        
# =============================================================================
#     def part1(self):
#         # this oversteps the recursionlimit
#         self.steps = 0
#         lines = self.lines
#         self.rows, self.cols = len(lines), len(lines[0])
#         for i, line in enumerate(lines):
#             if self.start_symbol in line:
#                 start_r = i
#                 start_c = line.index(self.start_symbol)
#                 break
#         self.starting_directions = self.directions[:3]
#         self.starting_directions = ['north']
#         while len(self.starting_directions) > 0:
#             self.positions = {}
#             self.positions[(start_r, start_c)] = 'S'
#             self.row = start_r
#             self.col = start_c
#             direc = self.starting_directions[0]
#             self.start_dir = direc
#             self.starting_directions.remove(direc)
#             self.steps = 0
#             print(self.row, self.col, 'S', '. now going: ', direc)
#             self.traverse(coming_from=self.coming_froms[direc])
#             
#             
#     def traverse(self, coming_from):
#         self.steps += 1
#         # directions = [direc for direc in self.directions if direc != coming_from]
#         direc = self.coming_froms[coming_from]
#         # print(f'{self.steps}. old_pos: ({self.row},{self.col}) {[self.lines[self.row][self.col]]}. Coming from: {coming_from}. Going {direc}.')
#         change_r, change_c = self.changes[direc][0], self.changes[direc][1]
#         new_r, new_c = self.row + change_r, self.col + change_c
#         if self.steps % 250 == 0:
#             self.show_plots()
#         if 0 <= new_r and new_r < self.rows and 0 <= new_c and new_r < self.cols:
#             next_symbol = self.lines[new_r][new_c]
#             if next_symbol == '.':
#                 return None
#             print(f'{self.steps}. old_pos: ({self.row},{self.col}) {[self.lines[self.row][self.col]]}. Coming from: {coming_from}. Going {direc}. new_pos: ({new_r},{new_c}) {self.lines[new_r][new_c]}')
#             if next_symbol in self.valid_connectors[direc] or next_symbol == self.start_symbol:
#                 if next_symbol == self.start_symbol:
#                     print(f'arrived at [{new_r}, {new_c}] after {self.steps}')
#                     if coming_from in self.starting_directions:
#                         self.starting_directions.remove(coming_from)
#                 else:
#                     new_direction = self.next_directions[direc][next_symbol]
#                     next_coming_from  = self.coming_froms[new_direction]
#                     print(new_r, new_c, next_symbol, '. now going: ', new_direction)
#                     if (new_r, new_c) in self.positions.keys():
#                         print('alarm!!')
#                     self.positions[(new_r, new_c)] = next_symbol
#                     self.row, self.col = new_r, new_c
#                     self.traverse(coming_from=next_coming_from)
#         if next_symbol == self.start_symbol:
#             print('total steps: ', self.steps)
#         self.show_plot()
#         self.result1 = self.steps // 2
#         self.time1 = timer()
#         return self.result1
#     
#     def show_plots(self):
#         plotlines = ['.' * len(line) for line in self.lines]
#         for pos, char in self.positions.items():
#             line = plotlines[pos[0]]
#             col = pos[1]
#             if col > 0 and col < len(line)-1:
#                 plotlines[pos[0]] = line[:col] + char + line[col+1:]
#             elif col == 0:
#                 plotlines[pos[0]] = char + line[1:]
#             else:
#                 plotlines[pos[0]] = line[:-1] + char
#         self.plotlines = plotlines
#         with open(f'10_plotlines_{self.start_dir}_{self.steps}.txt', 'w') as f:
#             for line in plotlines:
#                 f.write(line)
#                 f.write('\n')
# =============================================================================

    def part1(self):
        # this oversteps the recursionlimit
        lines = self.lines
        self.rows, self.cols = len(lines), len(lines[0])
        for i, line in enumerate(lines):
            if self.start_symbol in line:
                start_r = i
                start_c = line.index(self.start_symbol)
                break
        self.starting_directions = self.directions[:3]
        reached = False
        tries = -1
        while len(self.starting_directions) > 0 and not reached: 
            steps = 0
            start_dir = self.starting_directions[0]
            self.starting_directions.remove(start_dir)
            tries += 1
            # self.positions = {}
            # self.positions[(start_r, start_c)] = 'S'
            self.row = start_r
            self.col = start_c
            next_turn_possible = True
            here = (start_r, start_c)
            direc = self.starting_directions[0]
            symbol = 'S'
            self.positions = [here]
            while not reached and next_turn_possible:
                # print(here, symbol, direc)
                here = (here[0] + self.changes[direc][0], here[1] + self.changes[direc][1])
                symbol = self.lines[here[0]][here[1]]
                if symbol not in (self.valid_connectors[direc] + [self.start_symbol]):
                    next_turn_possible = False
                else:
                    steps += 1
                    
                    if symbol == self.start_symbol:
                        reached = True
                    else:
                        self.positions.append(here)
                        direc = self.next_directions[direc][symbol]
            # print('total steps: ', steps)
        self.result1 = steps // 2
        self.time1 = timer()
        return self.result1
    
    def show_plots(self):
        plotlines = ['.' * len(line) for line in self.lines]
        for pos, char in self.positions.items():
            line = plotlines[pos[0]]
            col = pos[1]
            if col > 0 and col < len(line)-1:
                plotlines[pos[0]] = line[:col] + char + line[col+1:]
            elif col == 0:
                plotlines[pos[0]] = char + line[1:]
            else:
                plotlines[pos[0]] = line[:-1] + char
        self.plotlines = plotlines
        with open(f'10_plotlines_{self.start_dir}_{self.steps}.txt', 'w') as f:
            for line in plotlines:
                f.write(line)
                f.write('\n')
                
    def part2(self):
        self.part1()
        possible_positions = set([(row, col) for row in range(len(self.lines)) for col in range(len(self.lines[0]))]) - set(self.positions)
         
        tunnel = Path(self.positions)
        nests = 0
        for pos in possible_positions:
            if tunnel.contains_point(pos):
                nests += 1
        self.result2 = nests
        self.time2 = timer()
        return self.result2
# =============================================================================
#     def part2(self):
#        this calcs the nest points touching points connected to the outside... but not as required the points you can get to by squeezing through
#         self.part1()
#         possible_positions = set([(row, col) for row in range(len(self.lines)) for col in range(len(self.lines[0]))]) - set(self.positions)
#         fringe = [(-1, i) for i in range(-1, len(self.lines[0])+1)]
#         fringe += [(len(self.lines), i) for i in range(-1, len(self.lines[0])+1)]
#         fringe += [(i, -1) for i in range(-1, len(self.lines)+1)]
#         fringe += [(len(self.lines[0]), i) for i in range(-1, len(self.lines)+1)]
# # =============================================================================
# #         fringe = [np.array([-1, i]) for i in range(-1, len(self.lines[0])+1)]
# #         fringe += [np.array([len(self.lines), i]) for i in range(-1, len(self.lines[0])+1)]
# #         fringe += [np.array([i, -1]) for i in range(-1, len(self.lines)+1)]
# #         fringe += [np.array([len(self.lines[0]), i]) for i in range(-1, len(self.lines)+1)]
# # =============================================================================
#         # fringe = set(fringe)
#         
#         border = [(-1, -1), (-1, 0), (-1, 1), 
#                 (0, -1), (0, 1), 
#                 (1, -1), (1, 0), (1, 1)]
#         
#         here = np.array([5, 7])
#         here + border
#         changes = True
#         checked = 0
#         while checked <= len(fringe)-1:
#             here = fringe[checked]
#             check_positions = set([(x[0] + here[0], x[1] + here[1]) for x in border])
#             checked += 1
#             # pos = np.array(set([-1, 0]))
#             overlap = check_positions & possible_positions
#             if len(overlap) > 0:
#                 # print(overlap)
#                 for el in overlap:
#                     possible_positions.remove(el)
#                     fringe.append(el)
#                 
#         self.result2 = len(possible_positions)
#         self.time2 = timer()
#         return self.result2
# 
# =============================================================================
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='10', simple=True)
    today.create_txt_files()
    today.lines
    today.make_conventions()

# simple part 1
    today.set_lines(simple=True)
    # today.parse_lines()
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# hard part 1
    today.set_lines(simple=False)
    today.part1()
    print(f'Part 1 <HARD> result is: {today.result1}')
    today.stop()


# simple part 2
    today.set_lines(simple=True)
    print('starting part 2, simple2')
    today.part2()
    print(f'Part 2 <SIMPLE> result is: {today.result2}')

# =============================================================================
# # simple part 2
#     print('starting part 2, simple2')
#     today.lines = today.read_lines(file_path='10_simple2.txt')
#     today.part2()
#     print(f'Part 2 <SIMPLE> result is: {today.result2}')
# 
# # simple part 2
#     print('starting part 2, simple3')
#     today.lines = today.read_lines(file_path='10_simple3.txt')
#     today.part2()
#     print(f'Part 2 <SIMPLE> result is: {today.result2}')
# =============================================================================

# hard part 2
    print('starting part 2')
    today.set_lines(simple=False)
    today.part2()
    print(f'Part 2 <HARD> result is: {today.result2}')
    today.stop()
    today.print_final()
    # 726 too high


