from copy import deepcopy
from pprint import pprint
from typing import List

from kakuro.cheat_sheet import cheat_sheet


def is_solved(board):
    print(f"Checking if board is solved...")
    for row in board:
        for cell in row:
            if cell != 'x' and cell == 0:
                return False
    return True


def _get_cell_groups(row):
    groups = []
    cur_group = []
    for cell in row:
        if cell != 'x':
            cur_group.append(cell)
        else:
            if cur_group:
                groups.append(cur_group)
            cur_group = []
    if cur_group:
        groups.append(cur_group)
    return groups


def _get_cells(row, si):
    cell_groups = _get_cell_groups(row)
    return cell_groups[si]


def _get_allowed_numbers(sum: int, n: int) -> List[int]:
    if n == 1:
        return [sum]
    return cheat_sheet[n][sum]


def _get_possible_values_for_cells(sum, cells):
    allowed_numbers = _get_allowed_numbers(sum, len(cells))
    new_cells = []
    for c in cells:
        new_c = c
        if c == 0:
            new_c = allowed_numbers
        elif isinstance(c, list):
            new_c = [n for n in c if n in allowed_numbers]
        new_cells.append(new_c)
    return new_cells


def _get_start_index_of_group(row, group_number):
    cur_group_number = 0
    cur_in_block = True
    for cell_i, cell in enumerate(row):
        if cell == 'x':
            if not cur_in_block:
                cur_group_number += 1
        else:
            if cur_group_number == group_number:
                return cell_i
            cur_in_block = False
    raise Exception(f"Could not get_start_index_of_group with row={row}, group_number={group_number}")


def _set_cell_horizontal(board, row_i, group_number, possible_values):
    start_index = _get_start_index_of_group(board[row_i], group_number)
    for j in range(start_index, start_index + len(possible_values)):
        pv_i = start_index - j
        board[row_i][j] = possible_values[pv_i]
    return board


def _set_cell_vertical(board, col_i, group_number, possible_values):
    col = [row[col_i] for row in board]
    start_index = _get_start_index_of_group(col, group_number)
    for j in range(start_index, start_index + len(possible_values)):
        pv_i = start_index - j
        board[j][col_i] = possible_values[pv_i]
    return board


def print_board(board):
    def get_cell_for_print(cell):
        if cell == 0 or len(cell) == 9:  # All numbers
            return '         '
        if isinstance(cell, str):
            return '    x    '

        cell_str = ''
        for n in range(1, 10):
            if n in cell:
                cell_str += str(n)
            else:
                cell_str += ' '
        return cell_str

    print(f"--<board>--")

    for row in board:
        for cell in row:
            print(" | ", end='')
            print(get_cell_for_print(cell), end='')
        print(" | ")


    print(f"--</board>--")


def solve(board, sums_horizontal, sums_vertical):
    print(f"Solving board...")
    print_board(board)
    solved_something = True
    while not is_solved(board) and solved_something:
        solved_something = False  # If we didn't solve anything the last time, stop and quit.

        for row_i, h_row_sums in enumerate(sums_horizontal):
            print(f"Solving row={row_i}")
            for sum_i, h_sum in enumerate(h_row_sums):
                row = board[row_i]
                cells = _get_cells(row, sum_i)
                possible_values = _get_possible_values_for_cells(h_sum, cells)
                if cells != possible_values:
                    solved_something = True
                board = _set_cell_horizontal(board, row_i, sum_i, possible_values)
                print_board(board)

        for col_i, v_row_sums in enumerate(sums_vertical):
            print(f"Solving col={col_i}")
            if col_i == 1:
                print(f"something goes wrong here...")
            for sum_i, v_sum in enumerate(v_row_sums):
                col = [row[col_i] for row in board]
                cells = _get_cells(col, sum_i)
                possible_values = _get_possible_values_for_cells(v_sum, cells)
                if cells != possible_values:
                    solved_something = True
                board = _set_cell_vertical(board, col_i, sum_i, possible_values)  # <--- vertical
                print_board(board)

    print(f"Board is unsolveable!")
