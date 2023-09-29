"""
Voorbeeld van multi processing run
"""
from fight.multitest import run_games


if __name__ == "__main__":
    res = (200, 100)
    run_games(res)