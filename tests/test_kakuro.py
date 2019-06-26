from unittest import TestCase

from kakuro.kakuro import solve, is_solved, _get_cell_groups, _get_possible_values_for_cells, _get_allowed_numbers


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
        self.assertEqual([[8, 9], [8, 9]], _get_possible_values_for_cells([0, 0], 17))

    def test_get_allowed_numbers(self):
        self.assertEqual([8, 9], _get_allowed_numbers(17, 2))
