from p5 import *

# Schwarzschild Radius Constants 
# Using M87 Blackhole Mass which is 2.6 Billion * Sun

light_speed = 299792458
gravity = 6.67E-11
mass = 2.6E9 * 1.989E30
s_radius = (2 * gravity * mass) / (light_speed ** 2)

def setup():
    size(500,500)
    background(255)



run()