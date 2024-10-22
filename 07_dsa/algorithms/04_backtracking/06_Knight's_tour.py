

# Knight’s tour problem	Finding a sequence of moves by a knight on a chessboard such that 
# it visits every square exactly once.



def is_valid_move(x, y, board):
    """Check if (x, y) is a valid move on the board."""
    return (0 <= x < len(board) and
            0 <= y < len(board) and
            board[x][y] == -1)

def print_board(board):
    """Print the board."""
    for row in board:
        print(' '.join(str(cell).rjust(2, ' ') for cell in row))

def solve_knights_tour_util(board, curr_x, curr_y, movei, x_moves, y_moves):
    """Util function to solve the Knight's Tour problem."""
    if movei == len(board) * len(board):
        return True

    for i in range(8):
        next_x = curr_x + x_moves[i]
        next_y = curr_y + y_moves[i]
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = movei
            if solve_knights_tour_util(board, next_x, next_y, movei + 1, x_moves, y_moves):
                return True
            board[next_x][next_y] = -1  # Backtrack

    return False

def solve_knights_tour(start_x, start_y, board_size):
    """Solve the Knight's Tour problem starting from (start_x, start_y)."""
    board = [[-1 for _ in range(board_size)] for _ in range(board_size)]

    # Knight's move offsets
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    board[start_x][start_y] = 0

    if not solve_knights_tour_util(board, start_x, start_y, 1, x_moves, y_moves):
        print("Solution does not exist")
    else:
        print_board(board)

# Example usage
board_size = 8  # Chessboard size
start_x, start_y = 0, 0  # Starting position
solve_knights_tour(start_x, start_y, board_size)
