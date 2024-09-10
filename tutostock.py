from manim import *
from math import sqrt
from manim.utils import scale
import csv
import numpy as np

class MainFunction(MovingCameraScene):
    def construct(self):
        sopen = []
        high = []
        low = []
        close = []

        archivo = 'AAPL.csv'
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                sopen.append(row[1])
                high.append(row[2])
                low.append(row[3])
                close.append(row[4])

        sopen = sopen[1:]
        high = high[1:]
        low = low[1:]
        close = close[1:]

        defopen = [float(sopen[x]) for x in range(0,len(sopen))]
        defhigh = [float(high[x]) for x in range(0,len(high))]
        deflow = [float(low[x]) for x in range(0,len(low))]
        defclose = [float(close[x]) for x in range(0,len(close))]

        xvals = [x for x in range(233)]
        yvals = defclose[:]

        ax = Axes(
            x_range=[0,232,30],
            y_range=[75,170,20],
            tips=False,
            x_length=10,
            axis_config={"include_numbers":False}
        )


        label = ax.get_axis_labels(y_label=Tex(r'NASDAQ: AAPL', font_size=15), x_label="")
        ax.center()

        graf = ax.plot_line_graph(
            x_values = xvals,
            y_values= yvals,
            add_vertex_dots=False,
        )

        graf.set_color_by_gradient([YELLOW,ORANGE,PINK,PURPLE])

        self.play(Write(ax), Write(label), rate_func=rate_functions.smooth)
        self.play(Write(graf), rate_func=rate_functions.smooth, run_time=2)
        self.wait(2)

"""
# HAY QUE PASAR EL OBJETO AX POR PARAMETRO PARA AJUSTAR A PANTALLA:
def plotcandlewrong(self,sopen,high,low,close):
        # 133.520004 // 133.610001 // 126.760002 // 129.410004
        print("Values: ",sopen,high,low,close)
        # Draw rectangle between open and close:
        try:
            print("Drawing: ", end='')
            if sopen<close:
                print("height = ", (close-sopen))
                roc = Rectangle(height=(close-sopen),width=4,color=GREEN_C) #.move_to((sopen+close)/2)
            else:
                print("height = ", (sopen-close))
                roc = Rectangle(height=(sopen-close),width=4,color=PURE_RED) #.move_to((sopen+close)/2)

            # Add tip from high to open:
            lho = Line(high,sopen, color=WHITE)
            # Add tip from close to low:
            llc = Line(low, close, color=WHITE)

            self.play(Write(roc),Write(lho),Write(llc))
        except TypeError as e:
            print("Error: ", e)

"""
