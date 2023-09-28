from multiprocessing import Process
from .game import init_game, quit_game


def run_multi(res):
    game = init_game(res)
    game.run()
    quit_game()


def run_games(res):
    process1 = Process(target=run_multi, args=(res,))
    process2 = Process(target=run_multi, args=(res,))
    for p in [process1, process2]:
        p.start()

    for p in [process1, process2]:
        p.join()

    quit_game()
