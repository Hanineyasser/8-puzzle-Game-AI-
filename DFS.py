from collections import deque
from helperFuncs import neighbors

def dfs(initial_state, goal_state):
    stack = deque([(initial_state, [initial_state], 0)])  # (state, path, depth)
    visited = set()
    visited.add(tuple(tuple(row) for row in initial_state))
    
    while stack:
        state, path, depth = stack.pop()
        if tuple(tuple(row) for row in state) == tuple(tuple(row) for row in goal_state):
            return path
        
        
        for new_state in neighbors(state):
            s_new = tuple(tuple(row) for row in new_state)
            if s_new not in visited:
                visited.add(s_new)
                stack.append((new_state, path + [new_state], depth + 1))
    return None




