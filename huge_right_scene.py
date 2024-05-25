from manim import *

FONT_SIZE = 40


class HugeRightEquation(Scene):

    def construct(self):
        eq1 = MathTex(
            'Va(',
            'x',
            ') = (\\frac{1}{2} - a_0 + a_1)\\cdot',
            'x',
            '^2 + (-\\frac{5}{2} + 4a_0 - 4a_1)\\cdot',
            'x',
            ' + (2 - 3a_0 + 4a_1)',
            font_size=FONT_SIZE
        )
        eq1.to_edge(UP)
        self.add(eq1)
        self.wait(1)
        eq2 = MathTex(
            'Va(',
            '2',
            ') = (\\frac{1}{2} - a_0 + a_1)\\cdot',
            '2^2',
            '+ (-\\frac{5}{2} + 4a_0 - 4a_1)\\cdot',
            '2',
            ' + (2 - 3a_0 + 4a_1)',
            font_size=FONT_SIZE
        )
        eq2.to_edge(UP)
        eq2[1::2].set_color(YELLOW)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(0.5)

        eq3 = MathTex(
            'Va(',
            '2',
            ') = (\\frac{1}{2} - a_0 + a_1)\\cdot',
            '4',
            '+ (-\\frac{5}{2} + 4a_0 - 4a_1)\\cdot',
            '2',
            '+ (2 - 3a_0 + 4a_1)',
            font_size=FONT_SIZE
        )
        eq3.to_edge(UP)
        eq3[1::2].set_color(YELLOW)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)

        req1 = MathTex(
            # power of two
            '= (',
            '4\\cdot',
            '\\frac{1}{2} - ',
            '4\\cdot',
            'a_0 + ',
            '4\\cdot',
            'a_1 ',
            ')',
            # power of 1
            '+ (',
            '2\\cdot',
            '(-\\frac{5}{2}) + ',
            '2\\cdot',
            '4a_0 -',
            '2\\cdot',
            '4a_1',
            ')',
            # power of 0 (constants)
            '+ (2 - 3a_0 + 4a_1)',
            font_size=FONT_SIZE
        )
        for i in (1, 3, 5,  9, 11, 13):
            req1[i].set_color(YELLOW)
        req1.next_to(eq3, direction=DOWN)
        self.play(Write(req1))
        self.wait(1)

        req2 = MathTex(
            # power of two
            '= ',
            '4\\cdot',
            '\\frac{1}{2} - ',
            '4\\cdot',
            'a_0 + ',
            '4\\cdot',
            'a_1 -',
            '2\\cdot',
            '\\frac{5}{2} + ',
            '2\\cdot',
            '4a_0 -',
            '2\\cdot',
            '4a_1',
            '+ 2 - 3a_0 + 4a_1',
            font_size=FONT_SIZE
        )
        for i in (1, 3, 5, 7, 9, 11):
            req2[i].set_color(YELLOW)
        req2.next_to(eq3, direction=DOWN)
        self.play(TransformMatchingTex(req1, req2))
        self.wait(1)

        req3 = MathTex(
            '=2 - 4a_0 + 4a_1 - 5 + 8a_0 - 8a_1 + 2 - 3a_0 + 4a_1',
            font_size=FONT_SIZE
        )
        req3.next_to(req2, direction=DOWN)
        self.play(Write(req3))
        self.wait(1)

        req4 = MathTex(
            '=- 4a_0 + 8a_0 - 3a_0 + 4a_1 - 8a_1 + 4a_1 + 2 - 5 + 2',
            font_size=FONT_SIZE
        )
        req4.next_to(req3, direction=DOWN)
        self.play(Write(req4))
        self.wait(1)

        req5 = MathTex(
            'Va(2) = 1a_0',
            '+ 0a_1',
            '- 1',
            font_size=FONT_SIZE
        )
        req5[1].fade()
        req5.next_to(req4, direction=DOWN)
        self.play(Write(req5))
        self.wait(1)

        req6 = MathTex(
            'Va(2) = a_0 - 1',
            font_size=FONT_SIZE
        )
        req6.next_to(req4, direction=DOWN)
        self.play(TransformMatchingTex(req5, req6))
        self.wait(1)
