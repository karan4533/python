from heapq import heappush, heappop

# Function to find the index of a value in the puzzle
def find_index(puzzle, value):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == value:
                return i, j

# Function to calculate the  distance heuristic
def manhattan_distance(puzzle):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                x_goal, y_goal = divmod(puzzle[i][j] - 1, 3)
                distance += abs(x_goal - i) + abs(y_goal - j)
    return distance

# Function to get possible moves
def get_moves(puzzle):
    moves = []
    x, y = find_index(puzzle, 0)
    if x > 0:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[x][y], new_puzzle[x - 1][y] = new_puzzle[x - 1][y], new_puzzle[x][y]
        moves.append(new_puzzle)
    if x < 2:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[x][y], new_puzzle[x + 1][y] = new_puzzle[x + 1][y], new_puzzle[x][y]
        moves.append(new_puzzle)
    if y > 0:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[x][y], new_puzzle[x][y - 1] = new_puzzle[x][y - 1], new_puzzle[x][y]
        moves.append(new_puzzle)
    if y < 2:
        new_puzzle = [row[:] for row in puzzle]
        new_puzzle[x][y], new_puzzle[x][y + 1] = new_puzzle[x][y + 1], new_puzzle[x][y]
        moves.append(new_puzzle)
    return moves

# Function to check if a puzzle is the goal state
def is_goal(puzzle):
    return puzzle == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Function to solve the 8-puzzle problem using A* algorithm
def solve(puzzle):
    frontier = [(manhattan_distance(puzzle), 0, puzzle)]
    came_from = {}
    cost_so_far = {str(puzzle): 0}

    while frontier:
        _, cost, current = heappop(frontier)

        if is_goal(current):
            path = []
            while str(current) in came_from:
                path.append(current)
                current = came_from[str(current)]
            path.append(current)
            path.reverse()
            return path

        for next_state in get_moves(current):
            new_cost = cost + 1
            if str(next_state) not in cost_so_far or new_cost < cost_so_far[str(next_state)]:
                cost_so_far[str(next_state)] = new_cost
                priority = new_cost + manhattan_distance(next_state)
                heappush(frontier, (priority, new_cost, next_state))
                came_from[str(next_state)] = current

    return None

# Example initial puzzle
initial_puzzle = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

# Solve the puzzle
solution = solve(initial_puzzle)

# Print the solution steps
if solution:
    print("Solution steps:")
    for step, puzzle in enumerate(solution):
        print("Step", step + 1)
        for row in puzzle:
            print(row)
        print()
else:
    print("No solution found.")
