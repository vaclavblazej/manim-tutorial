from manim import *
config.frame_width=1
config.pixel_height=400
config.pixel_width=1200

import random

def st(scene, pos):
    res = Star(
            n=min(random.randint(5, 8), random.randint(5, 8)),
            outer_radius=0.003*(min(min(random.randint(3,10), random.randint(3,10)), random.randint(3,10))),
            stroke_opacity=1,
            stroke_width=0.1,
            fill_color=WHITE,
            fill_opacity=1,
            )
    res.set(offset=random.randint(0, 100)/100)
    res.move_to(pos)
    res.rotate(random.randint(1,100))
    scene.add(res)
    return res

def rndpos(c=2000, w=5, h=2):
    c/=10
    w/=10
    h/=10
    return [random.randint(-c,c)/c*w, random.randint(-c,c)/c*h, 0]

def flicker(star):
    #  anim = []
    #  for i in range(random.randint(1, 7)):
        #  anim.append((i))
    #  anim = list(sorted(anim))
    #  start = star.get_fill_opacity()
    return star.set_fill(opacity=0.5+random.randint(-10,10)/10)

class Main(Scene):
    def construct(self):
        res = []
        for i in range(100):
            star = st(self, rndpos())
            star.add_updater(flicker)
            res.append(star)
        #  self.play(*map(flicker, res))
        self.wait(4)
