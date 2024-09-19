from manim import *

UNISWAP_PINK = ManimColor('#FE0079')
UNISWAP_GREEN = ManimColor('#00fe83')
UNISWAP_BLUE = ManimColor('#007bfe')
UNISWAP_ORANGE = ManimColor('#fe8300')
BG_COLOR = ManimColor('#0F0E17')

class MainFunction(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.camera.frame.save_state()

        # +---------------+
        # | UNISWAP INTRO |
        # +---------------+
        unilogo = SVGMobject("uni-logo.svg").scale(1.75)

        self.wait()
        self.play(Write(unilogo))
        self.wait()

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
            lambda x: 1/x,
            x_range=[0.2, plotlim],
            use_smoothing=True,
            color=UNISWAP_PINK
        )

        equation = MathTex("x\\cdot y = k", color=UNISWAP_PINK).move_to(ax.c2p(plotlim*0.65, plotlim*0.6))

        vg1 = VGroup(curve, equation)
        
        x = ValueTracker(1)
        
        d1 = always_redraw(lambda: Dot(radius=0.125).set_color(BLUE_C).move_to(ax.c2p(x.get_value(), 1/x.get_value())))
        chart_vg = VGroup(ax, vg1, reserves, unilogo, d1)

        self.play(Write(ax), Write(xreserves), Write(yreserves))
        self.play(Write(curve), Unwrite(unilogo), run_time=1.25)
        self.play(Write(equation))
        self.wait()

        self.play(self.camera.frame.animate.scale(0.5).move_to(ax.c2p(1, 1.5)))
        self.play(Write(d1))
        self.play(Flash(d1, color=BLUE_C, flash_radius=0.125+SMALL_BUFF))
        self.wait()

        self.play(x.animate.set_value(0.35), rate_func=rate_functions.ease_in_out_cubic, run_time=1.25)
        self.play(x.animate.set_value(3.5), rate_func=rate_functions.ease_in_out_cubic, run_time=1.25)
        self.play(x.animate.set_value(1), rate_func=rate_functions.ease_in_out_cubic, run_time=1.25)
        self.wait()  

        self.play(Restore(self.camera.frame), chart_vg.animate.move_to(ORIGIN).shift(LEFT*3))
        self.wait()

        # +-------------------+
        # | NUMERICAL EXAMPLE |
        # +-------------------+
        dx_buy_dy_1 = MathTex("(x+dx)\\cdot(y-dy)", "=", "k").move_to(RIGHT*4 + UP*3).scale(0.75)
        dx_buy_dy_2 = MathTex("xy-xdy+ydx-dxdy", "=", "k").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*0.5 + LEFT*0.4)
        dx_buy_dy_3 = MathTex("xy+ydx-xdy-dxdy", "=", "k").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*1 + LEFT*0.4)
        dx_buy_dy_4 = MathTex("y(x+dx)-dy(x+dx)", "=", "k").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*1.5 + LEFT*0.4)
        dx_buy_dy_5 = MathTex("y(x+dx)", "=", "k + dy(x+dx)").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*2 + LEFT*0.4)
        dx_buy_dy_6 = MathTex("y(x+dx) - k", "=", "dy(x+dx)").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*2.5 + LEFT*0.4)
        dx_buy_dy_7 = MathTex("dy", "=", "y - \\frac{xy}{x+dx}").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*3.3)
        dx_buy_dy_8 = MathTex("dy", "=", "y\\cdot\\underbrace{\\left(\\frac{x+dx}{x+dx}\\right)}_{1} - \\frac{xy}{x+dx}").move_to(dx_buy_dy_1).scale(0.75).shift(DOWN*4.7 + LEFT*0.6)
        dx_buy_dy_9 = MathTex("dy", "=", "\\frac{yx+ydx-xy}{x+dx}").scale(0.75).move_to(dx_buy_dy_1).shift(DOWN*6.1)
        
        dx_buy_dy_10 = MathTex("dy=\\frac{ydx}{x+dx}").scale(0.75).move_to(dx_buy_dy_1).shift(DOWN*2.25)
        sr_10 = SurroundingRectangle(dx_buy_dy_10, color=UNISWAP_PINK, buff=0.15)

        dx_buy_dy_11 = MathTex("dy","=","\\frac{y\cdot dx(1-\phi)}{x+dx(1-\phi)}").scale(0.75).move_to(dx_buy_dy_1).shift(DOWN*3.75)
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
        self.play(
            FadeOut(dx_buy_dy_2), 
            FadeOut(dx_buy_dy_3), 
            FadeOut(dx_buy_dy_4), 
            FadeOut(dx_buy_dy_5), 
            FadeOut(dx_buy_dy_6), 
            FadeOut(dx_buy_dy_7), 
            FadeOut(dx_buy_dy_8),
            dx_buy_dy_9.animate.shift(UP*5.1)
        )
        self.play(TransformFromCopy(dx_buy_dy_9, dx_buy_dy_10))
        self.play(Write(sr_10))
        self.play(TransformFromCopy(dx_buy_dy_10, dx_buy_dy_11))
        self.play(Transform(sr_10, sr_11))
        self.wait()

        self.play(
            FadeOut(dx_buy_dy_9), 
            FadeOut(dx_buy_dy_10), 
            FadeOut(dx_buy_dy_1), 
            dx_buy_dy_11.animate.shift(UP*3.5+RIGHT*0.75), 
            sr_10.animate.shift(UP*3.55+RIGHT*0.75)
        )
        self.wait()

        self.play(Unwrite(xreserves), Unwrite(yreserves))
        self.play(chart_vg.animate.move_to(ORIGIN+DOWN*0.2).scale(1.25))

        d1_border = Dot(stroke_width=4, fill_opacity=0, radius=0.15).set_color(BLUE_C).move_to(ax.c2p(1, 1))
        self.add(d1_border)

        # xline = always_redraw(lambda: DashedLine(ax.c2p(x.get_value(), 0), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C))
        xline = DashedLine(ax.c2p(x.get_value(), 0), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C).add_updater(lambda m: m.put_start_and_end_on(ax.c2p(x.get_value(), 0), ax.c2p(x.get_value(),1/x.get_value())))
        yline = DashedLine(ax.c2p(0,1/x.get_value()), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C).add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0,1/x.get_value()), ax.c2p(x.get_value(),1/x.get_value())))

        xline0 = DashedLine(ax.c2p(x.get_value(), 0), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C)
        yline0 = DashedLine(ax.c2p(0,1/x.get_value()), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C)

        x_label = MathTex("x", color=BLUE_C).add_updater(lambda m: m.next_to(ax.c2p(x.get_value(), 0),DOWN))
        y_label = MathTex("y", color=BLUE_C).add_updater(lambda m: m.next_to(ax.c2p(0, 1/x.get_value()),LEFT))
       
        x0_label = MathTex("x_0", color=BLUE_C).move_to(ax.c2p(x.get_value(), 0)).shift(DOWN*0.35)
        y0_label = MathTex("y_0", color=BLUE_C).move_to(ax.c2p(0, 1/x.get_value())).shift(LEFT*0.35)

        labels_0 = VGroup(x0_label, y0_label)

        self.remove(d1)
        d1 = Dot(radius=0.125).set_color(BLUE_C).add_updater(lambda m: m.move_to(ax.c2p(x.get_value(), 1/x.get_value())))
        self.add(d1)

        self.play(Write(xline), Write(yline), Write(x_label), Write(y_label))

        self.wait()

        self.add(xline0)
        self.add(yline0)

        self.play(
            x.animate.set_value(0.3).set_color(ORANGE),
            x_label.animate.set_color(ORANGE),
            y_label.animate.set_color(ORANGE),
            xline.animate.set_color(ORANGE),
            yline.animate.set_color(ORANGE),
            d1.animate.set_color(ORANGE),
            FadeIn(x0_label),
            FadeIn(y0_label),
            rate_func=rate_functions.ease_in_out_cubic
        )

        dx_buy_dy_12 = MathTex("dy^{+}","=\\frac{y_0\cdot dx^{-}(1-\phi)}{x_0+dx^{-}(1-\phi)}").scale(0.75).move_to(dx_buy_dy_11)
        sr_12 = SurroundingRectangle(dx_buy_dy_12, color=UNISWAP_PINK, buff=0.15)
        

        x1_label = MathTex("x_1", color=ORANGE).move_to(ax.c2p(x.get_value(), 0)).shift(DOWN*0.35)
        y1_label = MathTex("y_1", color=ORANGE).move_to(ax.c2p(0, 1/x.get_value())).shift(LEFT*0.35)

        self.play(
            TransformMatchingTex(x_label, x1_label),
            TransformMatchingTex(y_label, y1_label),
        )

        self.wait()

        self.play(Wiggle(labels_0), Wiggle(dx_buy_dy_11))
        self.play(Transform(sr_10, sr_12), TransformMatchingTex(dx_buy_dy_11, dx_buy_dy_12))

        dy_line = Line(ax.c2p(1,1), ax.c2p(1, 1/x.get_value()))
        dx_line = Line(ax.c2p(x.get_value(), 1/x.get_value()), ax.c2p(1,1/x.get_value()))

        dx_text = MathTex("dx^{-}").scale(0.75).add_updater(lambda m: m.next_to(dx_line, UP).shift(UP*0.5+RIGHT*0.15))
        dy_text = MathTex("dy^{+}").scale(0.75).add_updater(lambda m: m.next_to(dy_line, RIGHT).shift(RIGHT*0.5))

        brace_dx = BraceBetweenPoints(
            ax.c2p(x.get_value(),1/x.get_value()),
            ax.c2p(1,1/x.get_value()), 
            direction=UP)
        
        brace_dy = BraceBetweenPoints(
            ax.c2p(1,1),
            ax.c2p(1, 1/x.get_value()), 
            direction=RIGHT)

        # self.play(Write(dy_line), Write(dx_line))
        self.play(Write(brace_dx), Write(brace_dy))
        self.play(Write(dx_text), Write(dy_text))

        self.play(FocusOn(dx_buy_dy_12[0]))
        self.play(FocusOn(dy_text))

        self.wait(2)