from p5 import *
from Blackhole import Blackhole
# Schwarzschild Radius Constants 
# Using M87 Blackhole Mass which is 2.6 Billion * Sun

light_speed = 30
gravity = 6
mass = 2.6E9 * 1.989E30
s_radius = (2 * gravity * mass) / (light_speed ** 2)

m87 = Blackhole( 250, 250, 3000, gravity, light_speed)

def setup():
    size(500,500)
    background(255)
    

def draw():
    m87.show()

run()