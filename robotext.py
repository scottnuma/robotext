"""A small world explorer to teach python functions

Online version here: https://repl.it/BsmV
"""
#Background varaibles
WEST = 0
NORTH = 1
EAST = 2
SOUTH = 3

DIRECTION_STRINGS = ["WEST", "NORTH", "EAST", "SOUTH"]

LEFT = -1
RIGHT = 1



class World:
	"""A world of text to explore"""

	def __init__(self, width=10, height=10):
		self.__points = [["." for x in range(width)] for y in range(height)]
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

	def set_point(self, x, y, character):
		"""Set a point on the map of be a certain character"""
		assert len(character) == 1
		self.__points[y][x] = character

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
		return "Robot, x:%s, y:%s, inv:%s" % (self.__x, self.__y, self.__inventory)
	
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
			print "Invalid Movement"
		print self.__world

	def read(self):
		"""Inspect what the robot is currently standing above"""

		# Make sure that the robot has been placed in the world
		assert self.__world
		return self.__world.get_point(self.__x, self.__y)

	def grab(self):
		"""Adds the current object to inventory"""
		if self.__inventory:
			print "Inventory Full"
		else:
			self.__inventory = self.__world.take(self.__x, self.__y)

	def release(self):
		"""Puts object in the inventory on the ground"""
		if self.__inventory:
			if self.read() == '.':
				self.__world.leave(self.__inventory, self.__x, self.__y)
				self.__inventory = None
			else:
				print "Area blocked"
		else:
			print "Inventory empty"
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

if __name__ == "__main__" or __name__ == "__builtin__":
	a = World()
	a.set_point(3,3,'3')
	a.set_point(4,5,'2')
	a.set_point(6,1,'4')
	a.set_point(8,5,'5')

	#Create the hayward world
	b = World()
	b.set_point(3,8,'H')
	b.set_point(8,2,'A')
	b.set_point(7,8,'Y')
	b.set_point(1,3,'W')
	b.set_point(8,6,'A')
	b.set_point(3,2,'R')
	b.set_point(6,9,'A')
	b.set_point(3,5,'D')

	r = Robot()
	a.set_robot(r)