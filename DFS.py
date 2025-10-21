from collections import deque
from helperFuncs import neighbors
import random
from index import is_solvable



def dfs(initial_state, goal_state, max_depth=20):
    stack = deque([(initial_state, [initial_state], 0)])  # (state, path, depth)
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))  # Convert to tuple only for visited set

    while stack:
        state, path, depth = stack.pop()
        if state == goal_state:
            return path
        if depth >= max_depth:
            continue
        for new_state in neighbors(state):  # new_state should be a list
            neighbor_tuple = tuple(map(tuple, new_state))  # Convert to tuple only for checking
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                stack.append((new_state, path + [new_state], depth + 1))
    return None



# def test_dfs():
#     state = [0,1,2,3,4,5,6,7,8]
#     # shuffle until we pick a solvable state so BFS has a solution to show
#     attempts = 0
#     while True:
#         random.shuffle(state)
#         attempts += 1
#         flat = state[:]
#         if is_solvable(flat):
#             break
#         if attempts >= 1000:
#             # fallback: accept current state (rare)
#             break
#     print(state)
#     initial_state = [state[i:i+3] for i in range(0, 9, 3)]
#     print("Initial State:")
#     for row in initial_state:
#         print(row)
#     goal_state = [[0,1,2],[3,4,5],[6,7,8]]
#     print("Goal State:")
#     for row in goal_state:
#         print(row)



#     print("Use Dfs algorithm to solve the puzzle.")
#     steps = dfs(initial_state, goal_state)
#     if steps:
#         print(f"Solution found in {len(steps)-1} moves")
#     else:
#         print("No solution found")


# if __name__ == "__main__":
#     test_dfs()