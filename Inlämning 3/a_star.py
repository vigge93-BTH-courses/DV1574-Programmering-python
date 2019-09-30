'''Module for utilizing A* on a 2D grid.'''
import math
from grid import Occupation


def a_star(grid, start, goal):
    '''Function to calculate a path through a grid.'''
    # Create a dictionary with the non-blocked nodes
    available_nodes = {}
    for i, col in enumerate(grid):
        for j, state in enumerate(col):
            if state != Occupation.BLOCKED:
                available_nodes[(i, j)] = state

    # Initialize sets
    open_set = {start: Occupation.START}
    closed_set = {}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while len(open_set) > 0:
        # Get the next node with the lowest f-score that is in the open set
        current = min([x for x in f_score if x in open_set],
                      key=lambda x: f_score[x])

        # We have reached the goal, return the reconstructed path
        if current == goal:
            return reconstruct_path(came_from, current)

        # Move the current node from the open set to the closed set
        del open_set[current]
        closed_set[current] = grid[current[0]][current[1]]

        # Get all the non-blocked neighbors not in the closed set
        neighbors = {}
        for i in range(-1, 2):
            for j in range(-1, 2):
                node = (current[0] + i, current[1] + j)
                # Only consider the horizontal and vertical neighbors
                if not i == j and not i * j != 0:
                    if node in available_nodes and node not in closed_set:
                        neighbors[node] = available_nodes[node]

        for neighbor in neighbors:
            # Calculate new g-score
            tentative_g_score = g_score[current] + 1

            # If g-score is better than previous g-scores,
            # or the node doesn't have a previous g-score,
            # update the path
            if neighbor not in g_score \
                    or tentative_g_score < g_score[neighbor]:
                # Update the path and g-score
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score

                # Calculate new f-score
                f_score[neighbor] = g_score[neighbor] \
                    + heuristic(neighbor, goal)

                # Ensure neighbor is in the open set
                if neighbor not in open_set:
                    open_set[neighbor] = neighbors[neighbor]
    # If no path is found, return None
    return None


def heuristic(node, goal):
    '''Calculates the manhattan distance from the current node to the goal.'''
    # |x1 - x2| + |y1 - y2|
    dist = abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    return dist


def reconstruct_path(came_from, current):
    '''Reconstructs the path by working backwards'''
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path
