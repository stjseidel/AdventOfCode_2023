# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import re

class Target():
    def __init__(self, sources, target, change):
        self.sources = sources
        self.target = target
        self.change = change
    
    
class Today(AOC):
    def __init__(self, day, simple):
        AOC.__init__(self, day)
        self.simple = simple
        
    def parse_lines(self):
        lines = self.lines
        self.seeds = [int(seed) for seed in  lines[0].split(':')[1].split(' ') if seed != '']
        
        steps = -1
        almanac = {}
        for line in lines[1:]:
            if not line == '':
                if 'map' in line:
                    steps += 1
                    almanac[steps] = []
                else:
                    almanac[steps].append([int(element) for element in line.split(' ')])
        self.almanac = almanac
        
# =============================================================================
#     def part1_attempt1(self):
#         # for line in self.lines:
#         #     this_line = line.split(':')
#         #     game = self.extract_numbers_from_string(this_line[0])
#         #     numbers = this_line[1]
#         self.parse_lines()
#         target_maps = {target:{} for target in list(self.almanac.keys())}
#         last = max(self.almanac.keys())
#         for step, alm in self.almanac.items():
#             # al items: target, source, range_len
#             # if not step == last:
#             # print(step, alm)
#             for i, al in enumerate(alm):
#                 target, sources, range_len = al[0], al[1], al[2]
#                 new_dic = {sources+i:target+i for i in range(range_len)}
#                 # print(step, al, new_dic)
#                 target_maps[step].update(new_dic)
#                 # print(al)
#                 # print(target_maps[step])
#                 
#     
#         for seed in self.seeds:
#             if not seed in target_maps[last].keys():
#                 target_maps[last][seed] = seed
#         seed_positions = {step:{} for step in range(len(target_maps) + 1)}
#         seed_pos = {seed:seed for seed in self.seeds}    
#         seed_positions[0] = seed_pos
#         for step, target_map in target_maps.items():
#             for seed, pos in seed_positions[step].items():
#                 if pos in target_map:
#                     seed_positions[step+1][seed] = target_map[pos]
#                 else:   
#                     seed_positions[step+1][seed] = pos
#                 # print(seed, pos)
#             print(step)
#             for item in seed_positions[step+1].items():
#                 seed, new_pos = item[0], item[1]
#                 old_pos = seed_positions[step][seed]
#                 print(seed, ': ', old_pos, ' ---> ', new_pos)
#             print('----------')
#         for seed, location in seed_pos.items():
#             print(seed, location)
#             
#             
#         resulting_positions = [seed_pos[seed] for seed in self.seeds]
#         result = min(resulting_positions)
#         if self.result1 == 0:
#             self.result1 = result
#         self.time1 = timer()
#         return result        
# =============================================================================
    
    def part1(self):
        # for line in self.lines:
        #     this_line = line.split(':')
        #     game = self.extract_numbers_from_string(this_line[0])
        #     numbers = this_line[1]
        
        target_maps = {target:[] for target in list(self.almanac.keys())}
        last = max(self.almanac.keys())
        for step, alm in self.almanac.items():
            # al items: target, source, range_len
            # if not step == last:
            # print(step, alm)
            for i, al in enumerate(alm):
                target, sources, range_len = al[0], al[1], al[2]
                source_range = range(sources, sources+range_len)
                target_range = range(target, target+range_len)
                change = target-sources
                target_map = Target(sources=source_range, target=target_range, change=change)
                # print(step, al, new_dic)
                target_maps[step].append(target_map)
                # print(al)
                # print(target_maps[step])
                
    
        # seed_positions = {step:{} for step in range(len(target_maps) + 1)}
        seed_positions = {}
        seed_pos = {seed:seed for seed in self.seeds}    
        seed_positions[0] = seed_pos
        for step, target_map in target_maps.items():
            print(step)
            seed_positions[step+1] = {}
            for seed, pos in seed_positions[step].items():
                found = False
                for target in target_map:
                    # print(target.sources, target.target, target.change)
                    if pos in target.sources:
                        seed_positions[step+1][seed] = pos + target.change
                        found = True
                        # print(f'{step}: {pos} found in {target.sources}. {pos}+{target.change} --> {pos+target.change} {target.target}')
                        break
                if not found:
                    seed_positions[step+1][seed] = pos
                    # print(f'{step}: {pos} NOT found in {[target.sources for target in target_map]}')
                # print(seed, pos)
            # print(step)
            for item in seed_positions[step+1].items():
                seed, new_pos = item[0], item[1]
                old_pos = seed_positions[step][seed]
                # print(seed, ': ', old_pos, ' ---> ', new_pos)
            # print('----------')
        # for seed, location in seed_pos.items():
            # print(seed, location)
            
            
        resulting_positions = [seed_positions[max(seed_positions.keys())][seed] for seed in self.seeds]
        print('resulting_positions: ', resulting_positions)
        result = min(resulting_positions)
        self.result1 = result
        self.time1 = timer()
        return result   



    def part2(self):
        self.parse_lines()
        chunk_seeds = self.chunk_line(self.seeds, 2)
        new_seeds = []
        first = [c[0] for c in chunk_seeds] 
        for chunk in chunk_seeds:
            new_seeds +=  list(range(chunk[0], chunk[0]+chunk[1]))
        self.seeds = new_seeds
            
        self.result2 = self.part1()
        self.time2 = timer()
        return self.result2
        # 155057073 is too high

    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time2, 2)})')
        

if __name__ == '__main__':
# prep
    day = '05'
    today = Today(day, simple=True)
    today.lines
    # today.parse_lines()
    # today.chunk_lines(3)

# simple part 1
    today.set_lines(simple=True)
    today.parse_lines()
    result = today.part1()
    print(f'Part 1 <SIMPLE> result is: {result}')

# hard part 1
    today.set_lines(simple=False)
    today.parse_lines()
    result = today.part1()
    print(f'Part 1 <HARD> result is: {result}')
    today.stop()


# simple part 2
    today.set_lines(simple=True)
    result = today.part2()
    print(f'Part 2 <SIMPLE> result is: {result}')
    
# hard part 2
    today.set_lines(simple=False)
    result = today.part2()
    print(f'Part 2 <HARD> result is: {result}')
    today.stop()
    today.print_final()
    
