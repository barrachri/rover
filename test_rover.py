from main import Rover, DIRECTIONS
import pytest


@pytest.mark.parametrize("direction", [*DIRECTIONS])
def test_rover_initialization(direction):
    name = "Teslover"
    x, y = 0, 1
    rover = Rover(position=(x, y, direction), name=name)
    assert rover.name == name
    assert rover.x == x
    assert rover.y == y
    assert rover.direction == direction


def test_rover_initialization_no_name():
    x, y, direction = 0, 1, "WEST"
    rover = Rover(position=(x, y, direction))
    assert rover.name


def test_rover_initialization_raise_error_invalid_direction():
    x, y, direction = 0, 1, "W"
    with pytest.raises(ValueError) as err:
        Rover(position=(x, y, direction))
    assert "Invalid direction" in str(err.value)


def test_rover_return_position():
    x, y, direction = 0, 1, "WEST"
    rover = Rover(position=(x, y, direction))
    assert rover.position == ((x, y), direction)


@pytest.mark.parametrize("command, new_position", [("FFF", (7, 2)), ("F", (5, 2))])
def test_rover_send_command(command, new_position):
    x, y, direction = 4, 2, "EAST"
    rover = Rover(position=(x, y, direction))
    resp = rover.send_command(command)
    assert resp == (new_position, "EAST")


@pytest.mark.parametrize(
    "command, last_position",
    (["FFZ", ((6, 2), "EAST")], ["ZZF", ((4, 2), "EAST")], ["TFT", ((4, 2), "EAST")]),
)
def test_rover_invalid_command(command, last_position):
    x, y, direction = 4, 2, "EAST"
    rover = Rover(position=(x, y, direction))
    with pytest.raises(ValueError):
        rover.send_command(command)
    assert rover.position == last_position
