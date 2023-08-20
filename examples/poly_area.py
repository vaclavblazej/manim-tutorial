from manim import *
import numpy

config.frame_width = 10

points = list(map(lambda x: x + [0], [
    [0, 0],
    [2, -1],
    [3, 1],
    [2, 0],
    [1, 2],
    [-1, 1],
    [-1, -1]
]))

def vec(a, b):
    return a[0]*b[1] - a[1]*b[0]

def show_area_computation(scene, origin_point, points):
    origin = Dot(origin_point)
    scene.play(Create(origin))
    scene.wait(0.2)
    res = [origin]
    time_anim = 4.0 / len(points)
    for idx in range(len(points)):
        a = points[idx]
        b = points[(idx+1)%len(points)]
        dr_poly = Polygon(origin_point, a, b, fill_opacity=0.3, stroke_opacity=0)
        if vec(numpy.subtract(a,origin_point), numpy.subtract(b,origin_point)) > 0:
            dr_poly.set(fill_color=GREEN)
        else:
            dr_poly.set(fill_color=RED)
        res.append(dr_poly)
        scene.play(Create(dr_poly, rate_func=rate_functions.linear), run_time=time_anim)
    return res


def area_computation(scene, points, origin_point):
    polygon = Polygon(*points, color=BLUE, fill_color=GREEN)
    scene.play(Create(polygon), run_time=1)
    res = show_area_computation(scene, origin_point, points)
    scene.wait(1)
    scene.play(FadeOut(*res), polygon.animate.set_fill(opacity=0.3))
    scene.wait(1)
    scene.play(FadeOut(polygon))

class Main(Scene):
    def construct(self):
        area_computation(self, list(map(lambda x: x + [0], [
            [1,0],
            [0,1.414],
            [-1,0]
            ])), [0,-1,0])
        area_computation(self, list(map(lambda x: x + [0], [
            [0, 0],
            [2, -1],
            [3, 1],
            [2, 0],
            [1, 2],
            [-1, 1],
            [-1, -1]
            ])), [-1.4, 0.2, 0])
