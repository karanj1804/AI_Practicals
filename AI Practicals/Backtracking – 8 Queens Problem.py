N = 8


def print_board(board):
    for row in board:
        for col in row:
            print("Q" if col == 1 else ".", end=" ")
        print()


def is_safe(board, row, col):

    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve(board, row + 1):
                return True

            board[row][col] = 0

    return False


board = [[0 for _ in range(N)] for _ in range(N)]

if solve(board, 0):
    print("Solution for 8 Queens:")
    print_board(board)
else:
    print("Solution Does Not Exist")