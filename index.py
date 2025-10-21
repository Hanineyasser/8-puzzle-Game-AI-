import random
import json
import os
from BreadthFS import Bfs
# from DFS import dfs


def is_solvable(array):
    # For 3x3 puzzle: solvable if number of inversions is even
                   #  to not return no solution
    inv = 0
    # making an array without the blank (0)-->to count the inversions in it 
                                            # cause we dont need to count the 0 
                                            # as it is not a number: it is just a blank slot
    arr = [x for x in array if x != 0]
    for i in range(len(arr)):
        # starting from the index after i
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0

# for the viewer(template) html file
def write_viewer(initial_state, steps, out_path):
    # join-->combine path components
    # os.path.dirname(__file__)-->returns the directory path of this file
    tpl_path = os.path.join(os.path.dirname(__file__), 'Viewer_template.html')
    # read the template file and store its content in tpl variable(a single string)
    # f-->the opened file object: to read or write to the file
    # encoding='utf-8'-->to support all characters and all languages 
    with open(tpl_path, 'r', encoding='utf-8') as f:
        tpl = f.read()
    # create a dictionary to hold the initial state and steps--> to convert to json later
    #                                               --> to be used in the viewer html file
    #  packages the initial puzzle and the steps together for easy use in your HTML viewer.
    data = {'initial': initial_state, 'steps': steps}
    # Use a variable for DATA in the template
    # replace the placeholder in the template with actual data-->variable data every run
    # json.dumps(data)-->convert python object to json string-->to be used in javascript in the viewer html file
    # using replace 2 times to cover both spacing cases
    content = tpl.replace('const DATA =', 'var DATA =').replace('{ data }', json.dumps(data)).replace('{data}', json.dumps(data))
    # to see the puzzle in the algos html files
    # it create a new html file with the viewer content
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
    # convert the flat list to a 2D list (3x3)
    # 3-->step size
    initial_state = [state[i:i+3] for i in range(0, 9, 3)]
    print("Initial State:")
    for row in initial_state:
        print(row)
    goal_state = [[0,1,2],[3,4,5],[6,7,8]]
    print("Goal State:")
    for row in goal_state:
        print(row)

    print("Choose algorithm:")
    print("1. BFS")
    print("2. DFS")
    print("3. A* (Manhattan)")
    print("4. A* (Euclidean)")
    # strip-->to remove any whitespace at the start or the end
    choice = input("Enter 1, 2, 3, 4 or 5: ").strip()
    if choice == '1':
        print("Using BFS algorithm to solve the puzzle.")
        steps = Bfs(initial_state, goal_state)
        algo_name = "BFS"
    elif choice == '2':
        print("Using DFS algorithm to solve the puzzle.")
        from DFS import dfs
        steps = dfs(initial_state, goal_state)
        algo_name = "DFS"
    elif choice == '3':
        print("Using IDS algorithm to solve the puzzle.")
        from IDFS import idfs
        steps = idfs(initial_state, goal_state)
        algo_name = "IDS"
    elif choice == '4':
        print("Using A* (Manhattan) algorithm to solve the puzzle.")
        from A import A_star
        steps = A_star(initial_state, goal_state)
        algo_name = "A_star_Manhattan"
    elif choice == '5':
        print("Using A* (Euclidean) algorithm to solve the puzzle.")
        from A import A_star_Euc
        steps = A_star_Euc(initial_state, goal_state)
        algo_name = "A_star_Euclidean"
    else:
        print("Invalid choice. Exiting.")

    if steps:
        print(f"Solution found in {len(steps)-1} moves")
    else:
        print("No solution found")
    # create the algos html with the folder path and the file name
    out_path = os.path.join(os.path.dirname(__file__), f'{algo_name}_viewer.html')
    # [initial_state] if no steps so that the html file isnt empty and shows the initial state
    write_viewer(initial_state, steps or [initial_state], out_path)
    # for checking
    print(f'Wrote viewer to: {out_path}')


if __name__ == '__main__':
    main()