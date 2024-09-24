from manim import *
import numpy as np
from math import e

UNISWAP_PINK = ManimColor('#FE0079')
UNISWAP_GREEN = ManimColor('#00fe83')
UNISWAP_BLUE = ManimColor('#007bfe')
UNISWAP_ORANGE = ManimColor('#fe8300')
BG_COLOR = ManimColor('#0F0E17')

class PriceChange(MovingCameraScene):
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
        
        d1 = always_redraw(lambda: Dot(radius=0.15).set_color(BLUE_C).move_to(ax.c2p(x.get_value(), 1/x.get_value())))
        chart_vg = VGroup(ax, vg1, reserves, unilogo, d1)

        self.play(Write(ax), Write(xreserves), Write(yreserves))
        self.play(Write(curve), Unwrite(unilogo), run_time=1.25)
        self.play(Write(equation))
        self.wait()

        self.play(self.camera.frame.animate.scale(0.5).move_to(ax.c2p(1, 1.5)))
        self.play(Write(d1))
        self.play(Flash(d1, color=BLUE_C, line_length=0.1, flash_radius=0.1+SMALL_BUFF))

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
        d1 = Dot(radius=0.15).set_color(BLUE_C).add_updater(lambda m: m.move_to(ax.c2p(x.get_value(), 1/x.get_value())))
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
            run_time=1.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        dx_buy_dy_12 = MathTex("dy^{+}","=\\frac{y_0\cdot dx^{-}(1-\phi)}{x_0+dx^{-}(1-\phi)}").scale(0.75).move_to(dx_buy_dy_11).shift(LEFT*0.2)
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
            direction=UP
        )
        
        brace_dy = BraceBetweenPoints(
            ax.c2p(1,1),
            ax.c2p(1, 1/x.get_value()), 
            direction=RIGHT
        )

        self.play(Write(dy_line), Write(dx_line))
        self.play(Write(brace_dx), Write(brace_dy), Write(dx_text), Write(dy_text))

        self.play(FocusOn(dx_buy_dy_12[0]))
        self.play(FocusOn(dy_text))

        self.wait(3)

        allGroup = VGroup(
            chart_vg, 
            dx_buy_dy_12, 
            sr_12, 
            sr_10,
            xline,
            yline,
            xline0,
            yline0,
            dy_line, 
            dx_line,
            brace_dx, 
            brace_dy, 
            dx_text, 
            dy_text,
            x1_label,
            y1_label,
            x0_label,
            y0_label,
            d1_border,
            d1,
        )

        self.play(Unwrite(allGroup))

        self.wait(2)

