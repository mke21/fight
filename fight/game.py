"""
The main game class making
"""
from dataclasses import dataclass, field
import pygame as pg
from pygame.surface import SurfaceType
from .settings import RES, FPS, CAPTION

BACKGROUND = pg.image.load('assets/Night-level.png')
pg.display.set_caption(CAPTION)


@dataclass
class Game:
    screen: SurfaceType
    clock: pg.time.Clock
    _keep_running: bool = field(init=False, default=True)

    def quit(self) -> None:
        """Quit the game"""
        self._keep_running = False

    def _check_running(self) -> None:
        """Check if the game is running"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def _update(self) -> None:
        """Update in the loop"""
        self._check_running()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{CAPTION} FPS:{self.clock.get_fps() :.1f}')

    def run(self) -> None:
        while self._keep_running:
            self._update()
            pg.display.update()


def init_game(res: tuple[int, int] | None = None) -> Game:
    pg.init()
    screen = pg.display.set_mode(res or RES)  # if res not set, use RES
    screen.blit(BACKGROUND, (0, 0))
    clock = pg.time.Clock()
    return Game(screen=screen, clock=clock)


def quit_game() -> None:
    pg.quit()


if __name__ == '__main__':
    game = init_game()
    game.run()
    pg.quit()
