import unittest
from .game import init_game, quit_game

# please make a test for the game.py and main.py
# you can use the test_run.py as a template


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = init_game()
        # run game and then send a pygame.QUIT event
        self.game.run()
        quit_game()

    def test_init_game(self):
        self.assertEqual(self.game.screen.get_width(), 1920)
        self.assertEqual(self.game.screen.get_height(), 1080)
        self.assertEqual(self.game.clock.get_fps(), 30)

    def test_quit_game(self):
        self.assertEqual(self.game.keep_running, False)

    def test_run(self):
        self.assertEqual(self.game.keep_running, False)

    def tearDown(self):
        self.game = None


if __name__ == '__main__':
    unittest.main()
