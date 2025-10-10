# Function to find the position of the blank (0) tile
def findBlank(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return None
# Function to generate possible moves from the current state
def neighbors(state):
    neighbors = []
    x, y = findBlank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # copy the matrix to not affect the old one when swapping
            new_state = [row[:] for row in state]
            # swap the blank with the adjacent tile
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors
