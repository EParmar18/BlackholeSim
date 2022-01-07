from p5 import *
from Blackhole import Blackhole
from Photon import Photon
import numpy
import math
# Schwarzschild Radius Constants 
# Using M87 Blackhole Mass which is 2.6 Billion * Sun

light_speed = 30
gravity = 2
mass = 6000
s_radius = (2 * gravity * mass) / (light_speed ** 2)
delta_time = 0.1
height = 1000
width = 1000
frameRate = 130
photon_count = 5

m87 = Blackhole( width/2, height/2, mass, gravity, light_speed)
photons = []
start = height / 2
end = (height / 2) - m87.rs * 2.6
print("Start" , start)
print("m87", m87.rs)
print("End", end)

for i in range(500,900):
    if i % photon_count == 0:
        photons.append(Photon(width/2 + (width / 4), i, light_speed,delta_time))



y = end
i = 0


def setup():
    size(width,height)
    background(255)
    

def draw():
    m87.show()
    background(255)

    for p in photons:
        m87.pull(p)
        p.update()
        p.show()

if __name__ == '__main__':
    run(frame_rate = frameRate)