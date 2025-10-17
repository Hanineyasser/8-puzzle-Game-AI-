import random
import json
import os
from BreadthFS import Bfs
from DFS import dfs


def is_solvable(flat_state):
    # For 3x3 (odd width) puzzle: solvable if number of inversions is even
    inv = 0
    arr = [x for x in flat_state if x != 0]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0


def write_viewer(initial_state, steps, out_path):
    tpl_path = os.path.join(os.path.dirname(__file__), 'BFS_viewer_template.html')
    with open(tpl_path, 'r', encoding='utf-8') as f:
        tpl = f.read()
    data = {'initial': initial_state, 'steps': steps}
    content = tpl.replace('{data}', json.dumps(data))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    print("Solve this 8 puzzle")
    print("Initial State: ")
    state = [0,1,2,3,4,5,6,7,8]
    # shuffle until we pick a solvable state so BFS has a solution to show
    attempts = 0
    while True:
        random.shuffle(state)
        attempts += 1
        flat = state[:]
        if is_solvable(flat):
            break
        if attempts >= 1000:
            # fallback: accept current state (rare)
            break
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
    steps = Bfs(initial_state, goal_state)
    if steps:
        print(f"Solution found in {len(steps)-1} moves")
    else:
        print("No solution found")

     


    out_path = os.path.join(os.path.dirname(__file__), 'BFS_viewer.html')
    write_viewer(initial_state, steps or [initial_state], out_path)
    print(f'Wrote viewer to: {out_path}')


if __name__ == '__main__':
    main()