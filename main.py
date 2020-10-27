from typing import Tuple
from uuid import uuid4

positionType = Tuple[int, int, str]
positionTypeResponse = Tuple[Tuple[int, int], str]

DIRECTIONS = ("NORTH", "EAST", "SOUTH", "WEST")


def rbrain(command: str, x: int, y: int, direction: str) -> Tuple[int, int, str]:
    logic = {
        "F": {
            "NORTH": (0, 1),
            "EAST": (1, 0),
            "SOUTH": (0, -1),
            "WEST": (-1, 0),
        }
    }

    # the command we receive must be a subset
    # of the instructions implemented inside logic
    if (set(command) <= logic.keys()) is False:
        raise ValueError("Instruction error: `{command}` not valid")

    for instruction in command:
        execution_plan = logic[instruction]
        x += execution_plan[direction][0]
        y += execution_plan[direction][1]

    return x, y, direction


class Rover:
    """A rover power by AI and solar cells.

    But needs to be initialized, it takes a name
    and a position.

    You can initialite with a name (optional) and a position.

    A position is a tuple made with 3 elements, (x, y, direction):
    x, y: position on the map
    direction: one of the cardinal directions: NORTH, EAST, SOUTH, and WEST.

    """

    def __init__(self, position: positionType, name: str = None) -> None:
        x, y, direction = position

        if direction not in DIRECTIONS:
            raise ValueError(
                f"Invalid direction, direction should be one of {DIRECTIONS}"
            )

        self.name = name if name else uuid4().hex[:10]
        self.x, self.y, self.direction = x, y, direction

        # each rover has a brain
        # with some built-in logic to move around
        self.brain = rbrain

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
        self.x, self.y, _ = self.brain(command, self.x, self.y, self.direction)
        return self.position
