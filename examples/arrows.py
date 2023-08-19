from manim import *

class Main(Scene):
    def construct(self):
        s = ORIGIN
        t = 2*LEFT
        tips = [ArrowTriangleTip, ArrowTriangleFilledTip,
                ArrowCircleTip, ArrowCircleFilledTip,
                ArrowSquareTip, ArrowSquareFilledTip,
                StealthTip]
        arrows = map(lambda tip: Arrow(s, t, tip_shape=tip), tips)
        self.add(Group(*arrows).arrange(DOWN))
