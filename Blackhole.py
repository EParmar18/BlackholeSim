from p5 import *
import numpy
import math
class Blackhole:
    def __init__(self,x,y,m,g,c):
        self.x = x
        self.y = y
        self.pos = Vector(x,y)
        self.mass = m
        self.g = g
        self.rs = (2 * g * self.mass) / (c * c)
        print(self.rs)

    # Force of grav  = (G * M1 * M2) / r * 2
    # Problem here is that photons have 0 mass, so 
    def pull(self, p):
        force = self.pos - p.pos
        r = magnitude(force.x, force.y)
        fg = self.g * self.mass / (r * r)
        force.magnitude = fg
        p.vel = p.vel + force

    def show(self):
        fill(50)
        no_stroke()
        circle((self.pos), self.rs)

        no_fill()
        stroke(100)
        stroke_weight(10)
        circle(self.x, self.y, self.rs * 3 + 2)

        stroke(255, 150, 0)
        stroke_weight(4)
        circle(self.x, self.y, self.rs * 1.5 + 1)

