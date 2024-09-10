from manim import *
from math import sqrt, exp, pi, erf
from manim.mobject.mobject import T
from manim.utils import scale
import csv
import numpy as np

class MainFunction(MovingCameraScene):
    def construct(self):
        t1 = Tex(r'01/01/2022',font_size=200)
        sr = SurroundingRectangle(t1, buff=0.3).set_color_by_gradient([GREEN_C,BLUE_C])

        self.play(Write(t1))
        self.play(Create(sr))
        self.wait()
        self.play(Uncreate(sr), t1.animate.set_color_by_gradient([GREEN_C,BLUE_C]))
        self.wait(2)
