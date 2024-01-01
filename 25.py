# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import networkx as nx


class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        G = nx.Graph()
        for line in lines:
            node = line.split(':')[0]
            connectors = [node for node in line.split(':')[1].split(' ') if node != '']
            G.add_nodes_from([node] + connectors)
            for connector in connectors:
                G.add_edge(node, connector)
        # nx.draw(G, with_labels=True)
        self.G = G
        return lines
    
    def add_connected(self, node):
        if not node in self.connected:
            self.connected.add(node)
            for conn in self.G.neighbors(node):
                self.add_connected(conn)
        
    def part1(self):
        lines = self.parse_lines()
        G = self.G
        min_cut = nx.minimum_edge_cut(G)
        if not len(min_cut) == 3:
            print('minimum cut is not length 3!')
        for cut in min_cut:
            self.G.remove_edge(cut[0], cut[1])
        start = list(G.nodes)[0]
        self.connected = set()
        self.add_connected(start)
        
        self.result1 = len(self.connected) * (len(G.nodes) - len(self.connected))
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        # lines = self.parse_lines()
        self.result2 = None
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='25', simple=True)
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

# =============================================================================
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2()
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# =============================================================================

