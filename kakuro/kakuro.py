from copy import deepcopy
from typing import List


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
    return


def _get_possible_values_for_cells(sum, cells):
    allowed_numbers = _get_allowed_numbers(sum, len(cells))
    possible_solutions = []
    done = False
    while not done:
        possible_solution = deepcopy(cells)
        # TODO: continue


def solve(board, sums_horizontal, sums_vertical):
    print(f"Solving board...")
    solved_something = True
    while not is_solved(board) and solved_something:
        solved_something = False  # If we didn't solve anything the last time, stop and quit.

        for i, h_row_sums in enumerate(sums_horizontal):
            for sum_i, h_sum in enumerate(h_row_sums):
                row = board[i]
                cells = _get_cells(row, sum_i)
                possible_values = _get_possible_values_for_cells(h_sum, cells)

    print(f"Board is unsolveable!")
