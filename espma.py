from manim import *
from math import sqrt
from manim.utils import scale, tex
import csv
import numpy as np

class MainFunction(MovingCameraScene):
    def construct(self):
        nov = MathTex(r'90\%',font_size=300).set_color_by_gradient([GREEN_C,BLUE_C])
        pe = Tex(r'probabilidad de acierto').set_color_by_gradient([GREEN_C,BLUE_C]).move_to(DOWN)

       
        self.play(Write(nov))
        self.play(Flash(nov,num_lines=30,flash_radius=3+SMALL_BUFF, color=[GREEN_C,BLUE_C]))
        self.play(nov.animate.move_to(UP))
        self.play(Write(pe))
        self.wait()
        self.play(Unwrite(nov), Unwrite(pe))

        self.wait()

        juan = Tex(r'Juan juega a un juego donde hay dos resultados. ',r'Para jugar debe pagar ', r'\$100',  r'. Si gana, recibe ', r'\$500', r' y la probabilidad de ganar es del ', r'20\%',
         r'. ', r'¿Debería jugar?',font_size=35)

        juan[-1].set_color_by_gradient([GREEN_C,BLUE_C])

        for i in range(len(juan)):
            self.play(Write(juan[i]))

        self.wait(2)
        self.play(juan.animate.shift(UP*2.5))

        rect = Rectangle(width=3, height=1.5, grid_xstep=1, grid_ystep=0.5)
        grid = VGroup(rect).scale(2.5).shift(DOWN)
        self.play(Write(rect))

        v = 35

        res = Tex(r'Resultados', font_size=v).shift(LEFT*2.5,UP*0.2)

        val = Tex(r'Dinero', font_size=v).move_to(res)
        val.shift(DOWN*1.2)

        gana = Tex(r'Gana', font_size=v).move_to(res)
        gana.shift(RIGHT*2.5)

        ganadin = MathTex(r'\$500', font_size=v).move_to(gana).set_color_by_gradient([PURE_GREEN,GREEN_C])
        ganadin.shift(DOWN*1.2)

        pierde = Tex(r'Pierde', font_size=v).move_to(gana)
        pierde.shift(RIGHT*2.5)

        pierdedin = MathTex(r'-\$100', font_size=v).move_to(pierde).set_color_by_gradient([PURE_RED,RED_C])
        pierdedin.shift(DOWN*1.2)

        prob = Tex(r'Probabilidad', font_size=v).move_to(val)
        prob.shift(DOWN*1.3)

        probwin = MathTex(r'20\%', font_size=v).move_to(prob).set_color_by_gradient([ORANGE,YELLOW])
        probwin.shift(RIGHT*2.6)

        probloss = MathTex(r'80\%', font_size=v).move_to(probwin).set_color_by_gradient([ORANGE,PINK])
        probloss.shift(RIGHT*2.5)

        self.play(Write(res), Write(gana), Write(pierde), Write(val), Write(prob))

        self.play(juan[2].animate.set_color_by_gradient([PURE_RED,RED_C]), ApplyWave(juan[2], direction=RIGHT,amplitude=0.3))
        self.play(TransformFromCopy(juan[2],pierdedin))
        self.wait()

        self.play(juan[4].animate.set_color_by_gradient([PURE_GREEN,GREEN_C]), ApplyWave(juan[4], direction=RIGHT,amplitude=0.3))
        self.play(TransformFromCopy(juan[4],ganadin))
        self.wait()

        self.play(juan[6].animate.set_color_by_gradient([ORANGE,YELLOW]), ApplyWave(juan[6], direction=RIGHT,amplitude=0.3))
        self.play(TransformFromCopy(juan[6], probwin))
        self.wait()

        self.play(ApplyWave(probwin, direction=RIGHT))
        self.play(TransformFromCopy(probwin,probloss))

        recuadro = VGroup(res,val,gana,ganadin,pierde,pierdedin,prob,probwin,probloss,grid)

        self.wait(2)

        self.play(recuadro.animate.scale(0.5))
        self.play(recuadro.animate.shift(RIGHT*4, UP*1.5))

        espd = MathTex(r'\mathbb{E}[X] = \sum_{i=1}^{n} x_i P[X = x_i]').shift(UP, LEFT*3.5)
        espc = MathTex(r'\mathbb{E}[X] = \int_{\mathbb{R}} x f_{X}(x)dx').set_color_by_gradient([GREEN_C,BLUE_C]).shift(DOWN,LEFT)
        espg = MathTex(r'\mathbb{E}[X] = \int_{\Omega} X(\omega)dP(\omega); \quad X \in (\Omega,\mathcal{F},P)').set_color_by_gradient([ORANGE,YELLOW]).shift(DOWN*3,LEFT)

        self.play(Write(espd))
        self.play(espd.animate.set_color_by_gradient([ORANGE,PINK,PURPLE]))
        self.wait()
        self.play(espd.animate.set_color([WHITE]))
        self.wait()
        self.play(Write(espc))
        self.wait()
        self.play(Write(espg))
        self.wait(2)
        self.play(Unwrite(espg), Unwrite(espc))

        espd1 = MathTex(r'\mathbb{E}[X] = x_1 P(x_1) + x_2 P(x_2)').shift(DOWN*0.5,LEFT*3.1)

        espd2 = MathTex(r'\mathbb{E}[X] = ',r'500',r' \cdot ',r'0.2',r' + (',r'-100',r') \cdot ',r'0.8').shift(DOWN*1.5, LEFT*2.8)
        espd2[1].set_color_by_gradient([PURE_GREEN,GREEN_C])
        espd2[3].set_color_by_gradient([ORANGE,YELLOW])
        espd2[5].set_color_by_gradient([PURE_RED,RED_C])
        espd2[7].set_color_by_gradient([ORANGE,PINK])


        espd3 = MathTex(r'\mathbb{E}[X] = \$20').shift(DOWN*2.5, LEFT*3)

        self.play(TransformMatchingTex(espd.copy(),espd1, transform_mismatches=True))
        self.wait()
        self.play(TransformMatchingTex(espd1.copy(),espd2, transform_mismatches=True))
        self.wait()
        self.play(TransformMatchingTex(espd2.copy(),espd3, transform_mismatches=True))
        self.play(Circumscribe(espd3, color=PURE_GREEN), espd3.animate.set_color_by_gradient([PURE_GREEN,GREEN_C]))
        self.wait(2)

        self.play(FadeOut(espd,espd1,espd2), espd3.animate.shift(UP*3.5,LEFT*1.5))

        J10 = Tex(r'Juega 10 veces $=$ ', r'$\$200$').shift(LEFT*3.2)
        J100 = Tex(r'Juega 100 veces $=$ ', r'$\$2000$').shift(DOWN,LEFT*3)

        J10[1].set_color_by_gradient([PURE_GREEN,GREEN_C])
        J100[1].set_color_by_gradient([PURE_GREEN,GREEN_C])

        self.play(Write(J10))
        self.play(Write(J100))
        self.wait()

        vt = VGroup(juan, espd3, recuadro, J10, J100)
        self.play(FadeOut(vt))

        self.wait()

        comp = Tex(r'¿Comprarías el sistema con ',r'90\%', r' de probabilidad de acierto?')
        comp[1].set_color_by_gradient([GREEN_C, BLUE_C])
        self.play(Write(comp))
        self.play(Flash(comp[1],num_lines=15,flash_radius=0.5+SMALL_BUFF, color=[GREEN_C,BLUE_C]))
        self.play(comp.animate.shift(UP*2.5))


        etr = MathTex(r'\mathbb{E}[X] = ', r'\text{?}_G', r' \cdot ', r'0.9',r' + ',r'\text{?}_P', r' \cdot ', r'0.1')
        etr[1].set_color_by_gradient([YELLOW, GREEN_C])
        etr[3].set_color_by_gradient([GREEN_C, BLUE_C])
        etr[5].set_color_by_gradient([YELLOW, RED_C])
        etr[7].set_color_by_gradient([ORANGE,PINK])

        self.play(Write(etr))
        self.play(Circumscribe(etr[1], color=GREEN))
        self.play(Circumscribe(etr[5], color=ORANGE))

        etr2 = MathTex(r'0 < ', r'x', r' \cdot ', r'9',r' + ',r'y', r' \cdot ', r'1').shift(UP*0.2)
        etr2[1].set_color_by_gradient([YELLOW, GREEN_C])
        etr2[3].set_color_by_gradient([GREEN_C, BLUE_C])
        etr2[5].set_color_by_gradient([YELLOW, RED_C])
        etr2[7].set_color_by_gradient([ORANGE,PINK])

        self.play(etr.animate.shift(UP*1.5))
        self.play(TransformMatchingTex(etr.copy(),etr2,transform_mismatches=True))
        self.wait()

        etr3 = MathTex(r'0 = ', r'x', r' \cdot ', r'9',r' + ',r'y', r' \cdot ', r'1').shift(UP*0.2)
        etr3[1].set_color_by_gradient([YELLOW, GREEN_C])
        etr3[3].set_color_by_gradient([GREEN_C, BLUE_C])
        etr3[5].set_color_by_gradient([YELLOW, RED_C])
        etr3[7].set_color_by_gradient([ORANGE,PINK])

        self.play(TransformMatchingTex(etr2,etr3,transform_mismatches=False))

        eqd = Tex(r'Ecuación diofántica/diofantina:').shift(DOWN).set_color_by_gradient([ORANGE,PINK,PURPLE])
        self.play(Write(eqd))

        sol1 = MathTex(r'x = 0 + n').shift(DOWN*2)
        sol2 = MathTex(r'y = 0 -9n').shift(DOWN*2.5)
        sol3 = MathTex(r'n \in \mathbb{Z}').shift(DOWN*3)

        gsols = VGroup(sol1,sol2,sol3)

        self.play(Write(sol1), Write(sol2), Write(sol3))
        self.play(Circumscribe(gsols, color=ORANGE))
        
        sol11 = MathTex(r'x = 1; \quad x \in [0,+\infty]').shift(DOWN*2)
        sol22 = MathTex(r'y = -9; \quad y \in [-\infty, 0]').shift(DOWN*2.5)
        sol33 = MathTex(r'n \in \mathbb{Z^{+}}} \longrightarrow 1').shift(DOWN*3)

        self.play(TransformMatchingTex(sol3,sol33,transform_mismatches=True))
        self.play(TransformMatchingTex(sol1,sol11,transform_mismatches=True), TransformMatchingTex(sol2,sol22, transform_mismatches=True))
        
        gsols2 = VGroup(sol11,sol22,sol33)

        self.play(TransformMatchingTex(etr3,etr2,transform_mismatches=False))
        self.wait()

        sol111 = MathTex(r'x > 1;\quad x \in [0,+\infty]').shift(DOWN*2)
        self.play(TransformMatchingTex(sol11,sol111,transform_mismatches=True))
        self.wait()

        sol222 = MathTex(r'y > -9; \quad y \in [-\infty, 0]').shift(DOWN*2.5)
        self.play(TransformMatchingTex(sol22,sol222,transform_mismatches=True))
        self.wait()

        sr = SurroundingRectangle(gsols2, buff=0.2).set_color_by_gradient([ORANGE,PINK,PURPLE])
        self.play(Write(sr))

        self.wait(3)