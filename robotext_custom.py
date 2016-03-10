"""This file allows you to create new functions for robotext without having
to worry about accidentaly changing the base code of robotext.

Note: I've changed how you can control the robot. Functions can now be
accessed with the "r." part of the function call.

For example: "r.move()" has become "move()"
r.move() and all the old function calls will still work for the sake of
backwards compatability, but using move() is simpler and corresponds with our
learning goals right now.
"""

from robotext import *

# What functions do I have access to?

# move()			moves the robot one step in the direction its facing
# get_x()			returns the current x coordinate
# get_y()			returns the current y coordinate
# turn_left()		the robot now faces left of the previous direction
# turn_right() 		the robot now faces right of the previous direction
# get_direction() 	returns the currently facing 
# grab()			grabs the character the robot is currently covering
# release()			if able to, robot places character in inventory on ground
# get_inventory()	returns the contents of the inventory (may be None)
# world_height()	returns the heigh of the world
# world_width()		returns the width of the world

#Here's an example of how to use the functions
def easy_move(distance):
	"""Attempts to move the robot a certain number of times"""
	count = 0
	while count < distance:
		move()
		count += 1

def turn_around():
	"""Turns the robot around in the opposite direction"""
	turn_right()
	turn_right()

def move_to(x,y):
	"""Moves to a specific location of the map"""
	"YOUR CODE HERE"

def find_character(character):
	"""Moves the robot to cover a certain character on the map"""
	"YOUR CODE HERE"