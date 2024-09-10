from math import *
from manim import *
from manim.utils import scale, tex_templates
from numpy import array, square

class MainFunction(MovingCameraScene):
    def construct(self):
        delta(self)
        gamma(self)
        delta_gamma(self)
        vega(self)
        theta(self)
        rho(self)
        box_all(self)
        self.wait()

def delta(self):
    pass

def gamma(self):
    pass

def delta_gamma(self):
    """
    This method simply displays the image of Delta and Gamma.
    """

    # Create a LaTeX template for the title:
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    title_delta = Tex(r'\underline{$\Delta$ \& $\Gamma$ - How does the value of our options change?}', tex_template=myTemplate, font_size=40).move_to(UP*2)

    # We create the image object and display it:
    image_delta = ImageMobject("media/images/theta_time_decay/delta_explained.png")
    self.play(Write(title_delta),FadeIn(image_delta))
    self.wait()

    # We group our two elements to be able to surround them and 
    # move them around:
    gDeltaGamma = Group(title_delta,image_delta)
    framebox_dg = always_redraw(lambda: SurroundingRectangle(gDeltaGamma, buff = .1))
    self.play(Write(framebox_dg))
    self.play(gDeltaGamma.animate.scale(0.18).shift(LEFT*5.5,UP*2.75))

    global dg 
    dg = Group(gDeltaGamma,framebox_dg)

    self.wait()

