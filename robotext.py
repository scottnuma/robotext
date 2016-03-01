#Background varaibles
WEST = 0
NORTH = 1
EAST = 2
SOUTH = 3

DIRECTION_STRINGS = ["WEST", "NORTH", "EAST", "SOUTH"]

LEFT = -1
RIGHT = 1

class World:
	def __init__(self, width=5, height=5):
		self.__points = [["." for x in range(width)] for y in range(height)]
		self.__points[height//2][width//2] = '@'
		self.__width = width
		self.__height = height
		self.__robot = None 

	def __repr__(self):
		return "World, width:%s, height:%s" % (self.__width, self.__height)

	def __str__(self):
		"""Returns a string map representation of itself"""
		result = ""
		for y in reversed(range(self.__height)):
			for x in range(self.__width):
				if self.__robot:
					if x == self.__robot.get_x() and y == self.__robot.get_y():
						result += str(self.__robot)
					else:
						result += self.__points[y][x]
				else:
					result += self.__points[y][x]
			if y != 0:
				result += "\n"
		return result

	def take(self, x,y):
		"""Takes thing at location and replaces with '.'"""
		temp = self.__points[y][x]
		self.__points[y][x] = "."
		return temp

	def leave(self, thing, x, y):
		"""Leaves thing at location"""
		self.__points[y][x] = thing

	def set_robot(self, robot):
		"""Add a robot into the world to be displayed"""
		self.__robot = robot
		self.__robot.add_world(self)

	def get_height(self):
		return self.__height

	def get_width(self):
		return self.__width

	def get_point(self, x, y):
		return self.__points[y][x]

class Robot:
	def __init__(self, x = 0, y = 0):
		"""Creates a robot at (x,y) or (0,0) by default"""
		self.__x, self.__y = x, y
		self.__direction = NORTH
		self.__world = None
		self.__verbose = True
		self.__inventory = None
	def __repr__(self):
		return "Robot, x:%s, y:%s" % (self.__x, self.__y)
	
	def __str__(self):
		"""Defines the symbol that robot will be displayed as"""
		return "$"
	
	def turn_left(self):
		self.__direction = (self.__direction + LEFT) % 4
	
	def turn_right(self):
		self.__direction = (self.__direction + RIGHT) % 4

	def toggle_verbose(self):
		self.__verbose = not self.verbose
	
	def move(self):
		"""Moves the robot one space in the direction it's facing"""

		# Make sure that robot has been placed in the world
		assert self.__world

		if self.__direction == NORTH and self.__y + 1 < self.__world.get_height():
			self.__y += 1
		elif self.__direction == EAST and self.__x + 1 < self.__world.get_width():
			self.__x += 1
		elif self.__direction == SOUTH and self.__y - 1 > 0:
			self.__y -= 1
		elif self.__direction == WEST and self.__x - 1 > 0:
			self.__x -= 1
		else:
			print("Invalid Movement")
		print(self.__world)

	def read(self):
		"""Inspect what the robot is currently standing above"""

		# Make sure that the robot has been placed in the world
		assert self.__world
		return self.__world.get_point(self.__x, self.__y)

	def grab(self):
		"""Adds the current object to inventory"""
		if self.__inventory:
			print("Inventory Full")
		else:
			self.__inventory = self.__world.take(self.__x, self.__y)

	def release(self):
		"""Puts object in the inventory on the ground"""
		if self.__inventory:
			self.__world.leave(self.__inventory, self.__x, self.__y)
			self.__inventory = None
		else:
			print("Inventory empty")
	def get_inventory(self):
		return self.__inventory

	def add_world(self, world):
		"""Add the robot to a world"""
		self.__world = world

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_direction(self):
		return DIRECTION_STRINGS[self.__direction]

if __name__ == "__main__":
	a = World()
	r = Robot()
	a.set_robot(r)