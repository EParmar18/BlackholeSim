from p5 import *
from Blackhole import Blackhole
from Photon import Photon
import numpy
import math
# Schwarzschild Radius Constants 
# Using M87 Blackhole Mass which is 2.6 Billion * Sun

light_speed = 30
gravity = 6
mass = 6000
s_radius = (2 * gravity * mass) / (light_speed ** 2)
delta_time = 0.1
height = 250
width = 250
frameRate = 144

m87 = Blackhole( width, height, mass, gravity, light_speed)
photons = []
start = height / 2
end = height / 2 - m87.rs * 2.6
print("Start" , start)
print("End", end)

for i in range(100,400):
    if i % 10 == 0:
        photons.append(Photon(400, i, light_speed,delta_time))



y = end
i = 0


def setup():
    size(500,500)
    background(255)
    

def draw():
    m87.show()
    background(255)
    
    stroke(0)
    stroke_weight(1)
    line(0,100,width,100)
    line(0,400,width,400)
    for p in photons:
        m87.pull(p)

        p.update()
        p.show()

if __name__ == '__main__':
    run(frame_rate = frameRate)