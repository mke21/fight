from typing import Protocol
from pygame.surface import SurfaceType

class GameProtocol(Protocol):

    screen: SurfaceType

    def run(self):
        ...
