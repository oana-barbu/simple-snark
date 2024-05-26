from manim import *
from numpy import poly1d

FONT_SIZE = 36


class SchwartzZippel(Scene):
    def construct(self):
        # Define polynomials
        intersects = poly1d([1, -1]) * poly1d([1, -3])
        f = poly1d([1, -3, 3])
        g = f - intersects

        grid = NumberPlane()
        self.add(grid)

        f_graph = FunctionGraph(f)
        f_graph.set_color(GREEN)
        self.add(f_graph)
        self.wait()

        g_graph = FunctionGraph(g)
        g_graph.set_color(PURPLE)
        self.add(g_graph)

        # Calculate the intersection points
        points = [(1, g(1)), (3, g(3))]

        # Create and add dots at the intersection points
        dots = []
        for x, y in points:
            self.wait(0.3)
            dot = Dot(
                point=grid.c2p(x, y),
                color=YELLOW,
                radius=DEFAULT_DOT_RADIUS * 1.5
            )
            dots.append(dot)
            self.add(dot)

        self.wait()
        self.clear()

        self.wait()

        eq1 = MathTex(
            'f(x) = g(x)'
        ).to_edge(UP)
        self.play(Write(eq1))

        self.wait()
        eq2 = MathTex('x^2 - 3x + 3 = x')
        eq2.next_to(eq1, DOWN)
        self.play(Write(eq2))

        self.wait()
        eq3 = MathTex('x^2 - 3x + 3', '-x', ' = x', '-x')
        eq3[-1].set_color(YELLOW)
        eq3[-3].set_color(YELLOW)
        eq3.next_to(eq1, DOWN)
        self.play(TransformMatchingTex(eq2, eq3))

        self.wait()
        eq4 = MathTex('x^2 - 4x + 3 = 0')
        eq4.next_to(eq1, DOWN)
        self.play(TransformMatchingTex(eq3, eq4))

        self.wait()
        eq5 = MathTex('(x - 1)(x - 3) = 0')
        eq5.next_to(eq4, DOWN)
        self.play(Write(eq5))

        self.wait()
        zeros_text = MathTex(
            '\\Rightarrow f\\text{ and }g\\text{ intersect at }1\\text{ and }3'
        )
        zeros_text.next_to(eq5, DOWN)
        self.play(Write(zeros_text))

        self.wait(2.5)
        generalized = MathTex(
            '\\text{polynomials of degree }d\\text{ have at most }d\\text{ intersections}'
        ).set_color(YELLOW)
        generalized.next_to(zeros_text, DOWN)
        self.play(Write(generalized))

        self.wait(2)

        self.clear()
        self.wait()

        poly_comp = MathTex(
            'f(x) \\stackrel{?}{=} f\'(x)\\text{ and }deg(f) < 10^6'
        )
        poly_comp.to_edge(UP)
        self.play(Write(poly_comp))
        self.wait()

        challenge = MathTex(
            '\\text{challenge: }z \\in_R [0, 10^{70}]'
        )
        challenge.next_to(poly_comp, DOWN)
        self.play(Write(challenge))
        self.wait()

        pot_ineq = MathTex(
            'f(x) \\ne f\'(x)'
        )
        pot_ineq.next_to(challenge, DOWN)
        self.play(Write(pot_ineq))
        self.wait()

        probab = MathTex(
            '\\Rightarrow p(f(z) = f\'(z)) = \\frac{10^6}{10^{70}}',
            '\\approx 0',
            font_size=36

        )
        probab[-1].set_color(YELLOW)
        probab.next_to(pot_ineq, DOWN)
        self.play(Write(probab))
        self.wait()

        statement = MathTex(
            '\\text{If }f(z) = f\'(z)\\text{ then }f(x) = f\'(x)\\text{ at all }x').set_color(YELLOW)
        statement.next_to(probab, DOWN)
        self.play(Write(statement))
        self.wait()
