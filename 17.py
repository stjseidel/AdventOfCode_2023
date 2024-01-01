# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:32:12 2023

@author: stjse
"""

from aoc_class import AOC
from timeit import default_timer as timer
from dijkstar import Graph, find_path

    
class Today(AOC):
    # def __init__(self, day):
    #     AOC.__init__(self, day)
        
    def parse_lines(self, file_path=''):
        lines = self.lines
        # lines = [[int(lin) for lin in line.split(' ') if set(lin) != set('') ] for line in lines]
        
        self.nodes = {}
        for y, line in enumerate(lines):
            for x, value in enumerate(line):
# =============================================================================
#                 if value == 'S':
#                     startPoint = (x, y)
#                     print('Found start Point:', startPoint)
#                 elif value == 'E':
#                     target = (x, y)
#                     print('Found target Point:', target)
# =============================================================================
                # self.nodes[(x, y)] = heights[value]
                self.nodes[(x, y)] = int(value)
        

        return lines
    
    def part1(self):
        lines = self.parse_lines()
        start = (0, 0)
        target = (len(lines)-1, len(lines[0])-1)
        grid = [[int(char) for char in line] for line in lines]
        
        
        # Convert the grid to a graph
        graph = self.grid_to_graph(grid)
        
        # Find the path using Dijkstra's algorithm
        result = find_path(graph, start, target)
        
        if result.total_cost != float('inf'):
            print("The minimum path cost to reach the target is:", result.total_cost)
            print("The chosen path is:", result.nodes)
        else:
            print("The target is not reachable.")
        
        

        result = self.dijkstra_with_limit(grid, start, target, max_straight_moves=3)
        print(result)
        result, path = self.dijkstra_with_path(grid, start, target, max_straight_moves=3)
        print(result, path)
        
        if result != -1:
            import matplotlib.pyplot as plt
            import numpy as np
            print("The minimum path cost to reach the target is:", result)
            print("The chosen path is:", path)
            
            # Plot the grid and the chosen path
            grid_array = np.array(grid)
            plt.imshow(grid_array, cmap='viridis', interpolation='nearest', origin='upper')
            
            path_array = np.array(path)
            plt.plot(path_array[:, 1], path_array[:, 0], color='red', marker='o')
            
            plt.scatter(start[1], start[0], color='green', marker='o', label='Start')
            plt.scatter(target[1], target[0], color='blue', marker='o', label='Target')
            
            plt.legend()
            plt.show()
            
        else:
            print("The target is not reachable within the specified limitation.")

        self.result1 = result
        self.time1 = timer()
        return self.result1


    def dijkstra_with_limit(self, grid, start, target, max_straight_moves):
        import heapq
        rows, cols = len(grid), len(grid[0])
        
        # Possible moves: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Priority queue to store nodes with their cumulative cost
        priority_queue = [(0, start, 0)]  # (cost, current, consecutive_moves)
        
        # Dictionary to store the minimum cost to reach each cell
        min_cost = {start: 0}
        
        while priority_queue:
            cost, current, consecutive_moves = heapq.heappop(priority_queue)
            
            # Check if the current node is the target
            if current == target:
                return cost
            
            for direction in directions:
                x, y = current[0] + direction[0], current[1] + direction[1]
                
                # Check if the new cell is within the grid
                if 0 <= x < rows and 0 <= y < cols:
                    # Check if the consecutive moves exceed the limit
                    if consecutive_moves < max_straight_moves:
                        # Calculate the new cost to reach the neighbor
                        new_cost = cost + grid[x][y]
                        
                        # Update the minimum cost if it's smaller
                        if (x, y) not in min_cost or new_cost < min_cost[(x, y)]:
                            min_cost[(x, y)] = new_cost
                            heapq.heappush(priority_queue, (new_cost, (x, y), consecutive_moves + 1))
                    else:
                        # Reset consecutive moves if the limit is reached
                        heapq.heappush(priority_queue, (cost + grid[x][y], (x, y), 1))
        
        # If the target is not reachable
        return -1
    
    

    def dijkstra_with_path(self, grid, start, target, max_straight_moves):
        import heapq
        rows, cols = len(grid), len(grid[0])
        
        # Possible moves: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Priority queue to store nodes with their cumulative cost
        priority_queue = [(0, start, 0)]  # (cost, current, consecutive_moves)
        
        # Dictionary to store the minimum cost to reach each cell
        min_cost = {start: 0}
        
        # Dictionary to store the previous cell for each cell in the path
        previous_cell = {start: None}
        
        while priority_queue:
            cost, current, consecutive_moves = heapq.heappop(priority_queue)
            
            # Check if the current node is the target
            if current == target:
                # Reconstruct the path
                path = []
                while current is not None:
                    path.append(current)
                    current = previous_cell[current]
                return cost, path[::-1]  # Reverse the path
                
            for direction in directions:
                x, y = current[0] + direction[0], current[1] + direction[1]
                
                # Check if the new cell is within the grid
                if 0 <= x < rows and 0 <= y < cols:
                    # Check if the consecutive moves exceed the limit
                    if consecutive_moves < max_straight_moves:
                        # Calculate the new cost to reach the neighbor
                        new_cost = cost + grid[x][y]
                        
                        # Update the minimum cost if it's smaller
                        if (x, y) not in min_cost or new_cost < min_cost[(x, y)]:
                            min_cost[(x, y)] = new_cost
                            previous_cell[(x, y)] = current
                            heapq.heappush(priority_queue, (new_cost, (x, y), consecutive_moves + 1))
                    else:
                        # Reset consecutive moves if the limit is reached
                        previous_cell[(x, y)] = current
                        heapq.heappush(priority_queue, (cost + grid[x][y], (x, y), 1))
        
        # If the target is not reachable
        return -1, []
    
    
    
    def grid_to_graph(self, grid):
        rows, cols = len(grid), len(grid[0])
        graph = Graph()
    
        for i in range(rows):
            for j in range(cols):
                current_node = (i, j)
                current_cost = grid[i][j]
    
                # Add connections to neighbors
                for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i + direction[0], j + direction[1]
    
                    # Check if the neighbor is within the grid
                    if 0 <= x < rows and 0 <= y < cols:
                        neighbor_node = (x, y)
                        neighbor_cost = grid[x][y]
    
                        # Add edge to the graph
                        graph.add_edge(current_node, neighbor_node, {'cost': int(neighbor_cost)})
    
        return graph
    
    

    def part2(self):
        lines = self.parse_lines()
        self.result2 = 'TODO'
        self.time2 = timer()
        return self.result2
        
    def print_final(self):
        print(f'Part 1 result is: {self.result1}. (time: {round(self.time1 - self.beginning_of_time, 2)})')
        print(f'Part 2 result is: {self.result2} (time: {round(self.time2 - self.time1, 2)})')
        


    def get_surroundings(self, node):
        north = (node[0], node[1]+1)
        south = (node[0], node[1]-1)
        west = (node[0]-1, node[1])
        east = (node[0]+1, node[1])
        valid = [n for n in [east, south, west, north] if n in self.nodes]
        close_enough = [v for v in valid if self.nodes[node] >= self.nodes[v] -1]
        return close_enough
    




            
    
if __name__ == '__main__':
# prep
    today = Today(day='17', simple=True)
    today.create_txt_files()

# simple part 1
    today.set_lines(simple=True)
    today.part1()
    print(f'Part 1 <SIMPLE> result is: {today.result1}')
    
# =============================================================================
# # hard part 1
#     today.set_lines(simple=False)
#     today.part1()
#     print(f'Part 1 <HARD> result is: {today.result1}')
#     today.stop()
# =============================================================================


# =============================================================================
# # simple part 2
#     today.set_lines(simple=True) 
#     today.part2()
#     print(f'Part 2 <SIMPLE> result is: {today.result2}')
# =============================================================================

# =============================================================================
# # hard part 2
#     today.set_lines(simple=False)
#     today.part2()
#     print(f'Part 2 <HARD> result is: {today.result2}')
#     today.stop()
#     today.print_final()
# =============================================================================
