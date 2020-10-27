from typing import Tuple
from uuid import uuid4

positionType = Tuple[int, int, str]
positionTypeResponse = Tuple[Tuple[int, int], str]

DIRECTIONS = ("NORTH", "EAST", "SOUTH", "WEST")


def rbrain(instruction, x, y, direction):
    logic = {
        "NORTH": (0, 1),
        "EAST": (1, 0),
        "SOUTH": (0, -1),
        "WEST": (-1, 0),
    }
    return x + logic[direction][0], y + logic[direction][1], direction


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
        x, y, direction = position

        if direction not in DIRECTIONS:
            raise ValueError(
                f"Invalid direction, direction should be one of {DIRECTIONS}"
            )

        self.name = name if name else uuid4().hex[:10]
        self.x, self.y, self.direction = x, y, direction

    @property
    def position(self) -> positionTypeResponse:
        """Return current rover position.

        Tuple (x, y), direction"""
        return (self.x, self.y), self.direction

    def send_command(self, command: str) -> positionTypeResponse:
        """
        Send a command to the rover.

        Return rover's position.
        """
        for instruction in command:
            self.x, self.y, _ = rbrain(instruction, self.x, self.y, self.direction)
        return self.position
