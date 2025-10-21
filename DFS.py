from collections import deque
from helperFuncs import neighbors

def dfs(initial_state, goal_state, depth_limit=None):
    stack = deque([(initial_state, [initial_state], 0)])  # (state, path, depth)
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))  # Convert to tuple only for visited set

    while stack:
        state, path, depth = stack.pop()
        # print(f"DFS at depth {depth}")
        if state == goal_state:
            return path
        if depth_limit is not None and depth >= depth_limit:
            continue
        for new_state in neighbors(state):  # new_state should be a list
            neighbor_tuple = tuple(map(tuple, new_state))  # Convert to tuple only for checking
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                stack.append((new_state, path + [new_state], depth + 1))
    return None

if __name__ == "__main__":
    # Example usage
    initial_state = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    result = dfs(initial_state, goal_state)
    if result:
        print(f"Solution found in {len(result)-1} moves")
    else:
        print("No solution found")
