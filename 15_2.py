'''Exercise 15.2. Write a function named move_rectangle that takes a Rectangle and two numbers
named dx and dy . It should change the location of the rectangle by adding dx to the x coordinate of
corner and adding dy to the y coordinate of corner .'''


class Point(object):
	"""point"""
	

class Rectangle(object):
	"""Represents a rectangle.
	"""

box=Rectangle()

box.corner = Point()
box.corner.x = int(input())
box.corner.y = int(input())

def move_rectangle(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy
	print rect.corner.x,rect.corner.y



dx=int(input())
dy=int(input())

move_rectangle(box,dx,dy)
