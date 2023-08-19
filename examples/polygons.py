from manim import *

#  config.frame_width = 8
#  config.pixel_width = 3200; config.pixel_height = 5600

class Main(Scene):
    def construct(self):
        objs = []
        objs.append(Square(1))
        objs.append(Triangle())
        objs.append(Circle())
        objs.append(RegularPolygon(5))
        objs.append(Star(5))
        objs.append(Rectangle(width=3, height=1))
        objs.append(Polygon([0,0,0], [0,1,0], [1,0,0]))
        self.add(Group(*objs).arrange(DOWN))
