#Using the BFS to solve the 8 puzzle game
# using queue data structure
from collections import deque
from helperFuncs import neighbors
def Bfs(initial_state, goal_state):
    queue = deque([(initial_state, [initial_state])])
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        for neighbor in neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append((neighbor, path + [neighbor]))
    return None