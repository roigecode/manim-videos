from manim import *
from math import sqrt
from manim.utils import scale

class MainFunction(MovingCameraScene):
    def construct(self):
        principal(self)
        self.wait(2)

def principal(self):
    h = MathTex(r"1899", font_size=150)
    
    self.play(Write(h))
    self.wait()
    self.play(Unwrite(h))