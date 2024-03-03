import unittest
from tkinter import Tk
from SquareMovementApp import SquareMovementApp

class TestSquareMovementApp(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = SquareMovementApp(self.root)

    def test_initial_score(self):
        self.assertEqual(self.app.score, 0)

    def test_move_left(self):
        initial_coords = self.app.canvas.coords(self.app.square)
        self.app.move_left(None)
        new_coords = self.app.canvas.coords(self.app.square)
        self.assertTrue(new_coords[0] < initial_coords[0])

    def test_move_right(self):
        initial_coords = self.app.canvas.coords(self.app.square)
        self.app.move_right(None)
        new_coords = self.app.canvas.coords(self.app.square)
        self.assertTrue(new_coords[0] > initial_coords[0])

    def test_jump(self):
        initial_coords = self.app.canvas.coords(self.app.square)
        self.app.jump(None)
        new_coords = self.app.canvas.coords(self.app.square)
        self.assertTrue(new_coords[1] < initial_coords[1])

    def test_collision_obstacle(self):
        self.app.canvas.coords(self.app.square, 300, 220, 300 + self.app.square_size, 220 + self.app.square_size)
        self.assertTrue(self.app.check_collision_obstacle())

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
