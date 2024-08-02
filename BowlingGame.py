from typing import Any
import unittest

class BowlingGame(object):
    def __init__(self) -> None:
        self.score = 0
        

    def throw(self, pins):
        self.score += pins

class BowlingGameTest(unittest.TestCase):
    def test_all_gutters(self):
        game = BowlingGame()
        for _ in range(20):
            game.throw(0)
        
        self.assertEqual(game.score, 0)

    def test_all_ones(self):
        game = BowlingGame()
        for _ in range(20):
            game.throw(1)
        
        self.assertEqual(game.score, 20)

if __name__ == '__main__':
    unittest.main()