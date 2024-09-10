from manim import *

class TestPrincipal(Scene):
    def construct(self):
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a= Square().set_color(BLUE).shift(RIGHT)
        m2b= Circle().set_color(BLUE).shift(RIGHT)

        self.play(FadeIn(m1a,m2a))
        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1.5)
        self.play(FadeOut(m1a,m2a))
        self.wait(1)

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(r'$\mathscr{H} \rightarrow \mathbb{H}$}', tex_template=myTemplate, font_size=144)
        
        R = Tex(r'$\mathbb{R}$',tex_template=myTemplate, font_size=144)
        Q = Tex(r'$\mathbb{Q}$',tex_template=myTemplate, font_size=144)

        self.add(R)
        self.play(FadeIn(R))
        self.wait(1)
        self.play(Transform(R,Q))
        self.wait(1)
        self.play(FadeOut(R))
        self.wait(1)

        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", WHITE)
        self.add(equation)
        self.play(FadeIn(equation))
        self.wait(1)
