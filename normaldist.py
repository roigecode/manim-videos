from manim import *
from math import sqrt, exp, pi, erf
from manim.mobject.mobject import T
from manim.utils import scale
import csv
import numpy as np

class MainFunction(MovingCameraScene):
    def construct(self):
        ax = Axes(
            x_range = [-4, 4, 1],
            y_range = [0, 0.4, 0.4],
            x_length = 15,
            y_length = 5,
            tips=False,
            axis_config = {'include_numbers':False}
        )

        # We draw our PDF function:
        curve =  ax.plot(lambda x: PDF_normal(x, 0, 1, 1)) 
        curve.set_color_by_gradient([YELLOW,PINK,PURPLE])

        vg = VGroup(ax,curve).scale(0.6)

        t0 = Tex(r'A beautiful prove for ',r'The Empirical Rule',r' or...')
        t0[1].set_color_by_gradient([PURPLE_C,WHITE])
        self.play(Write(t0))
        self.wait()
        self.play(FadeOut(t0))

        t1 = Tex(r"¿",r"Why is the percentage value within one standard deviation $(1 \sigma)$ range ",r"68\%",r"?", font_size=25)
        t1[2].set_color(PURE_GREEN)

        t2 = MathTex(r'\dfrac{e^{-\frac{(kx - \mu)^2}{2 \sigma^2}}}{\sigma \sqrt{2 \pi}}')
        t2Mid = MathTex(r'\dfrac{e^{-\frac{(1x - 0)^2}{2\cdot 1^2}}}{1 \sqrt{2 \pi}}').shift(LEFT*1.5)
        t2Final = MathTex(r'\dfrac{e^{-\frac{x^2}{2}}}{\sqrt{2 \pi}}').shift(LEFT*1.5)
        t2Int = MathTex(r'\int_{-1}^{1} \dfrac{e^{-\frac{x^2}{2}}}{\sqrt{2 \pi}} dx')
        t2Int2 = MathTex(r'\int_{-1}^{1} \dfrac{e^{-\frac{x^2}{2}}}{\sqrt{2} \sqrt{\pi}} dx')

        t3 = Tex(r'Our', r' PDF - (Probability Density Function)',r' is defined by:',font_size=25).move_to(UP*1.5)
        t3[1].set_color_by_gradient([YELLOW,PINK,PURPLE])

        center_dot = Dot().move_to(UP*2.5)

        mu = MathTex(r'\mu', font_size = 20)
        sigma1 = MathTex(r'1 \sigma', font_size = 20)
        sigma2 = MathTex(r'-1 \sigma', font_size = 20)
        sigma3 = MathTex(r'2 \sigma', font_size = 20)
        sigma4 = MathTex(r'-2 \sigma', font_size = 20)
        sigma5 = MathTex(r'3 \sigma', font_size = 20)
        sigma6 = MathTex(r'-3 \sigma', font_size = 20)

        mu.move_to(ax.coords_to_point(0,0))
        mu.shift(DOWN*0.3)
        sigma1.move_to(ax.coords_to_point(1,0))
        sigma1.shift(DOWN*0.3)
        sigma2.move_to(ax.coords_to_point(-1,0))
        sigma2.shift(DOWN*0.3)
        sigma3.move_to(ax.coords_to_point(2,0))
        sigma3.shift(DOWN*0.3)
        sigma4.move_to(ax.coords_to_point(-2,0))
        sigma4.shift(DOWN*0.3)
        sigma5.move_to(ax.coords_to_point(3,0))
        sigma5.shift(DOWN*0.3)
        sigma6.move_to(ax.coords_to_point(-3,0))
        sigma6.shift(DOWN*0.3)
        
        let = Tex(r'\underline{Let:}').move_to(UP*1.6)
        kt = MathTex(r'k = 1').move_to(UP*0.75)
        mt = MathTex(r'\mu = 0')
        st = MathTex(r'\sigma = 1').move_to(DOWN*0.75)

        iex = Tex(r'When we integrate a PDF we get the probability as the area bellow the bounded curve. We will rewrite our expression as:',font_size=25).move_to(DOWN*1.5)
        iex2 = Tex(r'Our limits of integration are -1 \& 1 because we want to know the value at $1\sigma$',font_size=25).move_to(DOWN*1.5)
        iex3 = Tex(r'Substitute $u = \dfrac{x}{\sqrt{2}}$ then $\dfrac{du}{dx} = \dfrac{1}{\sqrt{2}} \, \therefore\, dx = \sqrt{2}\, du$:', font_size=25).move_to(UP*1.5)
        iex4 = Tex(r'Undo the substitution $u = \dfrac{x}{\sqrt{2}}$:',font_size=30).move_to(DOWN*2)
        iex5 = Tex(r'Now we have $\int f(x)\, dx = F(x)$ so we need to evaluate it between our boundaries to get $\int_{-1}^{1} f(x)\, dx$:',font_size=30).move_to(DOWN*2)

        sr = SurroundingRectangle(iex2).set_color_by_gradient([GREEN_C,BLUE_C])

        alt1 = MathTex(r' = \int_{}^{} \dfrac{2e^{-u^2}}{\sqrt{\pi}} du').move_to(RIGHT*2.5)
        alt2 = MathTex(r' = \dfrac{\text{erf(}u\text{)}}{2}').move_to(RIGHT*1.75)
        alt3 = MathTex(r' = \dfrac{\text{erf(}\frac{x}{\sqrt{2}}\text{)}}{2} + C').move_to(RIGHT*2.5)
        alt4 = MathTex(r'= \text{erf(}\frac{1}{\sqrt{2}}\text{)}').move_to(RIGHT*2)
        alt5 = MathTex(r'= 0.682689...').move_to(RIGHT*2.75)
        alt6 = MathTex(r'\approx 68\%').move_to(RIGHT*2)

        l00 = ax.get_vertical_line(ax.input_to_graph_point(-1,curve), color= WHITE)
        l01 = ax.get_vertical_line(ax.input_to_graph_point(1,curve), color= WHITE)

        tvg = VGroup(let,kt,mt,st).move_to(RIGHT).scale(0.5)
        vg.add(mu,sigma1,sigma2,sigma3,sigma4,sigma5,sigma6, l00,l01)

        self.play(Write(t1))
        self.wait(0.75)
        self.play(t1.animate.move_to(UP*2.5))

        # Re-arrenge text:
        self.play(FadeOut(t1[1]), t1[2].animate.move_to(center_dot.get_center()), t1[0].animate.shift(RIGHT*4),t1[3].animate.shift(LEFT*4))

        self.play(Write(ax))
        self.play(Write(curve), Write(mu), Write(sigma1), Write(sigma2), Write(sigma3), Write(sigma4), Write(sigma5), Write(sigma6), Write(l00), Write(l01))
        self.wait(1)
        self.play(FadeOut(vg))
        self.play(Write(t3))
        self.wait(0.5)
        self.play(Write(t2))
        self.play(t2.animate.shift(LEFT*1.5))
        self.play(Write(tvg))
        self.play(TransformMatchingTex(t2,t2Mid, key_map={"e^{-\frac{(kx - \mu)^2}{2 \sigma^2}}":"e^{-\frac{(1x - 0)^2}{2\cdot 1^2}}","\sigma \sqrt{2 \pi}":"1 \sqrt{2 \pi}"}, 
        transform_mismatches=True))
        self.wait(0.5)
        self.play(TransformMatchingTex(t2Mid,t2Final, key_map={"e^{-\frac{(1x - 0)^2}{2\cdot 1^2}}":"e^{-\frac{x^2}{2}}","\sqrt{2 \pi}":"\sqrt{2 \pi}"}, transform_mismatches=True))
        self.play(Write(iex))
    
        self.play(FadeOut(tvg), TransformMatchingTex(t2Final,t2Int, transform_mismatches=True), FadeOut(t3), iex.animate.shift(UP*3))
        self.wait(0.5)
        self.play(TransformMatchingTex(t2Int, t2Int2, key_map={"1":"1","-1":"-1"},transform_mismatches=True))
        self.play(Write(iex2))
        self.play(Write(sr))
        self.wait(1)
        self.play(FadeOut(iex), Uncreate(sr),FadeOut(iex2))
        self.play(Write(iex3))
        self.play(t2Int2.animate.shift(LEFT*0.75),Write(alt1))
        self.wait(0.5)
        self.play(TransformMatchingTex(alt1,alt2, transform_mismatches=True))
        self.play(FadeOut(iex3), Write(iex4))
        self.play(iex4.animate.shift(UP*3.5))
        self.play(TransformMatchingTex(alt2,alt3, transform_mismatches=True))
        self.play(FadeOut(iex4), Write(iex5))
        self.play(iex5.animate.shift(UP*3.5))
        self.wait(0.5)
        self.play(TransformMatchingTex(alt3,alt4, transform_mismatches=True))
        self.wait(0.5)
        geqvg = VGroup(alt4,t2Int2)
        self.play(geqvg.animate.shift(LEFT*2),TransformMatchingTex(alt4.copy(),alt5, transform_mismatches=True))
        self.wait()
        self.play(TransformMatchingTex(alt5,alt6, transform_mismatches=True))
        self.play(alt6.animate.set_color(PURE_GREEN))
        self.wait(2)

        vgP1 = VGroup(alt6,t1[0],t1[2],t1[3],t2Int2, iex5, alt4)
        self.play(FadeOut(vgP1))
        textfi = Tex("But what does this all mean? Let's check it out visually!")
        self.play(Write(textfi))
        self.play(textfi.animate.shift(UP*2.5))
        self.play(FadeIn(vg))

        l1 = ax.get_vertical_line(ax.input_to_graph_point(-1,curve), color= WHITE)
        l2 = ax.get_vertical_line(ax.input_to_graph_point(1,curve), color= WHITE)
        l3 = ax.get_vertical_line(ax.input_to_graph_point(-2,curve), color= WHITE)
        l4 = ax.get_vertical_line(ax.input_to_graph_point(2,curve), color= WHITE)
        l5 = ax.get_vertical_line(ax.input_to_graph_point(-3,curve), color= WHITE)
        l6  = ax.get_vertical_line(ax.input_to_graph_point(3,curve), color= WHITE)

        textfi2 = MathTex(r"\text{We've just seen that for } 1 \sigma \text{ our value is } \int_{-1}^{1} \dfrac{e^{-\frac{x^2}{2}}}{\sqrt{2 \pi}} dx = \text{erf(}\frac{1}{\sqrt{2}}\text{)} = 0.682689... \,\approx 68\%", font_size=30).move_to(UP*2.5)
        jk = Tex(r"That's just a fancy way to say that the area bellow the curve between $\pm 1\sigma$ is ",r"$\approx 0.68$", font_size=30).move_to(DOWN*3)
        jk[1].set_color_by_gradient([BLUE_D,BLUE_C,BLUE_A])

        textf3 = Tex(r"But what if we want to know it at $2\sigma$ or $3\sigma$?",font_size=30).move_to(UP*2.5)
        textf4 = Tex(r"A beautiful move is just changing the integration limits to $\pm \sigma$: $\int_{-\sigma}^{\sigma} \dfrac{e^{-\frac{x^2}{2}}}{\sqrt{2 \pi}} dx$ but an easier way is to compute: ",font_size=30).move_to(DOWN*3)
        
        eqfin = MathTex(r"\text{erf(}\frac{\sigma}{\sqrt{2}}\text{)}").move_to(UP)
        eqfin1 = MathTex(r"\text{erf(}\frac{1}{\sqrt{2}}\text{)} = 0.682689... \approx 68\%").move_to(DOWN*3).set_color_by_gradient([BLUE_D,BLUE_C,BLUE_A])
        eqfin2 = MathTex(r"\text{erf(}\frac{2}{\sqrt{2}}\text{)} = 0.954499... \approx 95\%").move_to(DOWN*3).set_color_by_gradient([GREEN_D,GREEN_C,GREEN_A])
        eqfin3 = MathTex(r"\text{erf(}\frac{3}{\sqrt{2}}\text{)} = 0.997300... \approx 99\%").move_to(DOWN*3).set_color_by_gradient([RED_D,RED_C,RED_A])

        area1 = ax.get_area(curve, x_range=[-1,1], fill_opacity=0.9)
        area1.set_color_by_gradient([BLUE_D,BLUE_C,BLUE_A])
        area2 = ax.get_area(curve, x_range=[-2,2], fill_opacity=0.9)
        area2.set_color_by_gradient([GREEN_D,GREEN_C,GREEN_A])
        area3 = ax.get_area(curve, x_range=[-3,3], fill_opacity=0.9)
        area3.set_color_by_gradient([RED_D,RED_C,RED_A])

        fivg1 = VGroup(l1,l2,area1)
        fivg2 = VGroup(l3,l4,area2)
        fivg3 = VGroup(l5,l6,area3)

        self.play(FadeOut(textfi))
        self.play(Write(textfi2))
        self.play(Write(jk),Write(l1), Write(l2),sigma1.animate.set_color(BLUE_C), sigma2.animate.set_color(BLUE_C))
        self.play(Create(area1), rate_func=rate_functions.smooth)
        self.play(FadeOut(textfi2))
        self.play(Write(textf3), FadeOut(jk))
        self.wait(0.5)
        self.play(Write(textf4))
        self.wait(0.5)

        self.play(
        FadeOut(textf3), textf4.animate.shift(UP*5.5), FadeOut(ax), FadeOut(curve), FadeOut(fivg1),
        FadeOut(sigma1),FadeOut(sigma2),FadeOut(sigma3),FadeOut(sigma4),FadeOut(sigma5),FadeOut(sigma6),
        FadeOut(l1), FadeOut(l2), FadeOut(mu), FadeOut(l00), FadeOut(l01)
        )

        sr3 = SurroundingRectangle(eqfin).set_color_by_gradient([YELLOW,PINK,PURPLE])
        self.play(Write(eqfin))
        self.play(Create(sr3))
        self.play(Uncreate(sr3), eqfin.animate.set_color_by_gradient([YELLOW,PINK,PURPLE]))
        self.play(eqfin.animate.shift(DOWN*4))
        self.wait(0.5)

        self.play(TransformMatchingTex(eqfin,eqfin1,transform_mismatches=True),Write(ax),Write(sigma1),Write(sigma2),Write(sigma3),Write(sigma4),Write(sigma5),Write(sigma6),Write(curve),Write(l1), Write(l2), Create(area1), rate_func=linear)
        self.wait(1)
        self.play(Uncreate(l1), Uncreate(l2), Uncreate(area1))

        
        self.play(sigma1.animate.set_color(WHITE),
        sigma2.animate.set_color(WHITE),
        sigma3.animate.set_color(GREEN_C),
        sigma4.animate.set_color(GREEN_C),
        TransformMatchingTex(eqfin1,eqfin2,transform_mismatches=True), 
        Write(l3),Write(l4), Create(area2), rate_func=linear)

        self.wait(1)
        self.play(Uncreate(l3), Uncreate(l4), Uncreate(area2))

        self.play(sigma3.animate.set_color(WHITE),
        sigma4.animate.set_color(WHITE),
        sigma5.animate.set_color(RED_C),
        sigma6.animate.set_color(RED_C),
        TransformMatchingTex(eqfin2,eqfin3,transform_mismatches=True),Create(l5),Create(l6),Create(area3), rate_func=linear)
        self.wait()

        eqfin.set_color(WHITE)
        self.play(FadeOut(l5),FadeOut(l6),FadeOut(area3), FadeOut(textf4), FadeOut(vg))
        self.play(TransformMatchingTex(eqfin3,eqfin,transform_mismatches=True))
        self.play(eqfin.animate.shift(UP*3))
        sr2 = SurroundingRectangle(eqfin).set_color_by_gradient([BLUE_C,GREEN_C])
        self.play(Write(sr2), eqfin.animate.set_color_by_gradient([BLUE_C,GREEN_C]))
        self.wait()


        ax2 = Axes(
            x_range = [0, 3, 1],
            y_range = [0, 1, 0.5],
            x_length = 3,
            y_length = 1,
            tips=False,
            axis_config = {'include_numbers':False}
        )

        erf1 = ax2.plot(lambda x: erf(x), x_range=[0,3])
        erf1.set_color_by_gradient([YELLOW,GREEN,BLUE])

        erfg = VGroup(erf1,ax2).scale(2)

        t = ValueTracker(0)

        md = Dot(ax2.coords_to_point(0,0)).scale(0.7).set_color(ORANGE)
        md.add_updater(lambda x: x.move_to(ax2.c2p(t.get_value(), erf(t.get_value()))))

        xt = Tex(r"$\sigma$ = x = ").move_to(DOWN*2).scale(0.7)
        xt.shift(LEFT*2)
        xt_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=5)
            .set_value(t.get_value())
            .next_to(xt, RIGHT, buff=0.1)
            .scale(0.7)
        )

        yt = Tex(r"y = ").move_to(DOWN*2).scale(0.7)
        yt.shift(RIGHT*2)
        yt_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=5)
            .set_value(erf(t.get_value()))
            .next_to(yt, RIGHT, buff=0.1)
            .scale(0.7)
        )

        sef = MathTex(r'\text{erf(}\frac{\sigma}{\sqrt{2}}\text{)} = ').move_to(DOWN*3).set_color(WHITE)
        
        sef_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=5)
            .set_value(erf(t.get_value()/sqrt(2)))
            .next_to(sef, RIGHT, buff=0.1)
            .scale(0.7)
        )
        
        sefG = VGroup(sef, sef_value_text)
        ss = always_redraw(lambda: SurroundingRectangle(sefG).set_color(ORANGE))

        tef = Tex(r"To sum up, let's just have a quick look at the ",r"Gaussian error function",r":", font_size=30).move_to(UP*2.5)
        tef[1].set_color_by_gradient([YELLOW,GREEN,BLUE])
        self.play(Write(tef))
        self.play(Uncreate(sr2), FadeOut(eqfin))
        self.play(Write(ax2), Write(erf1), Write(md), Write(xt), Write(yt), Write(xt_value_text), Write(yt_value_text), Write(sef), Write(sef_value_text))

        self.wait()

        self.play(t.animate.set_value(1))
        self.play(Write(ss))
        self.wait()
        self.play(Uncreate(ss))
  
        self.play(t.animate.set_value(2))
        self.play(Write(ss))
        self.wait()
        self.play(Uncreate(ss))

        self.play(t.animate.set_value(3))
        self.play(Write(ss))
        self.wait()
        self.play(Uncreate(ss),Unwrite(tef), Uncreate(ax2), Uncreate(erf1), Uncreate(md), Unwrite(xt), Unwrite(yt), FadeOut(xt_value_text), FadeOut(yt_value_text), Uncreate(sef), FadeOut(sef_value_text))
       
        sq = Square(side_length=1, color=WHITE, fill_opacity=0.5).move_to(DOWN*0.3).scale(0.25)
        sq.shift(RIGHT).set_color_by_gradient([PURPLE_C,WHITE])
        qed = Tex(r'Q.E.D.').set_color_by_gradient([PURPLE_C,WHITE])
        self.play(Write(qed), Create(sq))
        self.wait(2)

        self.play(Uncreate(sq), Unwrite(qed))
        self.wait(3)

def PDF_normal(x, mu, sigma,k):
    return exp(-(((k*x)-mu)**2)/(2*sigma**2))/(sigma*sqrt(2*pi))