import math
import random
import heapq

def euclidean_distance(initialState): #2d list
    distance = 0
    goal_positions = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2)
    }
    for i in range(3):
        for j in range(3):
            value = initialState[i][j]
            if value != 0:
                goal_i, goal_j = goal_positions[value]
                distance += math.sqrt((abs(i - goal_i)) ** 2+ (abs(j - goal_j)) ** 2) #calcuting euclidian distance
    return distance
def manhattan_distance(state: tuple[tuple[int]]) -> int:
    """Return total Manhattan distance for the 8-puzzle."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:  # skip the blank tile
                goal_x = (value) // 3
                goal_y = (value) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


# ---------- Helper to Find Blank Position ----------
def find_blank(state: list[list[int]]) -> tuple[int, int]:
    """Return coordinates (x, y) of the blank tile (0)."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# ---------- Generate Neighbor States ----------
def neighbors(state: tuple[tuple[int]]) -> list[tuple[tuple[int]]]:
    """Return all valid neighboring states (as tuples)."""
    # Convert immutable tuple back to mutable list
    state = [list(row) for row in state]
    x, y = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    result = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            # Swap blank with adjacent tile
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            result.append(tuple(tuple(r) for r in new_state))  # convert to immutable tuple
    return result


# ---------- A* Algorithm ----------
def A_star(initialState: list[list[int]], goalState: list[list[int]]):
    """Perform A* search and return path from start to goal."""
    start = tuple(tuple(r) for r in initialState)
    goal = tuple(tuple(r) for r in goalState)

    pq = []
    heapq.heappush(pq, (manhattan_distance(start), 0, start, [start]))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path  # found solution!

        for neighbor in neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None
def A_star_Euc(initialState: list[list[int]], goalState: list[list[int]]):
    """Perform A* search and return path from start to goal."""
    start = tuple(tuple(r) for r in initialState)
    goal = tuple(tuple(r) for r in goalState)

    pq = []
    heapq.heappush(pq, (euclidean_distance(start), 0, start, [start]))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path  # found solution!

        for neighbor in neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + euclidean_distance(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None

