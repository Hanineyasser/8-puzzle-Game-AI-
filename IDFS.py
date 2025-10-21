from DFS import dfs

def idfs(initial_state, goal_state, max_depth=600):
    for depth in range(max_depth + 1):
        result = dfs(initial_state, goal_state, max_depth=depth)
        print(f"IDS at depth {depth} completed.") 
        if result is not None:
            return result
    return None
