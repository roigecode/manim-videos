import manim
import manimlib
import manimpango

from manimlib import *

class TestScene(Scene):
  def construct(self):
    t = TextMobject("Hello manim!")
    t.scale(2)

    self.play(Write(t))
    self.wait()