from typing import Any
import unittest

class BowlingGame(object):
    def __init__(self) -> None:
        self.score = 0
        self.throws = []
        

    def throw(self, pins):
        self.throws.append(pins)
    
    def calculate_score(self):
        ball = 0
        for frames in range(10):
            self.score += self.throws[ball] + self.throws[ball + 1]
            ball += 2

class BowlingGameTest(unittest.TestCase):
    def test_all_gutters(self):
        game = BowlingGame()
        for _ in range(20):
            game.throw(0)
        
        game.calculate_score()
        
        self.assertEqual(game.score, 0)

    def test_all_ones(self):
        game = BowlingGame()
        for _ in range(20):
            game.throw(1)

        game.calculate_score()
        self.assertEqual(game.score, 20)

    def test_for_spare(self):
        game = BowlingGame()
        game.throw(4)
        game.throw(6)
        game.throw(7)
        game.throw(0)
        for _ in range(16):
            game.throw(0)

        self.assertEqual(game.score, 24)

if __name__ == '__main__':
    unittest.main()