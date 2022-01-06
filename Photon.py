from p5 import *

class Photon:

    def __init__(self,x,y,c,dt):
        self.pos = Vector(x,y)
        self.x = x
        self.y = y
        self.c = c
        self.dt = dt
        self.vel = Vector(-c, 0)

    def update(self):
        deltaV = self.vel.copy()
        deltaV = deltaV * self.dt
        self.pos = self.pos + deltaV

    def show(self):
        stroke(255,0,0)
        point(self.pos.x, self.pos.y)
