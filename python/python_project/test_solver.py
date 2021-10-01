#!/usr/bin/env python3

import unittest
import random

from grid import SudokuGrid
from solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self._grid = SudokuGrid("349287501000000700000509002" \
                + "200095007001000400800720005"
                + "100402000008000000000000376")
        self._solver = SudokuSolver(self._grid)

    def test_00_is_valid(self):
        self.assertTrue(self._solver.is_valid())

    def test_01_is_solved(self):
        self.assertFalse(self._solver.is_solved())

    def test_02_solve_step(self):
        self._solver.solve_step()
        self.assertEqual(list(self._grid.get_row(0))[7], 6)
        self.assertEqual(list(self._grid.get_row(2))[6], 8)
        self.assertEqual(list(self._grid.get_row(6))[6:], [9, 5, 8])
        self.assertEqual(list(self._grid.get_row(7))[8], 4)

    def test_03_solve(self):
        sol = self._solver.solve()
        for i, row in enumerate(([3, 4, 9, 2, 8, 7, 5, 6, 1],
                [5, 8, 2, 6, 4, 1, 7, 9, 3],
                [6, 1, 7, 5, 3, 9, 8, 4, 2],
                [2, 3, 4, 1, 9, 5, 6, 8, 7],
                [7, 5, 1, 8, 6, 3, 4, 2, 9],
                [8, 9, 6, 7, 2, 4, 1, 3, 5],
                [1, 6, 3, 4, 7, 2, 9, 5, 8],
                [9, 7, 8, 3, 5, 6, 2, 1, 4])):
            self.assertEqual(list(sol.get_row(i)), row)


if __name__ == "__main__":
    unittest.main()
