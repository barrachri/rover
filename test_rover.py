from main import Rover, DIRECTIONS
import pytest


@pytest.mark.parametrize("direction", [*DIRECTIONS])
def test_rover_initialization(direction):
	name = "Teslover"
	x, y = 0, 1
	rover = Rover(position=(x,y,direction), name=name)
	assert rover.name == name
	assert rover.x == x
	assert rover.y == y
	assert rover.direction == direction

def test_rover_initialization_no_name():
	x, y, direction = 0, 1, "WEST"
	rover = Rover(position=(x,y,direction))
	assert rover.name


def test_rover_initialization_raise_error_invalid_direction():
	x, y, direction = 0, 1, "W"
	with pytest.raises(ValueError) as err:
		Rover(position=(x,y,direction))

	assert "Invalid direction" in str(err.value)
