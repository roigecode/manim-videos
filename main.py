from manim import *

class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        triangle = Triangle()
        triangle.flip(LEFT)
        triangle.rotate(-3 * TAU / 8)

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))
        self.play(Create(circle))
        self.play(Transform(circle, triangle))
        self.play(FadeOut(circle))
        self.play(Create(triangle))
        self.play(FadeOut(triangle))

        t = Text("Manim Works!")
        t.scale(2)
        

        self.play(Write(t))
        self.play(FadeOut(t))
        self.wait()
