from copy import deepcopy
from unittest import TestCase

from kakuro.kakuro import solve, is_solved, _get_cell_groups, _get_possible_values_for_cells, _get_allowed_numbers, \
    _set_cell_horizontal, _get_start_index_of_group


board1 = [
    ['x', 'x', 0, 0],
    ['x', 0, 0, 0],
    [0, 0, 0, 'x'],
    [0, 0, 'x', 'x'],
]
sums_horizontal1 = [[11], [11], [24], [17]]
sums_vertical1 = [[16], [20], [11], [16]]

solution1 = [
    ['x', 'x', 2, 9],
    ['x', 3, 1, 7],
    [7, 9, 8, 'x'],
    [9, 8, 'x', 'x'],
]


class KakuroSolverTestCase(TestCase):
    def test_is_solved(self):
        result = is_solved(board1)
        self.assertFalse(result)

        result = is_solved(solution1)
        self.assertTrue(result)

    def test_solve(self):
        result = solve(board1, sums_horizontal1, sums_vertical1)
        self.assertEqual(solution1, result)


    def test_get_cell_groups(self):
        row = [1, 2, 3, 'x', 4, 5]
        expected = [[1, 2, 3],[4, 5]]
        result = _get_cell_groups(row)
        self.assertEqual(expected, result)

        row = [1, 2, 3, 'x']
        expected = [[1, 2, 3]]
        result = _get_cell_groups(row)
        self.assertEqual(expected, result)

        row = ['x', 1, 2, 3]
        expected = [[1, 2, 3]]
        result = _get_cell_groups(row)
        self.assertEqual(expected, result)

    def test_get_possible_values_for_cells(self):
        self.assertEqual([[8, 9], [8, 9]], _get_possible_values_for_cells(17, [0, 0]))
        self.assertEqual([[1, 2, 3, 4], [1, 2, 3, 4]], _get_possible_values_for_cells(5, [0, 0]))
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual([vals, vals, vals], _get_possible_values_for_cells(11, [0, 0, 0]))

    def test_get_allowed_numbers(self):
        self.assertEqual([8, 9], _get_allowed_numbers(17, 2))
        self.assertEqual([1, 2, 3, 4], _get_allowed_numbers(5, 2))
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], _get_allowed_numbers(11, 3))

    def test_get_start_index_of_group(self):
        self.assertEqual(1, _get_start_index_of_group(['x', 1, 2], 0))
        self.assertEqual(0, _get_start_index_of_group([1, 2, 'x'], 0))
        self.assertEqual(3, _get_start_index_of_group([1, 2, 'x', 3, 4, 'x'], 1))
        self.assertEqual(6, _get_start_index_of_group([1, 2, 'x', 3, 4, 'x', 5], 2))


    def test_set_cells1(self):
        board = deepcopy(board1)
        row = 3
        group_number = 0
        possible_values = [[8, 9], [8, 9]]
        board = _set_cell_horizontal(board, row, group_number, possible_values)
        expected = [
            ['x', 'x', 0, 0],
            ['x', 0, 0, 0],
            [0, 0, 0, 'x'],
            [[8, 9], [8, 9], 'x', 'x'],
        ]
        self.assertEqual(expected, board)

    def test_set_cells2(self):
        board = deepcopy(board1)
        row = 0
        group_number = 0
        possible_values = [2, 9]
        board = _set_cell_horizontal(board, row, group_number, possible_values)
        expected = [
            ['x', 'x', 2, 9],
            ['x', 0, 0, 0],
            [0, 0, 0, 'x'],
            [0, 0, 'x', 'x'],
        ]
        self.assertEqual(expected, board)
