class Point():
	""" 2d point """
	
	


def dist(p1,p2):
	xd=p1.x-p2.x
	yd=p1.y-p2.y
	print xd,yd

p1=Point()
p2=Point()

print "Enter the x,y values for p1"
p1.x=int(input())
p1.y=int(input())

print "Enter the x,y values for p2"
p2.x=int(input())
p2.y=int(input())

dist(p1,p2)

