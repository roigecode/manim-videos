from manim import *
from math import sqrt, exp, pi, erf
from manim.mobject.mobject import T
from manim.utils import scale
import csv
import numpy as np

class MainFunction(MovingCameraScene):
    def construct(self):
        t1 = Tex(r'You take a PCR \small{\textit{(Polymerase Chain Reaction)}} test and get a',r' positive ',r'result... \\ How likely is it that you ',r'actually',r' have',r' COVID-19?', font_size=35)
        t1[1].set_color_by_gradient([PURPLE,PINK,ORANGE])
        t1[5].set_color_by_gradient([PURPLE,PINK,ORANGE])
        t2 = Tex(r'\textit{(A Spain based rough estimation)}', font_size=20).move_to(DOWN*0.85)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)
        self.play(Unwrite(t1), Unwrite(t2), run_time=0.75)
        self.wait(0.5)

        t3 = Tex(r"Let's use",r" Bayes' Theorem")
        t3[1].set_color_by_gradient([GREEN,BLUE])
        sr = SurroundingRectangle(t3).set_color_by_gradient([GREEN,BLUE])
        self.play(Write(t3))
        self.play(Create(sr))
        self.wait(0.5)
        self.play(Unwrite(t3), Uncreate(sr), run_time=0.75)
        self.wait()

        pc = MathTex(r'P(C) \equiv \text{ Prob. of having',r' COVID-19}',font_size=30).move_to(UP)
        pc[1].set_color_by_gradient([PURPLE,PINK,ORANGE])
        ppc = MathTex(r'P(\oplus \mid C) \equiv \text{ Prob. of getting a',r' positive',r' test result having',r' COVID-19}',font_size=30).move_to(UP*0.5)
        ppc[1].set_color_by_gradient([PURPLE,PINK,ORANGE])
        ppc[3].set_color_by_gradient([PURPLE,PINK,ORANGE])
        ppnc = MathTex(r'P(\oplus \mid C^c) \equiv  \text{ Prob. of getting a}', r'\text{ false positive} ',r'\text{ test result }',r'\text{NOT having COVID-19}',font_size=30)
        ppnc[1].set_color_by_gradient([PURPLE,PINK,ORANGE])
        ppnc[3].set_color_by_gradient([PURPLE,PINK,ORANGE])
        vgTexts = VGroup(pc,ppc,ppnc)

        self.play(Write(pc))
        self.wait()
        self.play(Write(ppc))
        self.wait()
        self.play(Write(ppnc))

        self.play(vgTexts.animate.arrange(DOWN,buff=.2,aligned_edge=LEFT))
        self.play(vgTexts.animate.shift(UP*3))

        sfv = SurroundingRectangle(vgTexts).set_color_by_gradient([PURPLE,PINK,ORANGE])
        self.play(Write(sfv))

        self.wait()

        pc1 = MathTex(r'P(C) = \dfrac{5.29\cdot 10^6}{47.35 \cdot 10^6} = \dfrac{5.29}{47.35} \approx 0.11^{\text{ ref}_{1,2}}',font_size=30).move_to(UP)
        ppc1 = MathTex(r'P(\oplus \mid C) = 0.89^{\text{ ref}_3}',font_size=30)
        ppnc1 = MathTex(r'P(\oplus \mid C^c) = 0.38^{\text{ ref}_4}',font_size=30).move_to(DOWN)
        vgT1 = VGroup(pc1,ppc1,ppnc1)

        self.play(TransformMatchingTex(pc.copy(),pc1,transform_mismatches=True))
        self.wait(1.5)
        self.play(TransformMatchingTex(ppc.copy(),ppc1,transform_mismatches=True))
        self.wait()
        self.play(TransformMatchingTex(ppnc.copy(),ppnc1,transform_mismatches=True))
        self.wait()
        self.play(vgT1.animate.arrange(DOWN,buff=.2,aligned_edge=LEFT))
        #self.play(Write(pc1))
        #self.play(Write(ppc1))
        #self.play(Write(ppnc1))

        self.play(vgT1.animate.shift(UP*1.2,LEFT*2.8))
        sfv2 = SurroundingRectangle(vgT1).set_color_by_gradient([ORANGE,PURPLE])
        self.play(Write(sfv2))

        allg = VGroup(vgT1,vgTexts)
        SRT = SurroundingRectangle(allg).set_color_by_gradient([YELLOW_C,ORANGE,PINK,PURPLE])

        self.wait(0.5)
        self.play(Write(SRT), FadeOut(sfv), FadeOut(sfv2)) 

        probt = Tex(r'But what is the probability of having ', r'COVID-19 ',r'having tested ',r'POSITIVE ',r'in a PCR?',font_size=30).move_to(DOWN*0.5)
        probt[1].set_color_by_gradient([GREEN_C,BLUE_C])
        probt[3].set_color_by_gradient([GREEN_C,BLUE_C])
        self.play(Write(probt))
        self.wait()

        pcmidoplus = MathTex(r'P(C \mid \oplus)',font_size=30).move_to(DOWN*1.75).shift(LEFT*4).set_color_by_gradient([GREEN_C,BLUE_C])
        form = MathTex(r'= \dfrac{P(\oplus \mid C) \cdot P(C)}{P(\oplus)}',font_size=30).move_to(DOWN*1.75).shift(LEFT*2)
        form1 = MathTex(r'= \dfrac{P(\oplus \mid C) \cdot P(C)}{P(\oplus \mid C) \cdot P(C) + P(\oplus C^c)\cdot P(C^c))}',font_size=30).move_to(DOWN*1.75).shift(RIGHT*2)
        form2 = MathTex(r'= \dfrac{0.89 \cdot 0.11}{0.89 \cdot 0.11 + 0.38 \cdot 0.89}',font_size=30).move_to(DOWN*1.75).shift(RIGHT*1.2)
        res1 = MathTex(r'= \dfrac{11}{49} \approx ',r'22\%',font_size=30).move_to(DOWN*1.75).shift(RIGHT*4)
        
        self.play(Write(pcmidoplus),Write(form))
        self.wait()
        self.play(TransformMatchingTex(form.copy(),form1, transform_mismatches=True, key_map={"P(\oplus \mid C) \cdot P(C)":"P(\oplus \mid C) \cdot P(C)","P(\oplus)":"P(\oplus \mid C) \cdot P(C) + P(\oplus C^c)\cdot P(C^c))"}))
        self.wait()
        self.play(FadeOut(form1),TransformMatchingTex(pc1.copy(),form2,transform_mismatches=True),TransformMatchingTex(ppc1.copy(),form2,transform_mismatches=True),TransformMatchingTex(ppnc1.copy(),form2,transform_mismatches=True))
        self.wait()
        self.play(TransformMatchingTex(form2.copy(),res1,transform_mismatches=True))

        self.play(res1[1].animate.set_color(PURE_GREEN))
        rr = SurroundingRectangle(res1[1]).set_color(PURE_GREEN)
        self.play(Create(rr))
        self.wait(2)
        self.play(res1[1].animate.set_color_by_gradient([GREEN_C,BLUE_C]), Uncreate(rr),)
        self.wait()

        eqG = VGroup(probt,res1[1])
        CD1 = Dot()
        CENTERDOT = Dot().move_to(DOWN*1.75)

        self.play(Uncreate(pcmidoplus), Uncreate(form), Uncreate(form2), Unwrite(res1[0]),FadeOut(vgTexts),FadeOut(vgT1), FadeOut(SRT))
        self.play(res1[1].animate.move_to(CENTERDOT).shift(UP*0.3).scale(2))
        self.play(eqG.animate.move_to(CD1))

        s22 = SurroundingRectangle(res1[1]).set_color_by_gradient([GREEN_C,BLUE_C])
        self.play(Write(s22))
        self.wait()

        srf = SurroundingRectangle(eqG).set_color_by_gradient([GREEN_C,BLUE_C])
        self.play(Uncreate(s22))
        self.play(Write(srf))

        self.wait()
        self.play(Uncreate(srf), FadeOut(probt),FadeOut(res1[1]))
        self.wait()

        gfi = VGroup(probt, res1[1])

        refs = Tex(r'\underline{References:}')
        ref1 = Tex(r'1.- Eurostat. (2021, 1st January). \textit{Population on January 1st by age and sex}. Retrieved: 14 December 2021, from ',r'\underline{https://ec.europa.eu/eurostat/data/database}',font_size=20)
        ref1[1].set_color(BLUE_C)
        ref2 = Tex(r'2.- INE, Instituto Nacional de Estadística. (2021, 1st January). INEbase: Cifras de población y Censos demográficos. INE. Retrieved: 14 December 2021.',font_size=20)
        ref3 = Tex(r'3.- Kucirka, L. M., Lauer, S. A., Laeyendecker, O., Boon, D., \& Lessler, J. (2020, 18th August). \textit{Variation in False-Negative Rate of Reverse Transcriptase Polymerase Chain Reaction-Based SARS-CoV-2 Tests by Time Since Exposure}. Annals of Internal Medicine, 173(4), 262-267. Retrieved: 14 December 2021 from ',r'\underline{https://doi.org/10.7326/m20-1495}',font_size=20).move_to(DOWN)
        ref3[1].set_color(BLUE_C)
        ref4 = Tex(r'4.- Redacción Médica. (2020, 27 NOvember). \textit{¿Cuál es el \% de fallo de la PCR en Covid-19?} Retrieved: 14 December 2021, from ',r'\underline{https://www.redaccionmedica.com/recursos-salud/faqs-covid19/cual-es-el-porcentaje-de-fallo-de-la-pcr}',font_size=20).move_to(DOWN*2)
        ref4[1].set_color(BLUE_C)

        self.play(Write(refs))
        self.play(refs.animate.shift(UP*3))
        self.wait(0.5)

        self.play(Write(ref1))
        self.play(ref1.animate.shift(UP*2))
        self.wait(0.5)

        self.play(Write(ref2))
        self.play(ref2.animate.shift(UP))
        self.wait(0.5)

        self.play(Write(ref3))
        self.play(ref3.animate.shift(UP*0.6))
        self.wait(0.5)

        self.play(Write(ref4))
        self.wait(3)
        self.play(Unwrite(refs), Unwrite(ref1), Unwrite(ref2), Unwrite(ref3), Unwrite(ref3), Unwrite(ref4))

        self.wait(3)