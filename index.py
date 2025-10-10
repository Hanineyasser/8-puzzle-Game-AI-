import random
from BreadthFS import Bfs 
# this is the main
print("Solve this 8 puzzle")
print("Initial State: ")
state = [0,1,2,3,4,5,6,7,8]
random.shuffle(state)
print(state)
initial_state = [state[i:i+3] for i in range(0, 9, 3)]
print("Initial State:")
for row in initial_state:
    print(row)
goal_state = [[0,1,2],[3,4,5],[6,7,8]]
print("Goal State:")
for row in goal_state:
    print(row)
print("Use BFS algorithm to solve the puzzle.")
solution = Bfs(initial_state, goal_state)
if solution:
    print(f"Solution found in {len(solution)-1} moves:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")