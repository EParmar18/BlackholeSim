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
        self.c = c
        self.rs = (2 * g * self.mass) / (c * c)
        print(self.rs)

    # Force of grav  = (G * M1 * M2) / r * 2
    # Method to mimic newtonian gravity
    def pull(self, p):
        force = self.pos - p.pos
        r = magnitude(force.x, force.y)
        fg = self.g * self.mass / (r * r)
        force.magnitude = fg
        p.vel = p.vel + force
        p.vel.magnitude = self.c

        if r <= self.rs:
            p.stop()

    def show(self):
        ellipse_mode(mode = 'RADIUS')
        fill(50)
        no_stroke()
        circle((self.pos), self.rs)

        no_fill()
        stroke(100)
        stroke_weight(6)
        circle(self.x, self.y, self.rs * 3 + 2)

        stroke(255, 150, 0)
        stroke_weight(3)
        circle(self.x, self.y, self.rs * 1.5 + 1)

