"""
dfs_nopath.py:

this file provides a search function for solving 2d mazes using depth first 
search (DFS), breadth first search (BFS), and A* search algorithms. The search 
function takes the start state, goal check function, next states function, and 
search type as arguments.

the manhattan distance was used because it provides a better estimate of the 
goal which helps for efficiency. the algorithm would be more efficient if the a* 
algorithm and the manhattan distance were used together.

Functions:
    - search(start_state, is_goal, next_states, search_type='DFS')
    - heuristic_algo(state)

__author__ = Marko Vockic, 000350323
"""
from queue import LifoQueue, Queue, PriorityQueue

def search(start_state, is_goal, next_states, search_type='DFS'):
    """
    perform a search to solve a maze using DFS, BFS, and A* algorithm.

    Args:
        start_state (tuple): the starting state of the maze
        
        is_goal (function): a function that checks if the current state is the 
        goal state
        
        next_states (function): a function that returns a list of possible next 
        states from the current state
        
        search_type (str): The search algorithm to use. Options are 'DFS', 
        'BFS', or 'A*'. default is set to'DFS'

    Returns:
        list: a list of states representing the solution path, or none if no 
        solution is found.
    """
    closed = []
    start_node = (start_state, [], 0)  # state, path, cost
    
    if search_type == 'DFS':
        open = LifoQueue()
    elif search_type == 'BFS':
        open = Queue()
    elif search_type == 'AFS':
        open = PriorityQueue()

    if search_type == 'AFS':
        heuristic = heuristic_algo(start_state)
        open.put((heuristic, start_node))
    else:
        open.put(start_node)

    while not open.empty():
        if search_type in ['DFS', 'BFS']:
            node = open.get()
        elif search_type == 'AFS':
            _, node = open.get()

        state, path, cost = node
        maze, position = state
        
        frozen_maze = tuple(tuple(row) for row in maze)
        
        if (frozen_maze, position) in closed:
            continue
        closed.append((frozen_maze, position))

        if is_goal(state):
            return path + [state]

        for next_state in next_states(state):
            next_maze, next_position = next_state
            frozen_next_maze = tuple(tuple(row) for row in next_maze)
            
            if (frozen_next_maze, next_position) not in closed:
                next_cost = cost + 1
                next_node = (next_state, path + [state], next_cost)
                if search_type == 'AFS':
                    heuristic = next_cost + heuristic_algo(next_state)
                    open.put((heuristic, next_node))
                else:
                    open.put(next_node)
    return None


def heuristic_algo(state):
    """
    calculates the distance between the current position in the maze and the 
    top row using the manhattan distance

    Args:
        state (tuple): the current state of the maze

    Returns:
        int: the manhattan distance
    """
    _, position = state
    y, _ = position
    return abs(y - 1)