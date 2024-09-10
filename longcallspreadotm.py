
from manim import *
from math import sqrt, exp, pi, erf
from manim.mobject.mobject import T
from manim.utils import scale
import csv
import numpy as np


class MainFunction(MovingCameraScene):
    def construct(self):
        title(self)
        self.wait()
        longcallandshortcall(self)
        self.wait()
        longcallspread(self)
        self.wait(2)
        sq = Square(side_length=1, color=WHITE, fill_opacity=0.5).move_to(DOWN*0.3).scale(0.25)
        sq.shift(RIGHT).set_color_by_gradient([PURPLE_C,WHITE])

        ex = Tex(r"Let's see how to set a ",r" Long Call Spread",r" in a real brokerage account:", font_size=35)
        ex[1].set_color_by_gradient([ORANGE,PINK,PURPLE])
        self.play(Write(ex))
        self.wait()
        self.play(Unwrite(ex))
        self.wait()

        qed = Tex(r'Q.E.D.').set_color_by_gradient([PURPLE_C,WHITE])
        self.play(Write(qed), Create(sq))
        self.wait(2)

        self.play(Uncreate(sq), Unwrite(qed))
        self.wait(5)


# +--------+ #
# | TITLE: | #
# +--------+ #

def title(self):
    title = Tex(r"What is a",r" Long (Bull/Debit) Call Vertical Spread?")
    title[1].set_color_by_gradient([ORANGE,PINK,PURPLE])
    
    t1 = Tex(r"A Call option is a financial contract that gives its",r" buyer (holder) ",r"the", r" \underline{right} to buy  ", r" the underlying security at a specified price within a specific time period. Alternatively, it gives its", r" seller (writer) ",r"the ",r"\underline{obligation} to sell",r" the security at a specified price at expiration.", font_size=35)

    t1[1].set_color_by_gradient([GREEN_C,BLUE_C])
    t1[3].set_color_by_gradient([GREEN_C,BLUE_C])
    t1[5].set_color_by_gradient([ORANGE,RED_C])
    t1[7].set_color_by_gradient([ORANGE,RED_C])

    lc = Tex(r"Let's see an example for a ",r" bought (long) Call", r" and one \\ for a ", r" sold (short) Call")
    lc[1].set_color_by_gradient([GREEN_C,BLUE_C])
    lc[3].set_color_by_gradient([ORANGE,RED_C])

    sr = SurroundingRectangle(title[1]).set_color_by_gradient([ORANGE,PINK,PURPLE])
    # PLAYS:
    self.play(Write(title))
    self.wait()
    self.play(Write(sr))
    self.wait()
    self.play(Unwrite(title), Uncreate(sr))
    self.wait()
    self.play(Write(t1))
    self.wait(10)
    self.play(Unwrite(t1))
    self.wait()
    self.play(Write(lc))
    self.wait(2)
    self.play(Unwrite(lc))


# +------------------------+ #
# | LONG CALL & SHORT CALL | #
# +------------------------+ #

