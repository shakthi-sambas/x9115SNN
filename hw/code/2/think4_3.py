
import math

from swampy.TurtleWorld import *
    
def polygon(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        triangle(t, r, angle/2)
        lt(t, angle)
    pu(t)
    fd(t, 120)
    pd(t)

def triangle(turtle_obj, radius, angle):
    base_angle = radius * math.sin(angle * math.pi / 180)

    lt(turtle_obj, angle)
    fd(turtle_obj, radius)
    rt(turtle_obj, 90+angle)
    fd(turtle_obj, 2*base_angle)
    rt(turtle_obj, 90+angle)
    fd(turtle_obj, radius)
    rt(turtle_obj, 180-angle)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1

size = 50
polygon(bob, 5, size)
polygon(bob, 6, size)
polygon(bob, 7, size)
polygon(bob, 8, size)
die(bob)

wait_for_user()
