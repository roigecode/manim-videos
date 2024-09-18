from manim import *

UNISWAP_PINK = ManimColor('#FE0079')

class MainFunction(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # +---------------+
        # | UNISWAP INTRO |
        # +---------------+
        unilogo = SVGMobject("uni-logo.svg").scale(1.75)
        self.play(Write(unilogo))
        self.wait(1)

        plotlim = 5
        ax = Axes(
            x_range=(0, plotlim, 1),
            y_range=(0, plotlim, 1),
            x_length=plotlim,
            y_length=plotlim,
            tips=False,
            axis_config={"include_numbers": False},
            x_axis_config={"include_ticks" : False},
            y_axis_config={"include_ticks" : False},
        )
        xreserves = Tex("X reserves", color=WHITE).move_to(ax.c2p(plotlim/2,0)).shift(DOWN*0.5)
        yreserves = Tex("Y reserves", color=WHITE).rotate(PI/2).move_to(ax.c2p(0,plotlim/2)).shift(LEFT*0.5)

        reserves = VGroup(xreserves, yreserves)

        curve = ax.plot(
            lambda x: 1 /x,
            x_range=[0.2, plotlim],
            use_smoothing=True,
            color=UNISWAP_PINK
        )

        equation = MathTex("x\\cdot y = k", color=UNISWAP_PINK)\
            .move_to(ax.c2p(plotlim*0.65, plotlim*0.6))

        vg1 = VGroup(curve, equation)
        
        x = ValueTracker(1)
        d1 = always_redraw(lambda: Dot(radius=0.125).set_color(BLUE_C).move_to(ax.c2p(x.get_value(), 1/x.get_value())))
        x_label = MathTex("x").add_updater(lambda m: m.next_to(ax.c2p(x.get_value(), 0), DOWN))

        chart_vg = VGroup(ax, vg1, reserves, unilogo, d1)

        self.play(Write(ax), Write(reserves))
        self.play(Transform(unilogo, vg1), run_time=0.75)
        self.wait()

        self.play(self.camera.frame.animate.scale(0.5).move_to(ax.c2p(1, 1.5)))
        self.play(Write(d1))
        self.wait()

        self.play(x.animate.set_value(0.35), rate_func=rate_functions.ease_in_out_cubic, run_time=1.25)
        self.play(x.animate.set_value(3.5), rate_func=rate_functions.ease_in_out_cubic, run_time=1.25)
        self.play(x.animate.set_value(1), rate_func=rate_functions.ease_in_out_cubic, run_time=1.25)
        self.wait()  

        self.play(Restore(self.camera.frame), chart_vg.animate.move_to(ORIGIN))
        self.play(chart_vg.animate.shift(LEFT*3))
        self.wait()

        # +-------------------+
        # | NUMERICAL EXAMPLE |
        # +-------------------+
        dx_buy_dy_1 = MathTex("(x+dx)\\cdot(y-dy) = k").move_to(RIGHT*4 + UP*3).scale(0.75)
        dx_buy_dy_2 = MathTex("xy-xdy+ydx-dxdy = k").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*0.5 + LEFT*0.4)
        dx_buy_dy_3 = MathTex("xy+ydx-xdy-dxdy=k").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*1 + LEFT*0.4)
        dx_buy_dy_4 = MathTex("y(x+dx)-dy(x+dx)=k").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*1.5 + LEFT*0.4)
        dx_buy_dy_5 = MathTex("y(x+dx) = k + dy(x+dx)").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*2 + LEFT*0.4)
        dx_buy_dy_6 = MathTex("y(x+dx) - k = dy(x+dx)").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*2.5 + LEFT*0.4)
        dx_buy_dy_7 = MathTex("dy = y - \\frac{xy}{x+dx}").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*3.3)
        dx_buy_dy_8 = MathTex("dy = y\\cdot\\underbrace{\\left(\\frac{x+dx}{x+dx}\\right)}_{1} - \\frac{xy}{x+dx}").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*4.7 + LEFT*0.6)
        dx_buy_dy_9 = MathTex("dy = \\frac{yx+ydx-xy}{x+dx}").scale(0.75).move_to(dx_buy_dy_1).shift(DOWN*6.1)
        
        dx_buy_dy_10 = MathTex("dy=\\frac{ydx}{x+dx}").scale(0.75).move_to(dx_buy_dy_1).shift(DOWN*2.25)
        sr_10 = SurroundingRectangle(dx_buy_dy_10, color=UNISWAP_PINK, buff=0.15)

        dx_buy_dy_11 = MathTex("dy=\\frac{y\cdot dx(1-\phi)}{x+dx(1-\phi)}").scale(0.75).move_to(dx_buy_dy_1).shift(DOWN*3.75)
        sr_11 = SurroundingRectangle(dx_buy_dy_11, color=UNISWAP_PINK, buff=0.15)

        self.play(TransformFromCopy(equation, dx_buy_dy_1))
        self.play(TransformFromCopy(dx_buy_dy_1, dx_buy_dy_2))
        self.play(TransformFromCopy(dx_buy_dy_2, dx_buy_dy_3))
        self.play(TransformFromCopy(dx_buy_dy_3, dx_buy_dy_4))
        self.play(TransformFromCopy(dx_buy_dy_4, dx_buy_dy_5))
        self.play(TransformFromCopy(dx_buy_dy_5, dx_buy_dy_6))
        self.play(TransformFromCopy(dx_buy_dy_6, dx_buy_dy_7))
        self.play(TransformFromCopy(dx_buy_dy_7, dx_buy_dy_8))
        self.play(TransformFromCopy(dx_buy_dy_8, dx_buy_dy_9), run_time=1.5)
        self.wait()
        self.play(FadeOut(dx_buy_dy_2), FadeOut(dx_buy_dy_3), FadeOut(dx_buy_dy_4), FadeOut(dx_buy_dy_5), FadeOut(dx_buy_dy_6), FadeOut(dx_buy_dy_7), FadeOut(dx_buy_dy_8),\
                dx_buy_dy_9.animate.shift(UP*5.1)\
        )
        self.play(TransformFromCopy(dx_buy_dy_9, dx_buy_dy_10))
        self.play(Write(sr_10))
        self.play(TransformFromCopy(dx_buy_dy_10, dx_buy_dy_11))
        self.play(Transform(sr_10, sr_11))
        self.wait()

        self.play(FadeOut(dx_buy_dy_9), FadeOut(dx_buy_dy_10), FadeOut(dx_buy_dy_1), dx_buy_dy_11.animate.shift(UP*3.5), sr_10.animate.shift(UP*3.55))
        self.wait()

        self.play(Unwrite(xreserves), Unwrite(yreserves), chart_vg.animate.move_to(ORIGIN).scale(1.5))

        self.wait(2)