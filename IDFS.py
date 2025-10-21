from DFS import dfs

def idfs(initial_state, goal_state, max_depth=600):
    # starting from 0 to max_depth, perform DFS with increasing depth limit
    for depth in range(max_depth + 1):
        result = dfs(initial_state, goal_state, max_depth=depth)
        # f->let u insert variable easily in a string
        print(f"IDS at depth {depth} completed.") 
        # returning the final result when we arrive to it
        if result is not None:
            return result
    return None