def vega(self):
    """
    This method plots all the equations and curve_1ics related to Vega and Implied Volatility.
    """
    # Create title and first equation:
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    title_vega = Tex(r'\underline{$\nu$ - How does IV affect our options?}', tex_template=myTemplate, font_size=40).move_to(UP)
    eq_vega = Tex(r'$\nu = \dfrac{\partial V}{\partial \sigma}$', tex_template=myTemplate, font_size=40)

    # Plot them:
    self.play(Write(title_vega))
    self.play(Write(eq_vega))
    self.wait(0.5)
    self.play(FadeOut(eq_vega))
    self.play(title_vega.animate.shift(UP*2))

    # Create the axes:
    ax = Axes(
            x_range = [-5, 5, 1],
            y_range = [0, 1, 0.2],
            tips=False,
            axis_config = {'include_numbers':False}
        )

    # Initialize mu (distribution mean) = 0, we will not use it
    # and sigma (standard deviation) + k (ValueTrackers) to 0 and 1:
    mu = ValueTracker(0)
    sigma = ValueTracker(1)
    k = ValueTracker(1)

    # We draw our PDF function:
    curve = always_redraw(lambda: ax.plot(
        lambda x: PDF_normal(x, 0, sigma.get_value(), k.get_value())).set_color(BLUE_C)
    )

    # We group the axes and the curve to scale them both
    curve_1Group = Group(ax,curve)
    curve_1Group.scale(0.5)

    # Text to display distrubtion mean (sigma):
    sigma_text = MathTex(r'\sigma =').next_to(ax, UP*4, buff=0.2).set_color(WHITE)
    sigma_text.shift(LEFT*0.4)

    # Decimal number with redraw updater:
    sigma_value_text = always_redraw(
        lambda: DecimalNumber(num_decimal_places=2)
        .set_value(sigma.get_value())
        .next_to(sigma_text, RIGHT, buff=0.2)
        .set_color_by_gradient(PINK,ORANGE)
        .scale(0.6)
    )

    # Idem but for 'k':
    k_text = MathTex(r'k =').set_color(WHITE).move_to(sigma_text.get_center())
    k_text.shift(DOWN*0.4)

    k_value_text = always_redraw(
        lambda: DecimalNumber(num_decimal_places=2)
        .set_value(k.get_value())
        .next_to(k_text, RIGHT, buff=0.2)
        .set_color_by_gradient(PINK,ORANGE)
        .scale(0.6)
    )

    gText = Group(k_text,sigma_text).set_color_by_gradient(PURPLE_C, PINK)

    # Text displayed in the base with a cool color gradient:
    base_text = MathTex(r'\longleftarrow \text{Out of the money}\quad\text{ATM}\quad\text{In the money} \longrightarrow').next_to(ax, DOWN, buff=0.2).scale(0.35).set_color_by_gradient(PURPLE_C,PINK,ORANGE)
    base_text.shift(LEFT*0.15)

    # Display some things:
    self.play(Write(ax), Write(sigma_text), Write(sigma_value_text), Write(k_text), Write(k_value_text), Write(base_text))
    self.play(Create(curve))

    # Functions to explain how time until expiration affects vega:
    func1 =  ax.plot(lambda x: PDF_normal(x, 0, 0.5, 0.2)).set_color(RED_C)
    func2 =  ax.plot(lambda x: PDF_normal(x, 0, 1, 1)).set_color(BLUE_C)
    func3 =  ax.plot(lambda x: PDF_normal(x, 0, 1.5, 5)).set_color(YELLOW_C)

    # Legend of the functions above:
    exp1 = Tex(r'30 days till expiration').scale(0.4).set_color(RED_C).move_to(k_text)
    exp1.shift(LEFT*1.5,DOWN)
    exp2 = Tex(r'15 days').move_to(exp1.get_left()).scale(0.4).set_color(BLUE_C).shift(DOWN*0.2,RIGHT*0.3)
    exp3 = Tex(r'5 days').move_to(exp1.get_left()).scale(0.4).set_color(YELLOW_C).shift(DOWN*0.4,RIGHT*0.25)

    # Change sigma and k values (updaters):
    self.play(sigma.animate.set_value(0.5),k.animate.set_value(0.2), run_time=1, rate_func=rate_functions.smooth)
    self.wait(0.5)
    self.play(sigma.animate.set_value(1.5),k.animate.set_value(5), run_time=1, rate_func=rate_functions.smooth)
    self.wait(0.5)
    self.play(sigma.animate.set_value(1),k.animate.set_value(1), run_time=1, rate_func=rate_functions.smooth)

    # Remove from screen the curve and values:
    self.play(FadeOut(sigma_text),FadeOut(k_text),FadeOut(sigma_value_text), FadeOut(k_value_text), run_time=0.25)
    curve_1Group.remove()
    curve.remove()

    # We group everything so we are able to move it around:
    provGroup = Group(ax,exp1,exp2,exp3,func1,func2,func3,base_text)

    # We display the three functions:
    self.play(Write(exp1),Create(func1),FadeOut(curve),FadeIn(func2),FadeIn(exp2),Write(exp3),Create(func3), run_time=1.5)
    self.play(provGroup.animate.shift(UP*1))

    # Group everything to framebox it:
    grupoVega = Group(title_vega, provGroup, ax)
    framebox_vega = always_redraw(lambda: SurroundingRectangle(grupoVega, buff = .1))
    self.play(Write(framebox_vega))
    self.play(grupoVega.animate.scale(0.265).shift(LEFT*5.5, UP*0.5))

    # Remove the things -> otherwise visual bugs appear because of grouping:
    sigma_text.remove()
    k_text.remove()
    sigma_value_text.remove()
    k_value_text.remove()
    
    
    # We declare a new global group to be able to access it from: def box_all(self):
    global vegagroup
    vegagroup = Group(grupoVega,framebox_vega)
    self.wait()

