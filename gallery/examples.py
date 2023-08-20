from manim import *
config.frame_width=12

class Brace(Scene):
    def construct(self):
        a = Dot([0,0,0])
        b = Dot([2,1,0])
        line = Line(a.get_center(), b.get_center()).set(color=ORANGE)
        b1 = BraceBetweenPoints(b.get_center(), a.get_center())
        b1text = b1.get_tex("x-x_1")
        self.add(VGroup(line, a, b, b1, b1text).move_to(ORIGIN))


class VectorArrow(Scene):
    def construct(self):
        a = Dot(ORIGIN)
        b = Vector([2,2,0])
        self.add(
                NumberPlane(),
                Tex("(0,0)").next_to(a, DOWN),
                Tex("(2,2)").next_to(b.get_end(), RIGHT),
                b,
                a,
                )


class Boolean(Scene):
    def construct(self):
        a = Square(1, fill_opacity=0.5)
        b = Triangle(fill_opacity=0.5).shift(0.2,0.2)
        g = Group(a, b).shift(4*LEFT)
        c = Intersection(a, b, fill_opacity=1, color=GREEN)
        u = Union(a, b, fill_opacity=1, color=ORANGE)
        e = Exclusion(a, b, fill_opacity=1, color=YELLOW)
        d = Difference(a, b, fill_opacity=1, color=BLUE)
        dd = Difference(b, a, fill_opacity=1, color=RED)
        self.add(g)
        self.play(FadeIn(c), run_time=0.6)
        self.play(c.animate.scale(0.6).shift(5*RIGHT + 2*UP))
        self.play(FadeIn(Text("Intersection").next_to(c, RIGHT)))
        self.play(FadeIn(u), run_time=0.6)
        self.play(u.animate.scale(0.6).shift(5*RIGHT))
        self.play(FadeIn(Text("Union").next_to(u, RIGHT)))
        self.play(FadeIn(e), run_time=0.6)
        self.play(e.animate.scale(0.6).shift(5*RIGHT - 2*UP))
        self.play(FadeIn(Text("Exclusion").next_to(e, RIGHT)))
        self.play(FadeIn(d), FadeIn(dd), run_time=0.6)
        self.play(d.animate.scale(0.6).next_to(g, UP+LEFT),
                  dd.animate.scale(0.6).next_to(g, DOWN+LEFT))
        self.play(FadeIn(Text("Difference a-b").next_to(d, RIGHT)),
                  FadeIn(Text("Difference b-a").next_to(dd, RIGHT)),
                  )
        self.wait(2)

class MovingPoint(Scene):
    def construct(self):
        a = Dot()
        c = Circle(1)
        self.add(c, a)
        self.play(GrowFromCenter(c))
        self.play(a.animate.shift(RIGHT))
        self.play(MoveAlongPath(a, c), rate_func=linear, run_time=2)
        self.play(Rotating(a, about_point=2*RIGHT, angle=PI), run_time=2)
        self.play(MoveAlongPath(a, c), rate_func=linear, run_time=2)
        #  self.play
        #  self.wait(2)
