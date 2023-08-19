from manim import Scene, Circle, Line, Rotate
from manim import RED, UP, ORIGIN, PI, linear


class Main(Scene):
    def construct(self):
        self.add(Circle(1, color=RED))
        minutes = Line(ORIGIN, UP*0.9)
        hours = Line(ORIGIN, UP*0.6)
        self.play(Rotate(minutes, angle=-12*2*PI, about_point=ORIGIN, rate_func=linear, run_time=10),
                  Rotate(hours, angle=-2*PI, about_point=ORIGIN, rate_func=linear, run_time=10))
