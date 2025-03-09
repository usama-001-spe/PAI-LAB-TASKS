def is_safe(board, row, col, n):
 
    for i in range(row):
        if board[i][col] == 'q':
            return False


    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 'q':
            return False

  
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 'q':
            return False

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([''.join(row) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'q'
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = '.'  

def print_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
    print()

def main():
    n = int(input("Enter the size of the chessboard: "))
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print_board(solutions[0])
    
   


main()
