#!/usr/bin/python3
'''
Solves the N-queens puzzle.
'''
import sys


def init_board(n):
    '''Initialize an `n`x`n` sized chessboard with 0's.'''
    chessboard = []
    [chessboard.append([]) for c in range(n)]
    [row.append(' ') for c in range(n) for row in chessboard]
    return (chessboard)


def board_deepcopy(chessboard):
    '''Return a deepcopy of a chessboard.'''
    if type(chessboard) is list:
        return list(map(board_deepcopy, chessboard))
    return (chessboard)


def get_solution(chessboard):
    '''Return the list of lists representation of a solved chessboard.'''
    solution = []
    for row in range(len(chessboard)):
        for chess in range(len(chessboard)):
            if chessboard[row][chess] == "Q":
                solution.append([row, chess])
                break
    return (solution)


def X_ed_out(cboard, row, col):
    '''In chess notation, the positions on a chessboard are typically identified by a combination of a letter and a number. The letters represent the columns, labeled from 'a' to 'h' from left to right, and the numbers represent the rows, labeled from 1 to 8 from bottom to top.
    Xout spots on a chessboard is use to denote capture.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    For example:
    'a1' is the bottom left square on the board.
    'h1' is the bottom right square.
    'a8' is the top left square.
    'h8' is the top right square
    'x1' is the forward spot
    'x8' is the backword spot
    'c1' is the 
    Args:
        cboard (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.'''

    # Xed out forward spots
    for x1 in range(col + 1, len(cboard)):
        cboard[row][x1] = "x"
    # Xed out backwards spots
    for x8 in range(col - 1, -1, -1):
        cboard[row][x8] = "x"
    # Xed out spots below
    for h1 in range(row + 1, len(cboard)):
        cboard[h1][col] = "x"
    # Xed out spots above
    for a8 in range(row - 1, -1, -1):
        cboard[a8][col] = "x"
    # Xed out spots diagonally down to the right
    c1 = col + 1
    for h8 in range(row + 1, len(cboard)):
        if c1 >= len(cboard):
            break
        cboard[h8][c1] = "x"
        c1 += 1
    # Xed out spots diagonally up to the left
    c1 = col - 1
    for h8 in range(row - 1, -1, -1):
        if c1 < 0:
            break
        cboard[h8][c1]
        c1 -= 1
    # Xed out spots diagonally up to the right
    c1 = col + 1
    for h8 in range(row - 1, -1, -1):
        if c1 >= len(cboard):
            break
        cboard[h8][c1] = "x"
        c1 += 1
    # Xed out spots diagonally down to the left
    c1 = col - 1
    for r in range(row + 1, len(cboard)):
        if c1 < 0:
            break
        cboard[r][c1] = "x"
        c1 -= 1


def recursive_chess(board, row, queens, solutions):
    '''Recursively solve an N-queens puzzle.
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    '''
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            curent_board = board_deepcopy(board)
            curent_board[row][c] = "Q"
            X_ed_out(curent_board, row, c)
            solutions = recursive_chess(curent_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_chess(board, 0, 0, [])
    for answe in solutions:
        print(answe)