class ValueImpermanentLoss(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.camera.frame.save_state()

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

        curve = ax.plot(
            lambda x: 1/x,
            x_range=[0.2, plotlim],
            use_smoothing=True,
            color=UNISWAP_PINK
        )

        xreserves = Tex("X reserves", color=WHITE).move_to(ax.c2p(plotlim/2,0)).shift(DOWN*0.5)
        yreserves = Tex("Y reserves", color=WHITE).rotate(PI/2).move_to(ax.c2p(0,plotlim/2)).shift(LEFT*0.5)
        reserves = VGroup(xreserves, yreserves)
        equation = MathTex("x","\\cdot","y","=", "k", color=UNISWAP_PINK).move_to(ax.c2p(plotlim*0.65, plotlim*0.6))

        vg1 = VGroup(curve, equation)
        
        x = ValueTracker(1)
        
        d1 = always_redraw(lambda: Dot(radius=0.15).set_color(BLUE_C).move_to(ax.c2p(x.get_value(), 1/x.get_value())))

        self.play(Write(ax), Write(xreserves), Write(yreserves))
        self.play(Write(curve), Unwrite(unilogo), run_time=1.25)
        self.play(Write(equation))
        self.wait()

        self.play(self.camera.frame.animate.scale(0.75).move_to(ax.c2p(1, 2)), Unwrite(xreserves), Unwrite(yreserves))
        self.play(Write(d1))
        d1_border = Dot(stroke_width=4, fill_opacity=0, radius=0.15).set_color(BLUE_C).move_to(ax.c2p(1, 1))
        d1.z_index = 1

        self.play(Flash(d1, color=BLUE_C, line_length=0.1, flash_radius=0.1+SMALL_BUFF))
        
        # +-----------------+
        # | PRICE ANIMATION |
        # +-----------------+  
        xline = DashedLine(ax.c2p(x.get_value(), 0), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C).add_updater(lambda m: m.put_start_and_end_on(ax.c2p(x.get_value(), 0), ax.c2p(x.get_value(),1/x.get_value())))
        yline = DashedLine(ax.c2p(0,1/x.get_value()), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C).add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0,1/x.get_value()), ax.c2p(x.get_value(),1/x.get_value())))

        xline0 = DashedLine(ax.c2p(x.get_value(), 0), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C)
        yline0 = DashedLine(ax.c2p(0,1/x.get_value()), ax.c2p(x.get_value(),1/x.get_value()), color=BLUE_C)

        x_label = MathTex("x", color=BLUE_C).add_updater(lambda m: m.next_to(ax.c2p(x.get_value(), 0),DOWN))
        y_label = MathTex("y", color=BLUE_C).add_updater(lambda m: m.next_to(ax.c2p(0, 1/x.get_value()),LEFT))
       
        x0_label = MathTex("x_0", color=BLUE_C).move_to(ax.c2p(x.get_value(), 0)).shift(DOWN*0.35)
        y0_label = MathTex("y_0", color=BLUE_C).move_to(ax.c2p(0, 1/x.get_value())).shift(LEFT*0.35)

        new_d1 = Dot(radius=0.15).set_color(BLUE_C).add_updater(lambda m: m.move_to(ax.c2p(x.get_value(), 1/x.get_value())))
        new_d1.z_index = 1

        self.add(new_d1)
        self.remove(d1)

        self.play(Write(d1_border),Write(xline), Write(yline), Write(x_label), Write(y_label))
        self.remove(d1)

        self.wait()

        self.add(xline0)
        self.add(yline0)

        self.play(
            x.animate.set_value(0.3).set_color(ORANGE),
            x_label.animate.set_color(ORANGE),
            y_label.animate.set_color(ORANGE),
            xline.animate.set_color(ORANGE),
            yline.animate.set_color(ORANGE),
            new_d1.animate.set_color(ORANGE),
            FadeIn(x0_label),
            FadeIn(y0_label),
            run_time=1.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        x1_label = MathTex("x_1", color=ORANGE).move_to(ax.c2p(x.get_value(), 0)).shift(DOWN*0.35)
        y1_label = MathTex("y_1", color=ORANGE).move_to(ax.c2p(0, 1/x.get_value())).shift(LEFT*0.35)

        self.play(
            TransformMatchingTex(x_label, x1_label),
            TransformMatchingTex(y_label, y1_label),
        )

        dy_line = Line(ax.c2p(1,1), ax.c2p(1, 1/x.get_value()))
        dy_line.z_index = 0

        dx_line = Line(ax.c2p(x.get_value(), 1/x.get_value()), ax.c2p(1, 1/x.get_value()))
        dx_line.z_index = 0

        brace_dx = Brace(
            dx_line,
            direction=UP
        )

        brace_dy = Brace(
            dy_line,
            direction=RIGHT
        )

        dx_text = MathTex("dx^{-}").scale(0.75).move_to(brace_dx).shift(UP*0.5+RIGHT*0.15)
        dy_text = MathTex("dy^{+}").scale(0.75).move_to(brace_dy).shift(RIGHT*0.5)

        self.play(Write(dy_line), Write(dx_line), Write(brace_dx), Write(brace_dy), Write(dx_text), Write(dy_text))

        self.wait(2)

        new_chart_vg = VGroup(ax, vg1, reserves, unilogo)
        self.play(
            Unwrite(new_d1), 
            Unwrite(x0_label), 
            Unwrite(y0_label), 
            FadeOut(xline), 
            Unwrite(yline), 
            Unwrite(xline0), 
            Unwrite(yline0), 
            Unwrite(d1_border), 
            Unwrite(x1_label), 
            Unwrite(y1_label),
            Unwrite(dy_line), Unwrite(dx_line), Unwrite(brace_dx), Unwrite(brace_dy), Unwrite(dx_text), Unwrite(dy_text)
        )
        self.wait()

        self.play(Restore(self.camera.frame), new_chart_vg.animate.move_to(ORIGIN).shift(LEFT*3))
        
        # +-------+
        # | CASES |
        # +-------+
        equation2 = MathTex("x","\\cdot","y","=", "L^2", color=UNISWAP_PINK).move_to(equation.get_center())
        self.play(Transform(equation, equation2))

        case_p = MathTex("P = \\frac{y}{x}", color=UNISWAP_PINK).scale(0.75)
        case_0 = MathTex("x=\\frac{y}{P} = \\frac{L}{\\sqrt{P}}").scale(0.75)
        case_1 = MathTex("y=L\\sqrt{P}").scale(0.75)
        case_2 = MathTex("\\frac{y^2}{P} = L^2").scale(0.75)
        cases = VGroup(case_p, case_0, case_1, case_2).arrange(DOWN, aligned_edge=LEFT)
        cases_brace = Brace(cases, direction=LEFT)

        cases_braced = VGroup(cases, cases_brace).move_to(ORIGIN).shift(RIGHT*3+UP)

        self.play(Write(case_p))
        self.play(TransformFromCopy(case_p, case_0))
        self.play(TransformFromCopy(case_0, case_1))
        self.play(TransformFromCopy(case_1, case_2))
        self.play(Write(cases_brace))
        self.wait()

        self.play(new_chart_vg.animate.shift(UP*1.5+LEFT*1.5).scale(0.75), cases_braced.animate.shift(DOWN*3+LEFT*8.25).scale(0.75))

        # +----------+
        # | LP VALUE |
        # +----------+
        lp_value_1 = MathTex("V_{LP}(P) := ", "xP+y", color=UNISWAP_PINK).scale(0.75).move_to(ORIGIN + UP*3)
        lp_value_2 = MathTex("= 2\\cdot y").scale(0.75)
        lp_value_3 = MathTex("= 2\\cdot \\frac{k}{x}").scale(0.75)
        lp_value_4 = MathTex("= 2\\cdot \\frac{L^2}{x}").scale(0.75)
        lp_value_5 = MathTex("= 2\\cdot \\frac{L^2}{\\frac{y}{P}}").scale(0.75)
        lp_value_6 = MathTex("= 2\\cdot \\frac{L^2\\cdot P}{y}").scale(0.75)

        lp_values = VGroup(
            lp_value_2,
            lp_value_3,
            lp_value_4,
            lp_value_5,
            lp_value_6
        ).arrange(DOWN, aligned_edge=LEFT).move_to(lp_value_1).shift(RIGHT*0.9 + DOWN*3)
       
        lp_value_7 = MathTex("= 2\\cdot \\frac{L^2\\cdot P}{L\\cdot \\sqrt{P}}").scale(0.75)
        lp_value_8 = MathTex("= 2L\\sqrt{P}").move_to(lp_value_1).scale(0.75)
        
        self.play(TransformFromCopy(equation, lp_value_1))
        self.play(TransformFromCopy(lp_value_1, lp_value_2))
        self.play(TransformFromCopy(lp_value_2, lp_value_3))
        self.play(TransformFromCopy(lp_value_3, lp_value_4))
        self.play(TransformFromCopy(lp_value_4, lp_value_5))
        self.play(TransformFromCopy(lp_value_5, lp_value_6))
        self.wait()
        
        self.play(lp_value_6.animate.move_to(lp_value_2).shift(DOWN*0.5+RIGHT*0.5), FadeOut(lp_value_2), FadeOut(lp_value_3), FadeOut(lp_value_4), FadeOut(lp_value_5))

        lp_values_2 = VGroup(
            lp_value_7,
            lp_value_8
        ).arrange(DOWN, aligned_edge=LEFT).move_to(lp_value_6).shift(DOWN*1.5)

        self.play(TransformFromCopy(lp_value_6, lp_value_7))
        self.play(TransformFromCopy(lp_value_7, lp_value_8))
        self.wait()

        lp_value_final = MathTex("V_{LP}(P) := ","2L\\sqrt{P}").move_to(ORIGIN + UP*3).scale(0.75).set_color(UNISWAP_PINK)
        self.play(Transform(lp_value_8, lp_value_final), FadeOut(lp_value_1), FadeOut(lp_value_7), FadeOut(lp_value_6))
        self.play(Circumscribe(lp_value_final, color=UNISWAP_PINK))
        self.wait()

        # +--------------+
        # | PRICE CHANGE |
        # +--------------+
        price_change_0 = MathTex("\\alpha := \\frac{P_T}{P_0}", color=UNISWAP_PINK).move_to(ORIGIN+UP*2+LEFT*0.75).scale(0.75)
        price_change_1 = MathTex("\\sqrt{\\frac{P_T}{P_0}} = \\sqrt{\\alpha}").move_to(price_change_0).scale(0.75)
        price_change_2 = MathTex("2L\\sqrt{P_T} = 2L\\sqrt{P_0}\\sqrt{\\alpha}").move_to(price_change_0).scale(0.75)
        price_change_3 = MathTex("V_{LP}(P_T) = V_{LP}(P_0)\\sqrt{\\alpha}").move_to(price_change_0).scale(0.75)
        price_change_4 = MathTex("V_T = V_0\\sqrt{\\alpha}").move_to(price_change_0).scale(0.75).shift(DOWN*2)

        price_changes = VGroup(
            price_change_1, 
            price_change_2, 
            price_change_3, 
            price_change_4
        ).arrange(DOWN, aligned_edge=LEFT).move_to(price_change_0).shift(RIGHT*1.2 + DOWN*2)

        self.play(Write(price_change_0))
        self.play(TransformFromCopy(price_change_0, price_change_1))
        self.play(TransformFromCopy(price_change_1, price_change_2))
        self.play(TransformFromCopy(price_change_2, price_change_3))
        self.play(TransformFromCopy(price_change_3, price_change_4))
        self.wait()

        self.play(
            price_change_4.animate.move_to(price_change_0).shift(RIGHT*0.3), 
            price_change_0.animate.shift(DOWN*2.9+LEFT*2.5).scale(0.75), 
            FadeOut(price_change_1), FadeOut(price_change_2), 
            FadeOut(price_change_3)
        )

        self.play(Circumscribe(price_change_4, color=UNISWAP_PINK), price_change_4.animate.set_color(UNISWAP_PINK))

        # +------------+
        # | VALUE HODL |
        # +------------+
        value_hodl_0 = MathTex("V_{HODL} = \\frac{V_0 + V_0 \\cdot \\alpha}{P} = L\\sqrt{P}(1+\\alpha)", color=UNISWAP_PINK).scale(0.75).move_to(lp_value_final).shift(DOWN*2+RIGHT*1.6)
        self.play(Write(value_hodl_0))
        self.wait()

        self.remove(lp_value_1, lp_value_8)
        self.play(
            lp_value_final.animate.move_to(case_0).shift(RIGHT*0.225).scale(0.75),
            FadeOut(case_0),
            price_change_4.animate.move_to(case_1).shift(RIGHT*0.125).scale(0.75),
            FadeOut(case_1),
            value_hodl_0.animate.move_to(case_2).shift(RIGHT*1.775).scale(0.75),
            FadeOut(case_2),
        )

        # +-------------+
        # | LP VS. HODL |
        # +-------------+
        ax2 = Axes(
            x_range=(0, plotlim/2, 0.1),
            y_range=(0, plotlim/2-0.5, 0.1),
            x_length=plotlim*1.5,
            y_length=plotlim*0.5*1.5,
            tips=False,
            axis_config={"include_numbers": False},
            x_axis_config={"include_ticks" : False},
            y_axis_config={"include_ticks" : False},
        ).shift(RIGHT*3+UP*1.7)

        alpha_label = MathTex("\\alpha").scale(0.75).move_to(ax2.c2p(plotlim/4, 0)).shift(DOWN*0.25)
        value_label = Tex("value").scale(0.75).move_to(ax2.c2p(0, plotlim/4)).shift(LEFT*0.25).rotate(PI/2) 

        value_lp_curve = ax2.plot(
            lambda x: np.sqrt(x),
            x_range=[0.01, plotlim/2],
            use_smoothing=True,
            color=UNISWAP_ORANGE
        )

        value_hodl_curve  = ax2.plot(
            lambda x: (1+x)/2,
            x_range=[0.01, plotlim/2],
            use_smoothing=True,
            color=UNISWAP_BLUE
        )

        value_0_constant = ax2.plot(
            lambda x: 0,
            x_range=[0.01, plotlim/2],
            use_smoothing=True,
            color=WHITE
        )

        value_impermanent_loss = ax2.plot(
            lambda x: 2*np.sqrt(x)/(1+x)-1,
            x_range=[0.01, plotlim/2],
            use_smoothing=True,
            color=WHITE
        )

        area = ax2.get_area(value_lp_curve, [0.01, 2.5], bounded_graph=value_hodl_curve, color=RED, opacity=1)
        impermanent_loss_area = ax2.get_area(
            value_impermanent_loss,
            [0.01, 2.5],
            bounded_graph=value_0_constant,
            color=RED,
            opacity=1
        )

        self.play(
            Write(ax2),
            Write(alpha_label),
            Write(value_label)
        )

        self.play(lp_value_final.animate.set_color(UNISWAP_ORANGE))
        self.play(ApplyWave(lp_value_final))
        self.play(Create(value_lp_curve))

        self.play(value_hodl_0.animate.set_color(UNISWAP_BLUE))
        self.play(ApplyWave(value_hodl_0))
        self.play(Create(value_hodl_curve))

        self.play(Write(area), Unwrite(value_lp_curve), Unwrite(value_hodl_curve))
        self.wait()

        new_ax_group = VGroup(ax2, alpha_label, value_label, area)

        old_ax_group = VGroup(ax, curve, equation)
        self.play(FadeOut(old_ax_group), new_ax_group.animate.shift(LEFT*6.25+DOWN*0.25).scale(0.75))

        # +------------------+
        # | IMPERMANENT LOSS |
        # +------------------+
        il_0 = MathTex("IL(\\alpha) := \\frac{V_{LP} - V_{HODL}}{V_{HODL}}", color=UNISWAP_PINK).scale(0.75).shift(UP*2.25+RIGHT*3.5)
        il_1 = MathTex("= \\frac{V_{LP}}{V_{HODL}}-1").scale(0.75)
        il_2 = MathTex("= \\frac{V_0 \\sqrt{\\alpha}}{L\\sqrt{P}(1+\\alpha)}-1").scale(0.75)
        il_3 = MathTex("= \\frac{2L\\sqrt{P}\\sqrt{\\alpha}}{L\\sqrt{P}(1+\\alpha)} - 1").scale(0.75)
        il_4 = MathTex("= \\frac{2\\sqrt{\\alpha}}{1+\\alpha} - 1").scale(0.75)

        il_final = MathTex("IL(\\alpha) := \\frac{2\\sqrt{\\alpha}}{1+\\alpha} - 1", color=UNISWAP_PINK).scale(0.75).move_to(il_0)

        il_vgroup = VGroup(il_1, il_2, il_3, il_4).arrange(DOWN, aligned_edge=LEFT).move_to(il_0).shift(RIGHT*0.75+DOWN*3)

        self.play(Write(il_0))
        self.play(TransformFromCopy(il_0, il_1))
        self.play(TransformFromCopy(il_1, il_2))
        self.play(TransformFromCopy(il_2, il_3))
        self.play(TransformFromCopy(il_3, il_4))

        self.play(
            FadeOut(il_0),
            FadeOut(il_1),
            FadeOut(il_2),
            FadeOut(il_3),
            Transform(il_4, il_final),
        )

        self.play(Circumscribe(il_final, color=RED_C), il_final.animate.set_color(RED_C))

        self.play(lp_value_final.animate.set_color(WHITE), value_hodl_0.animate.set_color(WHITE))

        self.wait(2)