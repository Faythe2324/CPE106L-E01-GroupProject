import unittest
import os
import oxo_logic
import oxo_data


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        """Create a new game before each test"""
        self.game = oxo_logic.Game()
        self.game.newGame()

    def test_new_game_starts_empty(self):
        """New game should create a board with 9 empty cells"""
        self.assertEqual(self.game.board, [" "] * 9)

    def test_user_move_valid(self):
        """User should be able to place 'X' in an empty cell"""
        self.game.userMove(0)
        self.assertEqual(self.game.board[0], "X")

    def test_user_move_invalid(self):
        """Placing in an occupied cell should raise ValueError"""
        self.game.userMove(0)
        with self.assertRaises(ValueError):
            self.game.userMove(0)

    def test_computer_move_places_O(self):
        """Computer should place 'O' in an empty cell"""
        result = self.game.computerMove()
        self.assertIn("O", self.game.board)
        self.assertIn(result, ["", "O", "D"])  # result can be win, draw, or continue

    def test_winning_move(self):
        """Game should detect a winning condition"""
        # Make X win in the first row
        self.game.board = ["X", "X", "X",
                           " ", " ", " ",
                           " ", " ", " "]
        self.assertTrue(self.game._isWinningMove())

    def test_draw_condition(self):
        """Game should return 'D' when board is full and no winner"""
        self.game.board = ["X", "O", "X",
                           "X", "O", "O",
                           "O", "X", "X"]
        result = self.game.computerMove()
        self.assertEqual(result, "D")

    def test_save_and_restore_game(self):
        """Game should save and restore correctly"""
        test_board = ["X", "O", "X",
                      " ", "O", " ",
                      "X", " ", " "]
        self.game.board = test_board
        self.game.saveGame()

        restored = self.game.restoreGame()
        self.assertEqual(restored, test_board)


if __name__ == "__main__":
    unittest.main()