from manim import *
from manim import Create, Scene, Transform, ReplacementTransform, FadeOut, Square, PI, PINK, Circle, TracedPath, Dot, RIGHT, Line, Rotate

from random import randint


#  import networkx as nx

#  G = nx.Graph()
#  G = nx.erdos_renyi_graph(60, 0.1)
#  for i in range(5):
    #  G.add_node("Child_%i" % i)
    #  G.add_node("Grandchild_%i" % i)
    #  G.add_node("Greatgrandchild_%i" % i)
    #  G.add_edge("ROOT", "Child_%i" % i)
    #  G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
    #  G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

#  nodes = 500
#  for i in range(nodes):
    #  G.add_node("Node_%i" % i)
#  for i in range(1, nodes):
    #  G.add_edge('Node_%i' % (randint(0, i-1)), 'Node_%i' % i)


class GraphTest(Scene):
    def construct(self):
        GD = Graph(list(G.nodes), list(G.edges), layout="spring", layout_scale=10)
        self.play(Create(GD))
        self.wait()
        self.play(Uncreate(GD))


class Shapes(Scene):
    def construct(self):
        dots = []
        dots.append(Dot())
        dots.append(AnnotationDot())
        dots.append(LabeledDot(MathTex(r'\alpha').set_color(PURPLE)))
        #  self.add(Group(*dots).arrange(buff=1).shift(2*UP))
        for i, shape in enumerate(dots):
            self.add(shape.shift(i*DOWN+2*LEFT))

        circular = []
        circular.append(Arc(0.2, 0, PI/2))
        circular.append(AnnularSector(0.3, 0.4, PI*3/2, color=GREEN))
        circular.append(Annulus(0.45, 0.5, color=BLUE))
        circular.append(Circle(0.6, color=RED))
        circular.append(Ellipse(1.4, 1.2, color=ORANGE))
        for shape in circular:
            self.add(shape.shift(LEFT+DOWN))

        curves = []
        curves.append(ArcBetweenPoints(ORIGIN, LEFT, PI / 2))
        curves.append(CurvedArrow(ORIGIN, LEFT, radius=PI / 2))
        curves.append(CurvedDoubleArrow(ORIGIN, LEFT))
        curves.append(CubicBezier(ORIGIN, UP, LEFT+DOWN, LEFT))
        for i, shape in enumerate(curves):
            self.add(shape.shift(2*RIGHT + i*DOWN))


class Hours(Scene):
    def construct(self):
        self.add(Circle(1, color=RED))
        minutes = Line(ORIGIN, UP*0.9)
        hours = Line(ORIGIN, UP*0.6)
        self.play(Rotate(minutes, angle=-12*2*PI, about_point=ORIGIN, rate_func=linear, run_time=10),
                  Rotate(hours, angle=-2*PI, about_point=ORIGIN, rate_func=linear, run_time=10))


class Main(Scene):
    def construct(self):
        pass


        #  a = Dot(RIGHT * 2)
        #  b = TracedPath(a.get_center, dissipating_time=2, stroke_opacity=[0, 1])
        #  self.add(a, b)
        #  self.play(a.animate(path_arc=PI / 4).shift(LEFT * 2))
        #  self.play(a.animate(path_arc=-PI / 4).shift(LEFT * 2))
        #  self.wait()

        #  circle = Circle()
        #  circle.set_fill(PINK, opacity=0.5)

        #  square = Square()
        #  square.rotate(PI / 4)

        #  self.play(Create(square))
        #  self.play(square.animate.rotate(PI / 4))
        #  self.play(Transform(square, circle))
        #  self.play(FadeOut(square))
        #  #  self.play(ReplacementTransform(square, circle)) replaces with circle
        #  text=MathTex(
            #  "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            #  "g(x)\\frac{d}{dx}f(x)"
        #  )
        #  self.play(Write(text))
        #  framebox1 = SurroundingRectangle(text[1], buff = .1)
        #  framebox2 = SurroundingRectangle(text[3], buff = .1)
        #  self.play(
            #  Create(framebox1),
        #  )
        #  self.wait()
        #  self.play(
            #  ReplacementTransform(framebox1,framebox2),
        #  )
        #  self.wait()
