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

    ferm = MathTex(r'x \equiv x^{e\cdot d} \text{ mod}(n), \quad \forall x \in \mathbb{Z}_n', font_size=100)

    self.play(Write(ferm))
    self.wait()
    self.play(Unwrite(ferm))
    self.wait(0.5)

    


    
   