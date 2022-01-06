from numpy import histogram
from p5 import *

class Photon:

    def __init__(self,x,y,c,dt):
        self.pos = Vector(x,y)
        self.x = x
        self.y = y
        self.c = c
        self.dt = dt
        self.vel = Vector(-c, 0)
        self.history = []

    def update(self):
        self.history.append(self.pos.copy())
        deltaV = self.vel.copy()
        deltaV = deltaV * self.dt
        self.pos = self.pos + deltaV

        if len(self.history) > 100:
            self.history.pop(0)

    def show(self):
        stroke(255,0,0)
        stroke_weight(4)
        point(self.pos.x, self.pos.y)

        stroke(0)
        stroke_weight(1)
        no_fill()
        begin_shape()

        for h in self.history:
            vertex(h.x, h.y)

        end_shape()

