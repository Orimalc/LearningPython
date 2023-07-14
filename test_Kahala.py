from unittest import TestCase

import numpy as np
import Kahala

class TestGame(TestCase):

    def test_fillingUpByTravelingP1(self):
        game1 = Kahala.Game()
        game1.set_board(np.asarray([[1, 2, 3, 4, 4, 5], [0, 0, 0, 0, 0, 0]]))
        game1.play(6)
        self.assertEqual([[2, 3, 4, 5, 5, 0], [0, 0, 0, 0, 0, 0]], game1.board.tolist())

    def test_toEnemyRowP1(self):
        game1 = Kahala.Game()
        game1.set_board(np.asarray([[4, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
        game1.play(1)
        self.assertEqual([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0]], game1.board.tolist())

    def test_backToOwnBoardP1(self):
        game1 = Kahala.Game()
        game1.board = np.asarray([[8,0,0,0,0,0],[0,0,0,0,0,0]])
        game1.play(1)
        self.assertEqual([[0,0,0,0,0,1],[1,1,1,1,1,1]], game1.board.tolist())
        game2 = Kahala.Game()
        game2.board=np.asarray([[0,0,0,0,0,13],[0,0,0,0,0,0]])
        game2.play(6)
        self.assertEqual([[1,1,1,1,1,1],[1,1,1,1,1,1]], game2.board.tolist())
        game3 = Kahala.Game()
        game3.board=np.asarray([[0,0,0,0,14,0],[0,0,0,0,0,0]])
        game3.play(5)
        self.assertEqual([[1,1,1,2,1,1],[1,1,1,1,1,1]], game3.board.tolist())

    def test_stealingP1(self):
        game1 = Kahala.Game()
        game1.board = np.asarray([1, 1, 1, 1, 0, 1, 0, 1, 8, 1, 1, 1, 1, 0])
        game1.play(3)
        self.assertEqual([1, 1, 1, 0, 0, 1, 8, 1, 0, 1, 1, 1, 1, 0], game1.board.tolist())

    def test_fillingUpByTravelingP2(self):
        game1 = Kahala.Game()
        game1.board=np.asarray([[0, 1, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0]])
        game1.play(2)
        game1.play(6)
        self.assertEqual([[1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1]], game1.board.tolist())

    def test_toEnemyRowP2(self):
        game1 = Kahala.Game()
        game1.board=np.asarray([[0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 3]])
        game1.play(4)
        game1.play(1)
        self.assertEqual([[1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0]], game1.board.tolist())

    def test_backToOwnBoardP2(self):
        game1 = Kahala.Game()
        game1.board=np.asarray([[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 8]])
        game1.play(3)
        game1.play(1)
        self.assertEqual([[1, 2, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0]], game1.board.tolist())
        game2 = Kahala.Game()
        game2.board=np.asarray([[0, 0, 1, 0, 0, 0], [13, 0, 0, 0, 0, 0]])
        game2.play(3)
        game2.play(6)
        self.assertEqual([[1, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]], game2.board.tolist())
        game3 = Kahala.Game()
        game3.board=np.asarray([[0, 0, 1, 0, 0, 0], [0, 14, 0, 0, 0, 0]])
        game3.play(3)
        game3.play(5)
        self.assertEqual([[1, 2, 1, 1, 1, 1], [1, 1, 2, 1, 1, 1]], game3.board.tolist())

