"""
main.py

this file is the main method for solving mazes using DFS, BFS, and A* search 
algorithms. It generates a random maze of the given size and then finds and 
displays the solution paths for each search algorithm along with the path length
and time taken to find the solution

To run the script, simply execute it in the command line:
    python main.py

The user will be prompted to enter the height and width of the maze.

Functions:
    - is_goal(state)
    - next_states(state)
    - print_maze_with_solution(maze, solution_path)
    - main

__author__ = Marko Vockic, 000350323
"""
from time import time
from dfs_nopath import search
from prim_maze_generator import generate_maze, print_maze

def is_goal(state):
    maze, position = state
    return position[0] == len(maze) - 1

def next_states(state):
    maze, position = state
    y, x = position
    neighbors = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    
    valid_neighbors = []
    for y_new, x_new in neighbors:
        if 0 <= y_new < len(maze) and 0 <= x_new < len(maze[0]) and maze[y_new][x_new] == 'c':
            valid_neighbors.append((maze, (y_new, x_new)))
    return valid_neighbors

def find_start(maze):
    for i, cell in enumerate(maze[0]):
        if cell == 'c':
            return (0, i)
    return None

def print_maze_with_solution(maze, solution_path):
    if not solution_path:
        print("No solution.")
        return

    for state in solution_path[1:-1]:
        _, position = state
        y, x = position
        maze[y][x] = '*'
    print_maze(maze)
    for state in solution_path[1:-1]:
        _, position = state
        y, x = position
        maze[y][x] = 'c'

def main():
    height = int(input("Enter the height of the maze: "))
    width = int(input("Enter the width of the maze: "))

    maze = generate_maze(height, width, multipath=True)
    start_position = find_start(maze)
    start_state = (maze, start_position)

    for search_type in ['DFS', 'BFS', 'AFS']:
        start_time = time()
        solution_path = search(start_state, is_goal, next_states, search_type)
        end_time = time()

        print()
        print(f"{search_type} solution:")
        print_maze_with_solution(maze, solution_path)
        print(f"Path: {len(solution_path)}")
        print(f"Time: {end_time - start_time} seconds")
        print()

if __name__ == "__main__":
    main()
