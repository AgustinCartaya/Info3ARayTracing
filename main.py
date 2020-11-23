#!/usr/bin/env python
"""Puray - a Pure Python Raytracer by Arun Ravindran, 2019"""
import argparse
import importlib
import os

from engine import RenderEngine
from scene import Scene

from color import Color
from light import Light
from material import *
from point import Point
from objects import *
from vector import Vector
from camera import Camera


#----------------------------Example00---------------------------------------------------------
WIDTH = 320
HEIGHT = 200
RENDER_IMG = "Example00.ppm"
CAMERA = Camera( Point(0,-0.35, -1), Vector(0, -1, 0), WIDTH, HEIGHT, -1, -1,1 )

OBJECTS = [
    Sphere(Point(0,10000.5,1), 10000.0, ChequeredMaterial()),
    Sphere(Point(-8,-0.1,8.1), 0.6,  Material( Color.from_hex("#FF0000") ) ),
    Sphere(Point(-6,-0.1,5.1), 0.2,  Material( Color.from_hex("#FFFF00") ) ),
    Sphere(Point(-2,-0.1,3), 0.3,  Material( Color.from_hex("#0000FF") ) ),
    Sphere(Point(2,-0.1,3), 0.6,  Material( Color.from_hex("#00FF00") ) ),


]

LIGHTS = [ 
    
    
    Light(Point(1.5,-.5,-10), Color.from_hex("#FFFFFF")),
    Light(Point(-0.5,-10.5,-10), Color.from_hex("#E6E6E6"))

]



def main():
    
    
    scene = Scene(CAMERA, OBJECTS, LIGHTS)
    engine = RenderEngine()
    image = engine.render(scene)
    with open(RENDER_IMG, "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
