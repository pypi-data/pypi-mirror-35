import unittest
from ybc_player import *


class MyTestCase(unittest.TestCase):
    def test_play(self):
        play('test.wav')


if __name__ == '__main__':
    unittest.main()