from manim import *

class Main(Scene):
    def construct(self):
        objs = []
        objs.append(Arc(0.2, 0, PI/2))
        objs.append(AnnularSector(0.3, 0.4, PI*3/2, color=GREEN))
        objs.append(Annulus(0.3, 0.4, color=BLUE))
        objs.append(Circle(0.3, color=RED))
        objs.append(Ellipse(0.3, 0.4, color=ORANGE))
        self.add(Group(*objs).arrange(DOWN))
