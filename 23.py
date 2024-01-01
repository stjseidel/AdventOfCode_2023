# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
import sys
import re

class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        return lines
                
    def longest_path(self, grid):
        def is_valid(x, y, direction):
            if not (0 <= x < rows and 0 <= y < cols and grid[x][y] != '#' and not visited[x][y]):
                return False
            if grid[x][y] in '^>v<' and direction == opposite_directions[grid[x][y]]:
                return False
            return True
    
        def dfs(x, y, direction, length):
            nonlocal max_length
    
            # Mark the current cell as visited
            visited[x][y] = True
    
            # Explore in the permissible direction
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
    
            if is_valid(nx, ny, direction):
                dfs(nx, ny, direction, length + 1)
    
            # Explore in all other permissible directions
            for new_direction in (direction + 1) % 4, (direction + 3) % 4:
                dx, dy = directions[new_direction]
                nx, ny = x + dx, y + dy
    
                if is_valid(nx, ny, new_direction):
                    dfs(nx, ny, new_direction, length + 1)
    
            # Backtrack
            if visited[-1][target_col]:
                print(length - 1, max_length -1)
                max_length = max(max_length, length)
            visited[x][y] = False
    
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
        opposite_directions = {'^': 2, '>': 3, 'v': 0, '<': 1}  # Mapping opposite directions
    
        max_length = 0
        visited = [[False] * cols for _ in range(rows)]
    
        # Find the starting cell in the top row
        start_col = grid[0].index('.')
        target_col = grid[-1].index('.')
    
        # Start DFS from the top row
        dfs(0, start_col, 2, 1)  # Start by going down
    
        return max_length - 1


    def part1(self):
        lines = self.parse_lines()
        result = self.longest_path(lines)
        print("Longest path length:", result)
        self.result1 = result
        self.time1 = timer()
        return self.result1
                
    def part2(self):
        lines = self.parse_lines()
        symbols_to_replace = "^>v<"
        pattern = re.compile(f"[{re.escape(symbols_to_replace)}]")
        # Use re.sub to replace matched symbols with '.'
        lines = [pattern.sub('.', line) for line in lines]
        result = self.longest_path(lines)
        print("Longest path length:", result)
        self.result2 = result
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        

if __name__ == '__main__':
# prep
    today = Today(day='23', simple=True)
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


    sys.setrecursionlimit(7000)
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

