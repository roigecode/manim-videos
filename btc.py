from math import *
from os import write
from manim import *
from numpy import array, flatiter, left_shift


class MainFunction(MovingCameraScene):
    def construct(self):
        # +-------------+ #
        # | SHORT CALL: | #
        # +-------------+ #

        fs = 17

        lct = Tex(r"Short Call (January 21, 2022 \$480.00 SPY)").set_color(WHITE)
        src = SurroundingRectangle(lct).set_color_by_gradient([
        ORANGE, PINK, PURPLE])
        self.play(Write(lct))
        self.play(Create(src))
        self.wait()
        self.play(Uncreate(src), lct.animate.set_color_by_gradient(
        [ORANGE, PINK, PURPLE]))
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
        y2 = MathTex(r"360\$", font_size=20).move_to(
        ax2.c2p(405, 360)).set_color_by_gradient([PURE_GREEN, GREEN])
        y2.shift(LEFT*0.6)
        ly1 = Line(ax2.c2p(425, 0), ax2.c2p(427, 0),
               stroke_width=0.9).move_to(ax2.c2p(405, 360))

        x_vals = [405, 480, 535]
        y_vals = [360, 360, -5140]
        graph = ax2.plot_line_graph(x_values=x_vals, y_values=y_vals,
                                add_vertex_dots=False, stroke_width=0.9).set_color(WHITE)

        line_1 = DashedLine(ax2.c2p(480, 360), ax2.c2p(
        480, 0), color=WHITE, stroke_width=0.9)
        arrow1 = Arrow(ax2.c2p(480, -4000), ax2.c2p(480, -250), buff=0.3,
                   stroke_width=2, max_tip_length_to_length_ratio=0.06)
        bc = Tex(r"-1 Call@480", font_size=25).move_to(ax2.c2p(480, -4000))

        price = Tex(r"360\$", font_size=20).move_to(
        ax2.c2p(405, 360)).set_color_by_gradient([PURE_GREEN, GREEN])
        price.shift(LEFT*0.6)

        price2 = MathTex(r'"-\infty \$"', font_size=20).move_to(ax2.c2p(405, -5135)
                                                            ).set_color_by_gradient([PURE_RED, RED])
        price2.shift(LEFT*0.6)
        ly2 = Line(ax.c2p(425, 0), ax.c2p(427, 0),
               stroke_width=0.9).move_to(ax.c2p(405, -5135))

        areatot1 = Polygram([ax2.c2p(405, 0), ax2.c2p(405, 360), ax2.c2p(480, 360), ax2.c2p(
        483.6, 0)], stroke_opacity=0, fill_color=PURE_RED, fill_opacity=0.5)
        areatot2 = Polygram([ax2.c2p(483.5, 0), ax2.c2p(535, 0), ax2.c2p(
        535, -5140)], stroke_opacity=0, fill_color=PURE_GREEN, fill_opacity=0.5)

        areatot1.set_color_by_gradient([PURE_GREEN, BLUE])
        areatot2.set_color_by_gradient([PINK, PURE_RED])

        # PDF:
        pdf = ax2.plot(lambda x: PDF_sc(x)).set_color(PINK)
        pdf_text = Tex(r"37d", font_size=15).set_color(
        PINK).move_to(ax2.c2p(483.6, 800))

    # Plotting the Standar Deviations (1st & 2nd):
    # 1SD: 440 // 500
        sd11 = DashedLine(ax2.c2p(440, -5140), ax2.c2p(440, 1000),
                      dash_length=0.075).set_color(PINK)
        sd12 = DashedLine(ax2.c2p(500, -5140), ax2.c2p(500, 1000),
                      dash_length=0.075).set_color(PINK)

        sd11_text = MathTex(
        r"-1\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(440, -5250))
        sd12_text = MathTex(r"1\sigma", font_size=fs).set_color(
        PINK).move_to(ax2.c2p(500, -5250))

    # 2SD: 410 // 530
        sd21 = DashedLine(ax2.c2p(410, -5140), ax2.c2p(410, 1000),
                      stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)
        sd22 = DashedLine(ax2.c2p(530, -5140), ax2.c2p(530, 1000),
                      stroke_width=0.9, dashed_ratio=0.4).set_color(PINK)

        sd21_text = MathTex(
        r"-2\sigma", font_size=fs).set_color(PINK).move_to(ax2.c2p(410, -5250))
        sd22_text = MathTex(r"2\sigma", font_size=fs).set_color(
        PINK).move_to(ax2.c2p(530, -5250))
    #profdot = Dot(ax.c2p(405, sigm(405)), radius=0.055).set_color(WHITE)

    # SHORT CALL PLAYS:
        self.play(Write(ax2), Write(labels), Write(line_1), Write(ly2),
              Create(areatot1), Create(areatot2), Write(ly1), Write(graph))
        self.wait(0.5)
        self.play(Write(bc), Write(arrow1), Write(price),
              Write(price2), Rotate(ly1, PI), Rotate(ly2, PI))
        self.wait(2)
        self.play(Write(pdf), Write(pdf_text), Write(sd11), Write(sd12), Write(sd11_text), Write(
        sd12_text), Write(sd21), Write(sd22), Write(sd21_text), Write(sd22_text))
        self.wait(3)
        self.play(FadeOut(ax2), FadeOut(price), FadeOut(ly2), FadeOut(price2), FadeOut(labels), FadeOut(line_1), FadeOut(areatot1), FadeOut(areatot2), FadeOut(ly1), FadeOut(graph), FadeOut(bc), FadeOut(
        arrow1), FadeOut(pdf), FadeOut(pdf_text), FadeOut(sd11), FadeOut(sd12), FadeOut(sd11_text), FadeOut(sd12_text), FadeOut(sd21), FadeOut(sd22), FadeOut(sd21_text), FadeOut(sd22_text))
        self.wait(2)
