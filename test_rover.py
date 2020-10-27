from main import Rover

def test_rover_initialization():
	name = "Teslover"
	x, y, direction = 0, 1, "W"
	rover = Rover(position=(x,y,direction), name=name)
	assert rover.name == name
	assert rover.x == x
	assert rover.y == y
	assert rover.direction == direction

def test_rover_initialization_no_name():
	x, y, direction = 0, 1, "W"
	rover = Rover(position=(x,y,direction))
	assert rover.name
