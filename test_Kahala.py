from unittest import TestCase

import numpy as np
import Kahala

class TestGame(TestCase):
    def test_play(self):
        game1 = Kahala.Game()
        game1.set_board(np.asarray([[8,0,0,0,0,0],[0,0,0,0,0,0]]))
        game1.play(1)
        self.assertEqual(np.asarray(game1.board).tolist(), [[0,0,0,0,0,1],[1,1,1,1,1,1]])

