import unittest
from score import Score

class TestHand(unittest.TestCase):
    def test_get_score(self):
        testcase_hand = [0, 1, 33554432, 33611776, 16834560, 73728, 10240]
        expected_score = [0, -10, 11, -30, 19, 19, 8]
        computed_score = [Score(hand).get_score() for hand in testcase_hand]

        for case in zip(computed_score, expected_score):
            self.assertEqual(case[0], case[1])

if __name__ == "__main__":
    unittest.main()
