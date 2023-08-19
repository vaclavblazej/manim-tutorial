from manim import *
#  import manim as m
#  from manim import DOWN, LEFT, UP, RIGHT, ORIGIN
#  from manim import RED, PURPLE, BLUE, GREEN, ORANGE
#  from manim import PI

#  from random import randint


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


#  class GraphTest(m.Scene):
    #  def construct(self):
        #  GD = m.Graph(list(G.nodes), list(G.edges), layout="spring", layout_scale=10)
        #  self.play(Create(GD))
        #  self.wait()
        #  self.play(Uncreate(GD))




class Main(m.Scene):
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