def theta(self):
    """
    I have been trying out how to fit Theta decay with a fairly
    simple equation. This is what I've come up with:

    Old: -(1/145)*(x**2)+100
    New: (100/sqrt(120))*sqrt(abs(x-120))
    """
    # We save the camera state so we can return
    # to the original view later on:
    self.camera.frame.save_state()
    
    # Define the axes and the function:
    ax = Axes(x_range=[0, 120, 30], y_range=[0, 100, 100], tips = False)
    
    curve_1 = ax.plot(lambda x: -(1/145)*(x**2)+100, x_range=[0, 120], color=WHITE, use_smoothing=True)

    # Create a LaTeX template for the title:
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    title_theta = Tex(r'\underline{$\theta$ - How does time decay affect our options?}', tex_template=myTemplate, font_size=40).next_to(curve_1, UP)

    # Define three vertical lines (Days remaining until expiration)
    line_1 = ax.get_vertical_line(ax.i2gp(30, curve_1), color=BLUE_C)
    line_2 = ax.get_vertical_line(ax.i2gp(60, curve_1), color=BLUE_C)
    line_3 = ax.get_vertical_line(ax.i2gp(90, curve_1), color=BLUE_C)

    # Define the dots:
    moving_dot = Dot(ax.i2gp(curve_1.t_min, curve_1), color=ORANGE)
    dot_1 = Dot(ax.i2gp(curve_1.t_min, curve_1))
    dot_2 = Dot(ax.i2gp(curve_1.t_max, curve_1))

    # We create and show a Vector Group with all our elements 
    # to be able to move it around the screen:
    theta = VGroup(title_theta, line_1, line_2, line_3, ax, curve_1, dot_1, dot_2, moving_dot)
    theta.move_to(RIGHT).scale(0.7)
    self.play(Write(title_theta))
    self.play(FadeIn(line_1, line_2, line_3, ax, curve_1, dot_1, dot_2, moving_dot))

    # We zoom in into the orange dot:
    self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

    # Updater to follow the dot with the camera:
    def update_curve(mob):
        mob.move_to(moving_dot.get_center())

    # We follow the orange dot along the function and 
    # restore the camera to its original position:
    self.camera.frame.add_updater(update_curve)
    self.play(MoveAlongPath(moving_dot, curve_1, rate_func=linear))
    self.camera.frame.remove_updater(update_curve)
    self.play(Restore(self.camera.frame))
    self.wait(0.25)

    # We draw a frame around our VGroup:
    framebox_theta = always_redraw(lambda: SurroundingRectangle(theta, buff = .1))
    self.play(Write(framebox_theta))

    # We move everything into the left down corner:
    self.play(theta.animate.scale(0.2).shift(LEFT*6.5,DOWN*0.05))

    global thetagroup
    thetagroup = Group(theta, framebox_theta)

    self.wait() 

def rho(self):
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    title_rho = Tex(r'\underline{$\rho$ - How risk-free rate of interest affects our options?}', tex_template=myTemplate, font_size=40).move_to(UP)
    
    eq1 = Tex(r'$\rho = \pm K\ t e^{-rt} N(\pm d2)$', tex_template=myTemplate, font_size=40)
    eq2 = Tex(r'where: $d1 = \dfrac{ln(\frac{S}{K}) + (r+\frac{\sigma^2}{2})t}{\sigma \sqrt{t}};$', tex_template=myTemplate, font_size=40).move_to(DOWN)
    eq3 = Tex(r'$d2 = d1 - \sigma \sqrt{t}$').move_to(DOWN*2)
    
    grho = Group(title_rho,eq1,eq2,eq3).scale(0.7).move_to(UP)

    self.play(Write(title_rho))
    self.play(Write(eq1))
    self.play(Write(eq2))
    self.play(Write(eq3))

    framebox_rho = always_redraw(lambda: SurroundingRectangle(grho, buff = .1))
    self.play(Write(framebox_rho))
    self.play(grho.animate.scale(0.3).shift(LEFT*5.5,DOWN*2.5))

    global rhogroup
    rhogroup = Group(grho, framebox_rho)

    self.wait()

def box_all(self):
    boxGroup = Group(dg,vegagroup,thetagroup,rhogroup)
    fba = always_redraw(lambda: SurroundingRectangle(boxGroup, buff = .3, corner_radius=0.1).set_color_by_gradient(PURPLE_C,PINK,BLUE_C))
    self.play(Write(fba))

    self.play(boxGroup.animate.arrange(DOWN,buff=.2))
    self.wait()

    svg = SVGMobject("media/images/greeks/youtube.svg") 

    for element in boxGroup:
        svg = SVGMobject("media/images/greeks/youtube.svg")
        svg.shift(element.get_center()).scale(0.5)
        self.play(FadeOut(element),Write(svg), run_time = 0.5)

    self.wait()

def PDF_normal(x, mu, sigma,k):
    return exp(-(((k*x)-mu)**2)/(2*sigma**2))/(sigma*sqrt(2*pi))