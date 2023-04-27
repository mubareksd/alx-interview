#!/usr/bin/python3
"""0-nqueens module that solves the N queens problem
"""
import sys


def nqueens(num):
    """nqueens function that solves the N queens problem

    Args:
        num (int): number of queens
    """
    board = [[0 for x in range(num)] for y in range(num)]
    solve_nqueens(board, 0, num)


def solve_nqueens(board, col, num):
    """solve_nqueens function that solves the N queens problem

    Args:
        board (list): board list
        col (int): column number
        num (int): number of queens in board

    Returns:
        bool: True if safe, False otherwise
    """
    if col == num:
        print_board(board)
        return True

    res = False
    for i in range(num):
        if is_safe(board, i, col, num):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, num) or res
            board[i][col] = 0
    return res


def is_safe(board, row, col, num):
    """is_safe function that checks if a queen can be placed on board

    Args:
        board (list): board list
        row (int): row number
        col (int): column number
        num (int): number of queens in board

    Returns:
        bool: True if safe, False otherwise
    """
    safe_row = row
    safe_col = col
    while safe_col >= 0 and safe_row < num:
        if board[safe_row][safe_col] == 1:
            return False
        safe_row += 1
        safe_col -= 1

    safe_row = row
    safe_col = col
    while safe_row >= 0 and safe_col >= 0:
        if board[safe_row][safe_col] == 1:
            return False
        safe_row -= 1
        safe_col -= 1

    for i in range(col):
        if board[row][i] == 1:
            return False
    return True


def print_board(board):
    """print_board function that prints the board

    Args:
        board (list): board list
    """
    print([[i, j] for i in range(
        len(board)) for j in range(len(board)) if board[i][j] == 1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        NUM = int(sys.argv[1])
        if NUM < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(NUM)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
