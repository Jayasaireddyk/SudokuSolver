
def print_board(board):
    print("\nSolved Sudoku Puzzle:\n")

    for row in board:
        for num in row:
            print(num, end=" ")
        print()

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, num, pos):
    row, col = pos
    
    for x in range(9):
        if board[row][x] == num and x != col:
            return False

    for x in range(9):
        if board[x][col] == num and x != row:
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)

    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            # Backtrack
            board[row][col] = 0

    return False

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


print("Sudoku Puzzle Solving...\n")

if solve(board):
    print_board(board)
else:
    print("No Solution Found!")