from manim import *
from math import sqrt, exp, pi, erf
from manim.mobject.mobject import T
from manim.utils import scale
import csv
import numpy as np


class MainFunction(MovingCameraScene):
    def construct(self):

        l0 = Tex(r"Contrato para").move_to(UP*2.5)

        l1 = Tex(r" vender 100 kg de trigo").move_to(UP*1.5)
        #l1[0].set_color_by_gradient([PURE_RED,RED])
        #sr1 = SurroundingRectangle(l1).set_color_by_gradient([PURE_RED,RED])

        l2 = Tex(r"el día", r" 01/01/2023",r" a ",r"100\$/kg.").move_to(UP*0.5)
        #l2[1].set_color_by_gradient([ORANGE,YELLOW])
        l2[3].set_color_by_gradient([GREY,WHITE])
        #sr2 = SurroundingRectangle(l2[1]).set_color_by_gradient([ORANGE,YELLOW])
        sr22 = SurroundingRectangle(l2[3]).set_color_by_gradient([PURE_GREEN,GREEN])

        l3 = Tex(r" Firmado por ambas partes el").move_to(DOWN*0.5)

        l4 = Tex(r"01/01/2022").move_to(DOWN*1.5)
        #l4.set_color_by_gradient([ORANGE,PINK,PURPLE])
        #sr4 = SurroundingRectangle(l4).set_color_by_gradient([ORANGE,PINK,PURPLE])

        l5 = Tex(r"Precio actual: ", r"75\$/kg").move_to(DOWN*2.5)
        l5[1].set_color_by_gradient([ORANGE,PINK,PURPLE])
        sr5 = SurroundingRectangle(l5[1]).set_color_by_gradient([ORANGE,PINK,PURPLE])

        g = VGroup(l0,l1,l2,l3,l4,l5)
        sr = SurroundingRectangle(g, buff=0.5).set_color(WHITE)

        self.play(Write(l0), Write(l1), Write(l2), Write(l3), Write(l4) , Write(l5), Write(sr), run_time=0.7)

        self.play(Write(sr5))
        self.wait()
        self.play(ReplacementTransform(sr5,sr22), l2[3].animate.set_color_by_gradient([PURE_GREEN,GREEN]), l5[1].animate.set_color_by_gradient([GREY,WHITE]))

        self.wait()

        self.play(g.animate.set_color(PURE_GREEN), ReplacementTransform(sr22,sr))
        self.play(sr.animate.set_color(PURE_GREEN))
   

        #self.play(g.animate.arrange(DOWN,buff=0.2, aligned_edge=LEFT))

        #gul = VGroup(g,sr)

        #tete = Tex(r'01/01/2022', font_size=200)
        #self.wait(5)
        #self.play(TransformMatchingTex(l4,tete,transform_mismatches=True), FadeOut(gul))

        self.wait(5)