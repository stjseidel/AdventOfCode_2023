# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer

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
        target_maps = {target:[] for target in list(self.almanac.keys())}
        for step, alm in self.almanac.items():
            for i, al in enumerate(alm):
                target, sources, range_len = al[0], al[1], al[2]
                source_range = range(sources, sources+range_len)
                target_range = range(target, target+range_len)
                change = target-sources
                target_map = Target(sources=source_range, target=target_range, change=change)
                target_maps[step].append(target_map)
    
        # seed_positions = {step:{} for step in range(len(target_maps) + 1)}
        seed_positions = {}
        seed_pos = {seed:seed for seed in self.seeds}    
        seed_positions[0] = seed_pos
        for step, target_map in target_maps.items():
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
            # for item in seed_positions[step+1].items():
            #     seed, new_pos = item[0], item[1]
            #     old_pos = seed_positions[step][seed]
            
        resulting_positions = [seed_positions[max(seed_positions.keys())][seed] for seed in self.seeds]
        print('resulting_positions: ', resulting_positions)
        result = min(resulting_positions)
        self.result1 = result
        self.time1 = timer()
        return result   

# =============================================================================
#     def part2(self):
#         self.parse_lines()
#         chunk_seeds = self.chunk_line(self.seeds, 2)
#         new_seeds = []
#         first = [c[0] for c in chunk_seeds] 
#         for chunk in chunk_seeds:
#             new_seeds +=  list(range(chunk[0], chunk[0]+chunk[1]))
#         self.seeds = new_seeds
#             
#         self.result2 = self.part1()
#         self.time2 = timer()
#         return self.result2
#     
# =============================================================================
    def part2(self):
        self.parse_lines()
        self.almanac
        chunk_seeds = self.chunk_line(self.seeds, 2)
        new_seeds = []
        current_ranges = [range(seed[0], seed[0]+seed[1]) for seed in chunk_seeds]
        origin_seeds = sum([len(rng) for rng in current_ranges])
        # current_ranges = [range(13, 14)]
        for pos, almanac in self.almanac.items():
            # print(f'{pos}: starting with {sum([len(rng) for rng in current_ranges])} seeds.')
            # print(f'{pos} START: {current_ranges}')
            # input_ranges = [range(maps[0], maps[0]+maps[2]) for maps in almanac]
            # output_ranges = [range(maps[1], maps[1]+maps[2]) for maps in almanac]
            output_ranges = []
            result_ranges = []
            origin = ''
            step = 0
            while len(current_ranges) > 0:
                step += 1
                this_range = current_ranges[0]
                if len(this_range) == 0:
                    current_ranges.remove(this_range)
                else:
                    if origin == this_range:
                        # print('case 5: no overlaps found in any map, directly convertig without change')
                        result_ranges.append(this_range)
                        current_ranges.remove(this_range)
                    else:
                        origin = this_range
                        start = this_range[0]
                        stop = this_range[-1]
                        killed = False
                        for maps in almanac:
                            # maps[0] == destination, # maps[1] == source, # maps[2] == length
                            maps_start = maps[1]
                            maps_stop = maps[1]+maps[2]
                            change = maps[0] - maps[1]
                            panic = False
                            if start + change == 0 or maps_start == 0 or start == 0:
                                print('panic')
                                panic = True
                            if stop < maps_start or start > maps_stop:
                                pass
                            else:
                                if panic:
                                    pass
                                current_ranges.remove(this_range)
                                if start <= maps_start and stop <= maps_stop:  
                                    # print('case 1')
                                    # starting earlier and stopping earlier
                                    result_ranges.append(range(maps_start + change, stop + change + 1))  # [maps_start, stop]
                                    current_ranges.append(range(start, maps_start))  # [start, maps_start[
                                    killed = True
                                    break
                                elif start >= maps_start and stop <= maps_stop:
                                    # print('case 2')
                                # fully within map
                                    result_ranges.append(range(start + change, stop + change + 1))  # [start, stop]
                                    killed = True
                                    break
                                
                                elif start >= maps_start and stop > maps_stop:
                                    # print('case 3')
                                # starting within and continuing
                                    result_ranges.append(range(start + change, maps_stop + change + 1))  # [start, maps_stop]
                                    current_ranges.append(range(maps_stop+1, stop+1))  # ]maps_stop, stop]
                                    killed = True
                                    break
                                    
                                elif start < maps_start and stop > maps_stop:
                                    # print('case 4')
                                    # extends over maps range
                                    result_ranges.append(range(maps_start + change, maps_stop + change +1))  # [maps_start, maps_stop]
                                    current_ranges.append(range(start, maps_start))  # [start, maps_start[
                                    
                                    current_ranges.append(range(maps_stop+1, stop+1))  # ]maps_stop, maps_stop]
                                    # almanac.remove(maps)
                                    killed = True
                                    break
                                else:
                                    print('not supposed to happen!')
                        if not killed:
                            result_ranges.append(this_range)
                            current_ranges.remove(this_range)
            if sum([len(rng) for rng in result_ranges]) != origin_seeds:
                print(f'diff: {origin_seeds - sum([len(rng) for rng in result_ranges])}')
                pass
            old_current_range = current_ranges
            current_ranges = list(set(current_ranges + result_ranges))
            print(f'{pos} END: {min([rng[0] for rng in result_ranges])}. Seeds: {sum([len(rng) for rng in result_ranges])}')
            print('.')
        
        lowest = min([rng[0] for rng in result_ranges])
        
        result_seeds = sum([len(rng) for rng in result_ranges])
        print(f'started with {origin_seeds} seeds and ended with {result_seeds} locations. matching numbers: {origin_seeds == result_seeds}')
        print(f'diff: {origin_seeds - result_seeds}')
            
        self.result2 = lowest
        self.time2 = timer()
        return self.result2
    

    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time2, 2)})')

if __name__ == '__main__':
# prep
    day = '05'
    today = Today(day, simple=True)

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

# =============================================================================
# # simple part 2
#     today.set_lines(simple=True)
#     result = today.part2()
#     print(f'Part 2 <SIMPLE> result is: {result}')
# =============================================================================
    
# =============================================================================
# simple part 2 provides correct solution but runs out of memory from simply reading
# the seed ranges into RAM
# =============================================================================
# hard part 2
# 32900747 too low
    today.set_lines(simple=False)
    result = today.part2()
    print(f'Part 2 <HARD> result is: {result}')
    today.stop()
    today.print_final()

