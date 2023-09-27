"""
The main entry point for the application.
"""
from .game import init_game, quit_game
import argparse


def main():
    parser = argparse.ArgumentParser(description="Fight game")
    parser.add_argument("-r", "--resolution", nargs=2, type=int, help="Resolution of the game",
                        metavar=("WIDTH", "HEIGHT"), default=None)
    args = parser.parse_args()
    game = init_game(args.resolution)
    game.run()
    quit_game()


if __name__ == "__main__":
    main()
