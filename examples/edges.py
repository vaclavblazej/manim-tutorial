from manim import *

class Main(MovingCameraScene):
    def construct(self):
        s = ORIGIN
        t = 4*LEFT
        self.camera.frame.set(ratio=3)
        edges = []
        edges.append(Line(s, t))
        edges.append(Arrow(s, t, buff=0))
        edges.append(DoubleArrow(s, t, buff=0))
        edges.append(ArcBetweenPoints(s, t, angle = PI / 2))
        edges.append(CurvedArrow(s, t, radius=10))
        edges.append(CurvedDoubleArrow(s, t))
        edges.append(CubicBezier(s, s+UP, t+DOWN, t))
        self.add(Group(*edges).arrange(DOWN))
