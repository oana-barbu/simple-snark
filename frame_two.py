from manim import *

class FrameTwo(Scene):
    def construct(self):
        logic_table = Table(
            [["0", "0", "1"],
            ["0", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "0"]],
            col_labels=[Tex("$a_0$"), Tex("$a_1$"), Tex("out")],
        )
        self.add(logic_table)
        self.wait()

        self.play(logic_table.animate.scale(0.5).to_edge(UL))
        self.wait()

        condition_0 = MathTex(
            r"\mathcal{C}_0: a_0 \cdot a_1 = 0",
        )
        self.add(condition_0)
        self.wait()
        self.play(condition_0.animate.to_edge(UP))
        self.wait()

        equation_0_1 = MathTex(
            r"0 \cdot 1 = 0",
        )
        self.add(equation_0_1.set_color(GREEN).next_to(condition_0, DOWN))
        self.wait()

        equation_0_2 = MathTex(
            r"0 \cdot 3 = 0",
        )
        self.add(equation_0_2.set_color(PURE_RED).next_to(equation_0_1, DOWN))
        self.wait()

        condition_1 = MathTex(
            r"\mathcal{C}_1: a_0 \cdot (a_0 - 1) = 0",
        )
        self.add(condition_1)
        self.wait()
        self.play(condition_1.animate.next_to(equation_0_2, DOWN))
        self.wait()

        condition_2 = MathTex(
            r"\mathcal{C}_2: a_1 \cdot (a_1 - 1) = 0",
        )
        self.add(condition_2)
        self.wait()
        self.play(condition_2.animate.next_to(condition_1, DOWN))
        self.wait()