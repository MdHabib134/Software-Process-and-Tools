import unittest
from Assignment import Assignment


class MyTestCase(unittest.TestCase):
    assignment = Assignment()

    def test_rock_paper_scissor_equal(self):

        self.assertEqual('Draw', self.assignment.play_game('rock', 'rock'))


        self.assertEqual('Draw', self.assignment.play_game('rock', 'rock'))
        self.assertEqual('Draw', self.assignment.play_game('paper', 'paper'))
        self.assertEqual('Draw', self.assignment.play_game('scissor', 'scissor'))

        self.assertEqual('You win', self.assignment.play_game('rock', 'scissor'))
        self.assertEqual('You win', self.assignment.play_game('paper', 'rock'))
        self.assertEqual('You win', self.assignment.play_game('scissor', 'paper'))

        self.assertEqual('Computer win', self.assignment.play_game('scissor', 'rock'))
        self.assertEqual('Computer win', self.assignment.play_game('rock', 'paper'))
        self.assertEqual('Computer win', self.assignment.play_game('paper', 'scissor'))

    def test_rock_paper_scissor_not_equal(self):
        self.assertNotEqual('You win', self.assignment.play_game('rock', 'rock'))
        self.assertNotEqual('You win', self.assignment.play_game('paper', 'paper'))
        self.assertNotEqual('You win', self.assignment.play_game('scissor', 'scissor'))
        self.assertNotEqual('Computer win', self.assignment.play_game('rock', 'rock'))
        self.assertNotEqual('Computer win', self.assignment.play_game('paper', 'paper'))
        self.assertNotEqual('Computer win', self.assignment.play_game('scissor', 'scissor'))

        self.assertNotEqual('Computer win', self.assignment.play_game('rock', 'scissor'))
        self.assertNotEqual('Computer win', self.assignment.play_game('paper', 'rock'))
        self.assertNotEqual('Computer win', self.assignment.play_game('scissor', 'paper'))
        self.assertNotEqual('Draw', self.assignment.play_game('rock', 'scissor'))
        self.assertNotEqual('Draw', self.assignment.play_game('paper', 'rock'))
        self.assertNotEqual('Draw', self.assignment.play_game('scissor', 'paper'))

        self.assertNotEqual('You win', self.assignment.play_game('scissor', 'rock'))
        self.assertNotEqual('You win', self.assignment.play_game('rock', 'paper'))
        self.assertNotEqual('You win', self.assignment.play_game('paper', 'scissor'))
        self.assertNotEqual('Draw', self.assignment.play_game('scissor', 'rock'))
        self.assertNotEqual('Draw', self.assignment.play_game('rock', 'paper'))
        self.assertNotEqual('Draw', self.assignment.play_game('paper', 'scissor'))


if __name__ == '__main__':
    unittest.main()
