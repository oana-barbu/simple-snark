from manim import *

class FrameThree(Scene):
    def construct(self):
        condition_0 = MathTex(
            r"\mathcal{C}_0: a_0 \cdot \quad a_1 \quad = 0",
        ).to_edge(UL)
        condition_1 = MathTex(
            r"\mathcal{C}_1: a_0 \cdot (a_0 - 1) = 0",
        ).next_to(condition_0, direction=DOWN)
        condition_2 = MathTex(
            r"\mathcal{C}_2: a_1 \cdot (a_1 - 1) = 0",
        ).next_to(condition_1, direction=DOWN)
        self.add(condition_0, condition_1, condition_2)
        self.wait()