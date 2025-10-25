# Import necessary libraries
from collections import deque
from helperFuncs import neighbors

# Depth-First Search to solve the 8-puzzle problem
def solve_puzzle_dfs(start, goal, depth_limit=None):

    stack = deque([(start, 0)])
    visited = set()

    start_tuple = tuple(map(tuple, start))
    goal_tuple = tuple(map(tuple, goal))

    # stack.append(PuzzleState(start, 0))
    visited.add(start_tuple)

    # parent pointers: child_tuple -> parent_tuple
    parent = {start_tuple: None}

    def reconstruct_path(end_tuple):
        path_tuples = []
        cur = end_tuple
        while cur is not None:
            path_tuples.append(cur)
            cur = parent.get(cur)
        path_tuples.reverse()
        print(f'Solution path length: {len(path_tuples)-1} moves')
        return [[list(row) for row in t] for t in path_tuples]

    while stack:
        curr , depth = stack.pop()


        curr_tuple = tuple(map(tuple, curr))

        print(f'Depth: {depth}')

        if depth_limit is not None and depth > depth_limit:
            continue

        if curr_tuple == goal_tuple:
            for visited_state in visited:
                print(visited_state)
            print(f'Total visited states: {len(visited)}')
            print(f'Goal state reached at depth {depth}')
            return reconstruct_path(curr_tuple)

        for new_board in neighbors(curr):
            board_tuple = tuple(map(tuple, new_board))
            if board_tuple not in visited:
                visited.add(board_tuple)
                parent[board_tuple] = curr_tuple
                stack.append((new_board, depth + 1))

    print('No solution found (DFS exhausted search space or reached depth limit)')

# Driver Code
if __name__ == '__main__':
    start = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    goal_state=[[0,1,2],[3,4,5],[6,7,8]]
    solve_puzzle_dfs(start, goal_state)