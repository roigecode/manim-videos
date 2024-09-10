from math import *
from cairo import FONT_SLANT_OBLIQUE
from manim import *
import numpy as np
import hashlib
import networkx

class MainFunction(MovingCameraScene):
    def construct(self):
        hash_animation(self)
        self.wait(2)

def hash_animation(self):
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

    ferm = MathTex(r'W_t = \dfrac{1}{\sigma}\cdot ln\left(\dfrac{K}{S_0}\right) - 1 \dfrac{1}{\sigma}\left(\mu - \dfrac{\sigma^2}{2}\right)t', font_size=75)

    self.play(Write(ferm))
    self.wait()
    self.play(Unwrite(ferm))
    self.wait(0.5)
