#!/usr/bin/env python3

import unittest
import unittest.mock
import random
import os.path

from grid import SudokuGrid


class TestSudokuGrid(unittest.TestCase):
    def setUp(self):
        self._grid = SudokuGrid("349000000000000700000509002" \
                + "200095007001000400800720005" \
                + "100402000008000000000000376")

    def test_00_init(self):
        with self.assertRaises(ValueError): # char
            grid = SudokuGrid("123456xyz" * 9)
        with self.assertRaises(ValueError): # hex values
            grid = SudokuGrid("123456abc" * 9)
        with self.assertRaises(ValueError): # too short
            grid = SudokuGrid("123456")
        with self.assertRaises(ValueError): # too long
            grid = SudokuGrid("12345678" * 11)

    def test_01_from_file(self):
        grid = SudokuGrid.from_file(os.path.join(os.path.dirname(__file__), "..", "sudoku_db.txt"),
                random.randint(1, 244)) # File not found if instructions not followed while setting up the ws

    def test_02_from_stdin(self):
        with unittest.mock.patch('builtins.input', return_value="123456789" * 9):
            grid = SudokuGrid.from_stdin()

    def test_03_str(self):
        expected_str = ("349000000", "000000700", "000509002",
                "200095007", "001000400", "800720005",
                "100402000", "008000000", "000000376")
        grid_str = str(self._grid).splitlines()
        for grid_line, expected_line in zip(expected_str, grid_str):
            self.assertRegex(grid_line, ".*".join(expected_line.replace("0", "[0 ]")))

    def test_04_get_row(self):
        self.assertEqual(list(self._grid.get_row(1)),
                [0, 0, 0, 0, 0, 0, 7, 0, 0])
        self.assertEqual(list(self._grid.get_row(4)),
                [0, 0, 1, 0, 0, 0, 4, 0, 0])

    def test_05_get_col(self):
        self.assertEqual(list(self._grid.get_col(4)),
                [0, 0, 0, 9, 0, 2, 0, 0, 0])
        self.assertEqual(list(self._grid.get_col(5)),
                [0, 0, 9, 5, 0, 0, 2, 0, 0])

    def test_06_get_region(self):
        self.assertEqual(list(self._grid.get_region(0, 0)),
                [3, 4, 9, 0, 0, 0, 0, 0, 0])
        self.assertEqual(list(self._grid.get_region(2, 1)),
                [4, 0, 2, 0, 0, 0, 0, 0, 0])

    def test_07_empty_pos(self):
        self.assertEqual(set(self._grid.get_empty_position()),
                {(7, 3), (4, 7), (1, 3), (4, 8), (5, 6), (6, 6), (8, 0), (7, 7), (0, 7), (2, 1), (6, 2),
                    (3, 7), (0, 3), (5, 1), (8, 5), (4, 0), (1, 2), (6, 7), (3, 3), (5, 5), (8, 1), (7, 6),
                    (4, 4), (1, 5), (3, 6), (2, 2), (0, 4), (4, 1), (1, 1), (6, 4), (3, 2), (2, 6), (8, 2),
                    (7, 1), (4, 5), (1, 4), (7, 5), (0, 5), (1, 0), (0, 8), (2, 7), (7, 8), (8, 3), (7, 0),
                    (6, 8), (6, 1), (3, 1), (5, 7), (7, 4), (0, 6), (1, 8), (2, 0), (4, 3), (1, 7), (5, 2),
                    (2, 4), (8, 4)})

    def test_08_write(self):
        for _ in range(4):
            i, j = random.choice(list(self._grid.get_empty_position()))
            val = random.randint(1, 9)
            self._grid.write(i, j, val)
            self.assertEqual(list(self._grid.get_row(i))[j], val)

    def test_09_copy(self):
        grid = self._grid.copy()
        for i in range(9):
            self.assertEqual(list(grid.get_row(i)), list(self._grid.get_row(i)))
        i, j = random.choice(list(self._grid.get_empty_position()))
        val = random.randint(1, 9)
        grid.write(i, j, val)
        self.assertEqual(list(self._grid.get_row(i))[j], 0)


if __name__ == "__main__":
    unittest.main()
