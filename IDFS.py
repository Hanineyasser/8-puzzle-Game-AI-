from DFS import dfs

def idfs(initial_state, goal_state):
    depth = 0
    while True:
        result = dfs(initial_state, goal_state, depth_limit=depth)
        # f->let u insert variable easily in a string
        print(f"IDS at depth {depth} completed.") 
        depth += 1
        # returning the final result when we arrive to it
        if result is not None:
            return result
    return None
