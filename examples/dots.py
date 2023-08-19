from manim import *

class Main(Scene):
    def construct(self):
        objs = []
        objs.append(Dot())
        objs.append(AnnotationDot())
        text = MathTex(r'\alpha').set_color(BLACK)
        objs.append(LabeledDot(text))
        self.add(Group(*objs).arrange(DOWN))
