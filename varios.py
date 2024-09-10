from math import *
from os import write
from manim import *
from numpy import array, flatiter, left_shift


class MainFunction(MovingCameraScene):
    def construct(self):
        # Create title and first equation:
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")

        t = MathTex(r'10 \xrightarrow{+4} 2', font_size=100)

        self.play(Write(t))

        self.wait(2)

        self.play(Unwrite(t))

        self.wait(2)
     

