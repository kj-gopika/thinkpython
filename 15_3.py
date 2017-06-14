'''Exercise 15.3. Write a version of move_rectangle that creates and returns a new Rectangle
instead of modifying the old one.'''


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
