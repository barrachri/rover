from typing import Tuple
from uuid import uuid4

positionType = Tuple[int, int, str]


class Rover:
    """A rover power by AI and solar cells.

    But needs to be initialized, it takes a name
    and a position.

    You can initialite with a name (optional) and a position.

    A position is a tuple made with 3 elements, (x, y, direction):
    x, y: position on the map
    direction: one of the cardinal directions: N, E, S, and W.

    """

    def __init__(self, position: positionType, name: str = None) -> None:
        self.name = name if name else uuid4().hex[:10]
        self.x, self.y, self.direction = position