def longcallandshortcall(self):
    # +------------+ #
    # | LONG CALL: | #
    # +------------+ #
    
    lct = Tex(r"Long Call (January 21, 2022 \$465.00 SPY)").set_color(WHITE)
    src = SurroundingRectangle(lct).set_color_by_gradient([GREEN_C, BLUE_C])
    self.play(Write(lct))
    self.play(Create(src))
    self.wait()
    self.play(Uncreate(src), lct.animate.set_color_by_gradient([GREEN_C, BLUE_C]))
    self.wait()
    self.play(Unwrite(lct))
    self.wait(0.5)

    fs = 17
    e = 2.71828182846

    ax = Axes(
        x_range=[405, 535, 5],
        y_range=[-1000, 8964, 10000],
        tips=False,
        x_axis_config={"include_numbers": True, "font_size": fs},
        y_axis_config={"include_numbers": False, "font_size": fs}
    )

    labels = ax.get_y_axis_label(Tex(r"P\&L [\$]", font_size=20))
    y2 = MathTex(r"-847\$", font_size=20).move_to(ax.c2p(405, -847))
    y2.set_color_by_gradient([PURE_RED,RED])
    y2.shift(LEFT*0.6)
    ly1 = Line(ax.c2p(425, 0), ax.c2p(427, 0), stroke_width=0.9).move_to(ax.c2p(405, -847))

    x_vals = [405, 465, 535]
    y_vals = [-847, -847, 8964]
    graph = ax.plot_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False, stroke_width=0.9).set_color(WHITE)

    line_1 = DashedLine(ax.c2p(465,-847), ax.c2p(465,0), color=WHITE, stroke_width=0.9)
    arrow1 = Arrow(ax.c2p(465, 5000), ax.c2p(465, 0), buff=0.3, stroke_width=2, max_tip_length_to_length_ratio=0.06)
    bc = Tex(r"+1 Call@465", font_size=25).move_to(ax.c2p(465, 5000))

    price = Tex(r"-847\$", font_size=20).move_to(ax.c2p(405,-847)).set_color_by_gradient([PURE_RED,RED])
    price.shift(LEFT*0.6)

    price2 = MathTex(r'+\infty \$', font_size=20).move_to(ax.c2p(405,8961)).set_color_by_gradient([PURE_GREEN,GREEN])
    price2.shift(LEFT*0.6)
    ly2 = Line(ax.c2p(425, 0), ax.c2p(427, 0), stroke_width=0.9).move_to(ax.c2p(405, -8961))

    # POLYGRAMS: Shade P&L areas:
    areatot1 = Polygram([ax.c2p(405, 0), ax.c2p(405, -847), ax.c2p(465, -847), ax.c2p(471, 0)], stroke_opacity=0, fill_color=PURE_RED, fill_opacity=0.5)
    areatot2 = Polygram([ax.c2p(471, 0), ax.c2p(535, 0), ax.c2p(535, 8964)], stroke_opacity=0, fill_color=PURE_GREEN, fill_opacity=0.5)
    
    areatot1.set_color_by_gradient([PURE_RED, PINK])
    areatot2.set_color_by_gradient([BLUE, PURE_GREEN])

    # PDF:
    pdf = ax.plot(lambda x: PDF_lc(x)).set_color(PINK)
    pdf_text = Tex(r"37d",font_size=15).set_color(PINK).move_to(ax.c2p(473.5,9250))
    
    # Plotting the Standar Deviations (1st & 2nd):
    # 1SD: 440 // 500
    sd11 = DashedLine(ax.c2p(440,-1100), ax.c2p(440,9000), dash_length=0.075).set_color(PINK)
    sd12 = DashedLine(ax.c2p(500,-1100), ax.c2p(500,9000), dash_length=0.075).set_color(PINK)

    sd11_text = MathTex(r"-1\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(440,-1200))
    sd12_text = MathTex(r"1\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(500,-1200))

    # 2SD: 410 // 530
    sd21 = DashedLine(ax.c2p(410,-1000), ax.c2p(410,9000), stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)
    sd22 = DashedLine(ax.c2p(530,-1000), ax.c2p(530,9000), stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)

    sd21_text = MathTex(r"-2\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(410,-1200))
    sd22_text = MathTex(r"2\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(530,-1200)) 
    #profdot = Dot(ax.c2p(405, sigm(405)), radius=0.055).set_color(WHITE)

    # LONG CALL PLAYS:
    self.play(Write(ax),Write(labels),Write(line_1), Create(areatot1), Create(areatot2), Write(ly1), Write(ly2),Write(graph))
    self.wait(0.5)
    self.play(Write(bc), Write(arrow1),Write(price),Write(price2),Rotate(ly1, PI), Rotate(ly2,PI))
    self.wait(2)
    self.play(Write(pdf),Write(pdf_text),Write(sd11),Write(sd12),Write(sd11_text),Write(sd12_text),Write(sd21),Write(sd22),Write(sd21_text),Write(sd22_text))
    self.wait(3)
    self.play(FadeOut(ax),FadeOut(price),FadeOut(price2),FadeOut(ly2),FadeOut(labels),FadeOut(line_1),FadeOut(areatot1),FadeOut(areatot2),FadeOut(ly1),FadeOut(graph),FadeOut(bc),FadeOut(arrow1), FadeOut(pdf),FadeOut(pdf_text),FadeOut(sd11),FadeOut(sd12),FadeOut(sd11_text),FadeOut(sd12_text),FadeOut(sd21),FadeOut(sd22),FadeOut(sd21_text),FadeOut(sd22_text))

    groupLongCall = VGroup(ax,ly2,labels,y2,ly1,graph,arrow1,bc,price,areatot1,areatot2,pdf,sd11,sd12,sd11_text,sd12_text,sd21,sd22,sd21_text,sd22_text,price2).scale(0.7)

    # +-------------+ #
    # | SHORT CALL: | #
    # +-------------+ #
    
    lct = Tex(r"Short Call (January 21, 2022 \$480.00 SPY)").set_color(WHITE)
    src = SurroundingRectangle(lct).set_color_by_gradient([ORANGE,PINK,PURPLE])
    self.play(Write(lct))
    self.play(Create(src))
    self.wait()
    self.play(Uncreate(src), lct.animate.set_color_by_gradient([ORANGE,PINK,PURPLE]))
    self.wait()
    self.play(Unwrite(lct))
    self.wait(0.5)

    ax2 = Axes(
        x_range=[405, 535, 5],
        y_range=[-5140, 1000, 10000],
        tips=False,
        x_axis_config={"include_numbers": True, "font_size": fs},
        y_axis_config={"include_numbers": False, "font_size": fs}
    )

    labels = ax2.get_y_axis_label(Tex(r"P\&L [\$]", font_size=20))
    y2 = MathTex(r"360\$", font_size=20).move_to(ax2.c2p(405, 360)).set_color_by_gradient([PURE_GREEN,GREEN])
    y2.shift(LEFT*0.6)
    ly1 = Line(ax2.c2p(425, 0), ax2.c2p(427, 0), stroke_width=0.9).move_to(ax2.c2p(405, 360))

    x_vals = [405, 480, 535]
    y_vals = [360, 360, -5140]
    graph = ax2.plot_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False, stroke_width=0.9).set_color(WHITE)

    line_1 = DashedLine(ax2.c2p(480,360), ax2.c2p(480,0), color=WHITE, stroke_width=0.9)
    arrow1 = Arrow(ax2.c2p(480, -4000), ax2.c2p(480, -250), buff=0.3, stroke_width=2, max_tip_length_to_length_ratio=0.06)
    bc = Tex(r"-1 Call@480", font_size=25).move_to(ax2.c2p(480, -4000))

    price = Tex(r"360\$", font_size=20).move_to(ax2.c2p(405,360)).set_color_by_gradient([PURE_GREEN,GREEN])
    price.shift(LEFT*0.6)

    price2 = MathTex(r'"-\infty \$"', font_size=20).move_to(ax2.c2p(405,-5135)).set_color_by_gradient([PURE_RED,RED])
    price2.shift(LEFT*0.6)
    ly2 = Line(ax.c2p(425, 0), ax.c2p(427, 0), stroke_width=0.9).move_to(ax.c2p(405, -5135))

    areatot1 = Polygram([ax2.c2p(405, 0), ax2.c2p(405, 360), ax2.c2p(480, 360), ax2.c2p(483.6, 0)], stroke_opacity=0, fill_color=PURE_RED, fill_opacity=0.5)
    areatot2 = Polygram([ax2.c2p(483.5, 0), ax2.c2p(535, 0), ax2.c2p(535, -5140)], stroke_opacity=0, fill_color=PURE_GREEN, fill_opacity=0.5)
    
    areatot1.set_color_by_gradient([PURE_GREEN,BLUE])
    areatot2.set_color_by_gradient([PINK, PURE_RED])

    # PDF:
    pdf = ax2.plot(lambda x: PDF_sc(x)).set_color(PINK)
    pdf_text = Tex(r"37d",font_size=15).set_color(PINK).move_to(ax2.c2p(483.6,800))
    
    # Plotting the Standar Deviations (1st & 2nd):
    # 1SD: 440 // 500
    sd11 = DashedLine(ax2.c2p(440,-5140), ax2.c2p(440,1000), dash_length=0.075).set_color(PINK)
    sd12 = DashedLine(ax2.c2p(500,-5140), ax2.c2p(500,1000), dash_length=0.075).set_color(PINK)

    sd11_text = MathTex(r"-1\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(440,-5250))
    sd12_text = MathTex(r"1\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(500,-5250))

    # 2SD: 410 // 530
    sd21 = DashedLine(ax2.c2p(410,-5140), ax2.c2p(410,1000), stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)
    sd22 = DashedLine(ax2.c2p(530,-5140), ax2.c2p(530,1000), stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)

    sd21_text = MathTex(r"-2\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(410,-5250))
    sd22_text = MathTex(r"2\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(530,-5250)) 
    #profdot = Dot(ax.c2p(405, sigm(405)), radius=0.055).set_color(WHITE)
    
    # SHORT CALL PLAYS:
    self.play(Write(ax2),Write(labels),Write(line_1), Write(ly2), Create(areatot1), Create(areatot2), Write(ly1),Write(graph))
    self.wait(0.5)
    self.play(Write(bc), Write(arrow1), Write(price), Write(price2),Rotate(ly1, PI), Rotate(ly2,PI))
    self.wait(2)
    self.play(Write(pdf),Write(pdf_text),Write(sd11),Write(sd12),Write(sd11_text),Write(sd12_text),Write(sd21),Write(sd22),Write(sd21_text),Write(sd22_text))
    self.wait(3)
    self.play(FadeOut(ax2),FadeOut(price),FadeOut(ly2),FadeOut(price2),FadeOut(labels),FadeOut(line_1),FadeOut(areatot1),FadeOut(areatot2),FadeOut(ly1),FadeOut(graph),FadeOut(bc),FadeOut(arrow1), FadeOut(pdf),FadeOut(pdf_text),FadeOut(sd11),FadeOut(sd12),FadeOut(sd11_text),FadeOut(sd12_text),FadeOut(sd21),FadeOut(sd22),FadeOut(sd21_text),FadeOut(sd22_text))
    self.wait(2)

    comb = Tex(r"Now let's combine both strategies to get the ",r"Long Call Vertical Spread",r"!", font_size=30)
    comb[1].set_color_by_gradient([ORANGE,PINK,PURPLE])
    self.play(Write(comb))
    self.wait(2)
    self.play(comb.animate.shift(UP*3))
    self.wait()

    groupShortCall = VGroup(ly2,ax2,labels,y2,ly1,graph,arrow1,bc,price,areatot1,areatot2,pdf,sd11,sd12,sd11_text,sd12_text,sd21,sd22,sd21_text,sd22_text, price2).scale(0.7)

    sumsi = MathTex(r"+",font_size=100)
    
    self.play(FadeIn(groupLongCall))
    self.play(groupLongCall.animate.scale(0.5))
    self.play(groupLongCall.animate.shift(LEFT*3))
    self.play(FadeIn(groupShortCall))
    self.play(groupShortCall.animate.scale(0.5))
    self.play(groupShortCall.animate.shift(RIGHT*3.75))
    self.play(Write(sumsi))

    self.wait(2)

    self.play(FadeOut(groupLongCall), Unwrite(sumsi), FadeOut(groupShortCall), Unwrite(comb))

# +------------------+ #
# | LONG CALL SPREAD | #
# +------------------+ #

def longcallspread(self):
    # FONT-SIZE FOR AXES:
    fs = 17
    e = 2.71828182846

    ax = Axes(
        x_range=[405, 535, 5],
        y_range=[-1000, 900, 10000],
        tips=False,
        x_axis_config={"include_numbers": True, "font_size": fs},
        y_axis_config={"include_numbers": False, "font_size": fs}
    )

    labels = ax.get_y_axis_label(Tex(r"P\&L [\$]", font_size=20))

    y1 = MathTex(r"653\$", font_size=fs).move_to(ax.c2p(405, 653)).set_color_by_gradient([PURE_GREEN,GREEN])
    y2 = MathTex(r"-847\$", font_size=fs).move_to(ax.c2p(405, -847)).set_color_by_gradient([PURE_RED,RED])
    y1.shift(LEFT*0.6)
    y2.shift(LEFT*0.6)

    ly1 = Line(ax.c2p(425, 0), ax.c2p(427, 0), stroke_width=0.9).move_to(ax.c2p(405, 653))
    ly2 = Line(ax.c2p(425, 0), ax.c2p(427, 0), stroke_width=0.9).move_to(ax.c2p(405, -847))

    BE = 473.5

    # Plot the Long Call Spread:
    x_vals = [405, 465, 473.5, 480, 535]
    y_vals = [-847, -847, 0, 653, 653]
    graph = ax.plot_line_graph(x_values=x_vals, y_values=y_vals, add_vertex_dots=False, stroke_width=0.9).set_color(WHITE)

    # POLYGRAMS: Shade the areas in their respective color:
    areatot1 = Polygram([ax.c2p(405, 0), ax.c2p(405, -847), ax.c2p(465, -847), ax.c2p(473.5, 0)], stroke_opacity=0, fill_color=PURE_RED, fill_opacity=0.5)
    areatot2 = Polygram([ax.c2p(473.5, 0), ax.c2p(535, 0), ax.c2p(535, 653), ax.c2p(480, 653)], stroke_opacity=0, fill_color=PURE_GREEN, fill_opacity=0.5)

    areatot1.set_color_by_gradient([PURE_RED, PINK])
    areatot2.set_color_by_gradient([BLUE, PURE_GREEN])

    # Strike prices lines:
    line_1 = DashedLine(ax.coords_to_point(465, 0), ax.c2p(465, -847), stroke_width=0.9)
    line_2 = DashedLine(ax.c2p(480, 0), ax.c2p(480, 653), stroke_width=0.9)

    # Options Text:
    longcall = Tex(r"+1 Call@465", font_size=20).move_to(ax.c2p(465, 653))
    shortput = Tex(r"-1 Call@480", font_size=20).move_to(ax.c2p(480, -847))
    ar1 = Arrow(ax.c2p(465, 653), ax.c2p(465, 0), buff=0.2, stroke_width=2, max_tip_length_to_length_ratio=0.1)
    ar2 = Arrow(ax.c2p(480, -847), ax.c2p(480, -100), buff=0.2, stroke_width=2, max_tip_length_to_length_ratio=0.1)

    # Sigmoid and PDF function:
    def sigm(x):
        return (1500/(1+e**(-0.1*x+47.35)))-847

    sigmoid = ax.plot(lambda x : (1500/(1+e**(-0.1*x+47.35)))-847).set_color(ORANGE)
    pdf = ax.plot(lambda x: PDF_cs(x)).set_color(PINK)
    pdf_text = Tex(r"37d",font_size=15).set_color(PINK).move_to(ax.c2p(473.5,1000))
    
    # Plotting the Standar Deviations (1st & 2nd):
    # 1SD: 440 // 500
    sd11 = DashedLine(ax.c2p(440,-1000), ax.c2p(440,900), dash_length=0.05).set_color(PINK)
    sd12 = DashedLine(ax.c2p(500,-1000), ax.c2p(500,900), dash_length=0.05).set_color(PINK)

    sd11_text = MathTex(r"-1\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(440,-1100))
    sd12_text = MathTex(r"1\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(500,-1100))

    # 2SD: 410 // 530
    sd21 = DashedLine(ax.c2p(410,-1000), ax.c2p(410,900), stroke_width=0.9, dashed_ratio=0.6).set_color(PINK)
    sd22 = DashedLine(ax.c2p(530,-1000), ax.c2p(530,900), stroke_width=0.9, dashed_ratio=0.6).set_color(PINK)

    sd21_text = MathTex(r"-2\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(410,-1100))
    sd22_text = MathTex(r"2\sigma", font_size=fs).set_color(PINK).move_to(ax.c2p(530,-1100)) 
    profdot = Dot(ax.c2p(405, sigm(405)), radius=0.055).set_color(WHITE)

    # PLAYS:
    self.play(Write(ax), Create(areatot1), Create(areatot2), Create(graph), Write(labels), Write(y1), Write(y2))
    self.play(Write(ly1), Write(ly2))
    self.play(Rotate(ly1, PI), Rotate(ly2, PI), Create(line_1), Create(line_2))
    self.play(Write(longcall), Write(ar1), Write(ar2), Write(shortput))
    self.wait()
    self.play(Write(sigmoid), Write(pdf), Write(pdf_text))
    self.play(FadeOut(line_1), FadeOut(line_2), Write(sd11),Write(sd12),Write(sd21),Write(sd22),Write(sd11_text),Write(sd12_text),Write(sd21_text),Write(sd22_text))
    self.wait(0.5)
    self.play(Write(profdot))
    self.play(MoveAlongPath(profdot, sigmoid, rate_func=rate_functions.smooth), run_time=3)

    self.wait(3)

    self.play(FadeOut(ax),FadeOut(areatot1),FadeOut(areatot2),FadeOut(graph),FadeOut(labels),FadeOut(y1),FadeOut(y2),FadeOut(ly1),FadeOut(ly2),FadeOut(longcall),
    FadeOut(ar1),FadeOut(ar2),FadeOut(shortput),FadeOut(sigmoid),FadeOut(pdf),FadeOut(pdf_text),FadeOut(sd11),FadeOut(sd12),FadeOut(sd21),FadeOut(sd22),FadeOut(sd11_text),
    FadeOut(sd12_text),FadeOut(sd21_text),FadeOut(sd22_text),FadeOut(profdot))

    self.wait()

    text1 = Tex(r"\underline{Time for some maths!}")
    self.play(Write(text1))
    self.play(text1.animate.shift(UP*3))

    deb = MathTex(r"D \equiv \text{ Debit payed to enter the trade.}", font_size=30)
    strk = MathTex(r"S_i \equiv \text{ Strike Price 'i'.}", font_size=30)

    proff = MathTex(r"\text{Max. Proffit}",r" = \Delta S - D = (S_B - S_A) - D=(480-465)-6.53\$ = 8.74\$ \cdot 100 =",r" 847\$ ", font_size=30)
    proff[0].set_color_by_gradient([PURE_GREEN,GREEN])
    proff[2].set_color_by_gradient([PURE_GREEN,GREEN])

    loss = MathTex(r"\text{Max. Loss}",r" = D = -6.74\$ \cdot 100 = ",r" -647\$", font_size=30).move_to(DOWN*1.5)
    loss[0].set_color_by_gradient([PURE_RED,RED])
    loss[2].set_color_by_gradient([PURE_RED,RED])

    be = MathTex(r"\text{Break Even}",r" = S_A + D = 465 + 6.47\$ \approx",r" 471.5\$", font_size=30).move_to(DOWN*3)
    be[0].set_color_by_gradient([GREY,WHITE])
    be[2].set_color_by_gradient([GREY,WHITE])

    self.play(Write(deb))
    self.play(deb.animate.shift(UP*0.5))
    self.play(Write(strk))
    dsvg = VGroup(deb,strk)
    self.play(dsvg.animate.arrange(DOWN,buff=.2,aligned_edge=LEFT))

    self.play(dsvg.animate.shift(LEFT*3.25))
    self.play(dsvg.animate.shift(UP*1.5))

    self.play(Write(proff))
    self.play(Write(loss))
    self.play(Write(be))
    vgpl = VGroup(proff,loss,be)
    self.play(vgpl.animate.arrange(DOWN,buff=.2,aligned_edge=LEFT))

    srp = SurroundingRectangle(proff[2]).set_color_by_gradient([PURE_GREEN,GREEN])
    srl = SurroundingRectangle(loss[2]).set_color_by_gradient([PURE_RED,RED])
    srb = SurroundingRectangle(be[2]).set_color_by_gradient([GREY,WHITE])

    self.play(Create(srp))
    self.play(Create(srl))
    self.play(Create(srb))

    self.wait(4)

    self.play(Uncreate(srp), Uncreate(srl), Uncreate(srb))
    self.play(FadeOut(dsvg), FadeOut(vgpl), FadeOut(text1))

    greeks = Tex(r"\underline{And finally, the Greeks!}").set_color_by_gradient([YELLOW,GREEN_C])
    self.play(Write(greeks))
    self.play(greeks.animate.shift(UP*2))

    delta = ImageMobject("D:/manim/media/images/longcallspreadotm/bsd.jpg").move_to(LEFT*4)
    gamma = ImageMobject("D:/manim/media/images/longcallspreadotm/bsg.jpg")
    vega = ImageMobject("D:/manim/media/images/longcallspreadotm/bsv.jpg").move_to(RIGHT*4)

    self.play(FadeIn(delta))
    self.play(FadeIn(gamma))
    self.play(FadeIn(vega))

    iv = Tex(r"Implied Volatility (IV) is somewhat neutral as we are both long and short a Call.",font_size=17).move_to(DOWN*2)
    self.play(Write(iv))
    self.wait(5)
    self.play(FadeOut(delta), FadeOut(gamma), FadeOut(vega), Unwrite(greeks), Unwrite(iv))

def PDF_normal(x, mu, sigma,k):
    return exp(-(((k*x)-mu)**2)/(2*sigma**2))/(sigma*sqrt(2*pi))

def PDF_cs(x):
    return 900*sqrt(2*pi)*exp(-(((1*x)-473.5)**2)/(2*25**2))/(sqrt(2*pi))

def PDF_lc(x):
    return 9500*sqrt(2*pi)*exp(-(((1*x)-473.5)**2)/(2*25**2))/(sqrt(2*pi))

def PDF_sc(x):
    return 1200*sqrt(2*pi)*exp(-(((1*x)-483.6)**2)/(2*25**2))/(sqrt(2*pi))
