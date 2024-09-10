from manim import *
from math import sqrt, exp, pi, erf
from manim.mobject.mobject import T
from manim.utils import scale
import csv
import numpy as np


class MainFunction(MovingCameraScene):
    def construct(self):
        
        dates = []
        close = []

        archivo = 'wh.csv'
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    dates.append(row[0])
                    close.append(float(row[1]))
                except ValueError:
                    pass
                except IndexError:
                    pass

        defclose = [float(close[x]) for x in range(0,len(close))]

        xvals = [x for x in range(len(defclose))]
        yvals = defclose[:]


        ax = Axes(
            x_range=[0,21000,1000],
            y_range=[0,15,1],
            tips=False,
            x_length=10,
            y_axis_config={"include_numbers":True, "font_size":17}
        )

        date1 = Tex(r'27/07/1959',font_size=17).move_to(ax.c2p(0,0))
        date1.shift(DOWN*0.3)
        date1.shift(RIGHT*0.3)

        date2 = Tex(r'17/12/2021', font_size=17).move_to(ax.c2p(16000,0))
        date2.shift(DOWN*0.3)
        date2.shift(RIGHT*0.3)

        date3 = Tex(r'14/01/1991', font_size=17).move_to(ax.c2p(8000,0))
        date3.shift(DOWN*0.3)
        date3.shift(RIGHT*0.2)

        label = ax.get_axis_labels(y_label=Tex(r'[\$] Wheat Prices - 61 Year Historical Chart (1960-2021):', font_size=15), x_label="")
        ax.center()

        graf = ax.plot_line_graph(
            x_values = xvals,
            y_values= yvals,
            add_vertex_dots=False,
            stroke_width=0.8
        )

        graf.set_color_by_gradient([YELLOW,ORANGE,PINK,PURPLE])

        x_vals_sub = [16000,16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000,20500,21000]
        y_vals_sub = [7.75, 8.5, 7.5, 8, 10, 9, 11.5,10,13,11.5,14]
        func_sub = ax.plot_line_graph(x_values=x_vals_sub, y_values=y_vals_sub, add_vertex_dots=False).set_color(PURE_GREEN)

        x_vals_baj = [16000,16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000,20500,21000]
        y_vals_baj = [7.75, 6, 7, 6.5, 7.5, 5, 6.5, 4,5,3,4,2,4.5]
        func_baj = ax.plot_line_graph(x_values=x_vals_baj, y_values=y_vals_baj, add_vertex_dots=False).set_color(PURE_RED)

        x_vals_med = [16000,16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000,20500,21000]
        y_vals_med = [7.75, 7.5, 8, 7.5, 8, 7.5, 8, 7, 8, 7.5, 7.75]
        func_med = ax.plot_line_graph(x_values=x_vals_med, y_values=y_vals_med, add_vertex_dots=False).set_color(WHITE)

        self.play(Write(ax), Write(label), Write(date1), Write(date2),Write(date3), rate_func=linear)
        self.play(Write(graf), rate_func=rate_functions.smooth, run_time=3)
        self.wait()
        self.play(Write(func_sub))
        self.wait()
        self.play(Write(func_baj))
        self.wait()
        self.play(Write(func_med))
        self.wait(2)

        self.play(Unwrite(func_sub), Unwrite(func_baj))
        self.wait(2)

        x_vals_sub2 = [16000,16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000,20500,21000]
        y_vals_sub2 = [7.75, 8.5, 7.5, 8, 10, 9, 11.5,10,13,11.5,14]
        func_sub2 = ax.plot_line_graph(x_values=x_vals_sub2, y_values=y_vals_sub2, add_vertex_dots=False).set_color(PURE_GREEN)

        x_vals_baj = [16000,16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000,20500,21000]
        y_vals_baj = [7.75, 6, 7, 6.5, 7.5, 5, 6.5, 4,5,3,4,2,4.5]
        func_baj = ax.plot_line_graph(x_values=x_vals_baj, y_values=y_vals_baj, add_vertex_dots=False).set_color(PURE_RED)

        self.play(Write(func_sub2), Write(func_baj))

        self.wait(5)