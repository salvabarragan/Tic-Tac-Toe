import unittest
from src.logic import Match

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.match = Match()

    def test_initial_board(self):
        self.assertEqual(self.match.moves, [" "] * 9)

    def test_player_x_move(self):
        result = self.match.player_x(1)
        self.assertTrue(result)
        self.assertEqual(self.match.moves[0], "X")

    def test_invalid_move(self):
        self.match.player_x(1)
        result = self.match.player_x(1)
        self.assertFalse(result)
        
    def test_check_result_1(self):
        self.match.moves = ["X", "X", "X",
                            "O", "O", " ",
                            " ", " ", " "]
        self.assertTrue(self.match.check_result("X"))
        
    def test_check_result_2(self):
        self.match.moves = ["X", "X", "",
                            "O", "O", "O",
                            "X", " ", " "]
        self.assertTrue(self.match.check_result("O"))

    def test_check_result_3(self):
        self.match.moves = [" ", " ", " ",
                            "O", "O", " ",
                            "X", "X", "X"]
        self.assertTrue(self.match.check_result("X"))
    def test_check_result_4(self):
        self.match.moves = ["O", " ", " ",
                            "O", "X", "X",
                            "O", " ", " "]
        self.assertTrue(self.match.check_result("O"))
        
    def test_check_result_5(self):
        self.match.moves = [" ", "X", " ",
                            "O", "X", "O",
                            " ", "X", " "]
        self.assertTrue(self.match.check_result("X"))
        
    def test_check_result_6(self):
        self.match.moves = ["X", "X", "O",
                            " ", " ", "O",
                            " ", " ", "O"]
        self.assertTrue(self.match.check_result("O"))
        
    def test_check_result_7(self):
        self.match.moves = ["X", " ", " ",
                            "O", "X", "O",
                            " ", " ", "X"]
        self.assertTrue(self.match.check_result("X"))
        
    def test_check_result_8(self):
        self.match.moves = ["X", "X", "O",
                            " ", "O", " ",
                            "O", " ", " "]
        self.assertTrue(self.match.check_result("O"))
        
    def test_check_reslut_draw(self):
        self.match.moves = ["X", "X", "O",
                            "O", "O", "X",
                            "X", "O", "X"]
        self.assertEqual(self.match.check_result("X"), 2)
        # "2" means "Draw", but it is shown in game.py
       

if __name__ == '__main__':
    unittest.main()

