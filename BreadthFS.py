#Using the BFS to solve the 8 puzzle game
# using queue data structure
from collections import deque
from helperFuncs import neighbors
def Bfs(initial_state, goal_state):
    # BFS-->queue data structure
    # queue takes--> (state, path to arrive to this state)
    queue = deque([(initial_state, [initial_state])])
    visited = set()
    # add the initial state to the visited set
    # initial_state-->2D array can't be added to a set directly
    # tuple-->immutable, ordered collection-->can't change its contents
    # we convert each row to a tuple, then the whole state to a tuple of tuples
    # result-->getting a hashable representation of the state, that can be added to a set
    visited.add(tuple(map(tuple, initial_state)))
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            for visited_stage in visited:
                print(visited_stage)
            print("Visited States of len:", len(visited))
            print("depth and moves of goal state:", len(path)-1)
            
            return path
        for neighbor in neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                # path + the neighbor's state-->path from start to neighbor
                queue.append((neighbor, path + [neighbor]))
    
    return None