

# Rat in a Maze	Finding a path from the starting position to the exit in a maze, with obstacles 
# represented as walls.


def is_safe_maze(maze, x, y, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

def solve_maze_util(maze, x, y, sol, n):
    if x == n-1 and y == n-1:
        sol[x][y] = 1
        return True

    if is_safe_maze(maze, x, y, n):
        sol[x][y] = 1

        if solve_maze_util(maze, x+1, y, sol, n):
            return True

        if solve_maze_util(maze, x, y+1, sol, n):
            return True

        sol[x][y] = 0
        return False

    return False

def solve_maze(maze):
    n = len(maze)
    sol = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_maze_util(maze, 0, 0, sol, n):
        print("No solution exists")
    else:
        for row in sol:
            print(row)

# Example maze
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze)


