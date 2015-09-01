from swampy.TurtleWorld import *
import math

def arc(turtle_obj, radius, angle):
	arc_length = 2*math.pi*radius*angle/360
	n = int(arc_length/3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n

	for i in range(n):
		fd(turtle_obj, step_length)
		lt(turtle_obj, step_angle)

def flower(turtle_obj, num_petals, radius, angle):
    for petal in range(num_petals):
        for i in range(2):
	        arc(turtle_obj, radius, angle)
	        lt(turtle_obj, 180-angle)
        lt(turtle_obj, 360.0/num_petals)

def move_without_writing(turtle_obj, length):
    pu(turtle_obj)
    fd(turtle_obj, 150)
    pd(turtle_obj)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

flower(bob, 7, 60.0, 60.0)

move_without_writing(bob, 100)
flower(bob, 10, 40.0, 80.0)

move_without_writing(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)

wait_for_user()