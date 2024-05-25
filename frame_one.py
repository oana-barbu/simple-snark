from manim import *

class FrameOne(Scene):
    def construct(self):
        c_4 = 1
        c_3 = -7
        c_2 = 14
        c_1 = -8

        equation_start = MathTex(
            r"f(x) = x^4 - 7x^3 + 14x^2 - 8x",
            # r"f(x) = \quad x^4 - 7x^3 + 14x^2 - \quad x \qquad \qquad \qquad \qquad    ",
            # r"f(x) = px^4 - 7x^3 + 14x^2 p ppp p ppp",
            # substrings_to_isolate="p"
        )
        # equation_start.set_color_by_tex("p", BLACK)
        
        self.add(equation_start)
        self.wait()

        equation_extended = MathTex(
            r"f(x) = 1x^4 - 7x^3 + 14x^2 - 8x^1 + 0x^0",
            substrings_to_isolate="x, 0, 1, 2, 3, 4"
        )
        equation_extended.set_color_by_tex("x", YELLOW)
        # equation_extended.set_color_by_tex("0", BLUE)
        # equation_extended.set_color_by_tex("1", BLUE)
        # equation_extended.set_color_by_tex("2", BLUE)
        # equation_extended.set_color_by_tex("3", BLUE)
        # equation_extended.set_color_by_tex("4", BLUE)
        # equation_extended[0][19].set_color(RED)

        self.play(ReplacementTransform(equation_start, equation_extended))
        
        self.wait()

        equation = MathTex(
            r"f(x) = x^4 - 7x^3 + 14x^2 - 8x",
        )
        self.add(equation)

        # self.play(FadeOut(equation_start))
        self.play(ReplacementTransform(equation_extended, equation))
        
        # self.play(FadeOut(equation_extended))
        self.wait()

        self.play(equation.animate.shift(DOWN * 3))
        self.wait()

        ax = Axes(
            x_range=[-2, 5, 1],
            y_range=[-20, 100, 20],
            tips=False,
            axis_config={"include_numbers": False},
            # y_axis_config={"scaling": LogBase(custom_labels=True)},
        ).move_to(UP)

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(
            lambda t: c_4 * t ** 4 + c_3 * t ** 3 + c_2 * t ** 2 + c_1 * t, 
            x_range=[-2, 5], 
            use_smoothing=False
        )
        self.play(FadeIn(ax))
        self.wait()
        self.play(Create(graph))
        
        self.wait()

        equation_scaled = MathTex(
            r"2f(x) = 2x^4 - 14x^3 + 28x^2 - 2x",
        )
        self.play(Transform(equation, equation_scaled.move_to(DOWN * 3)))
        # self.play(FadeOut(equation))

        graph_scaled = ax.plot(
            lambda t: 2 * c_4 * t ** 4 + 2 * c_3 * t ** 3 + 2 * c_2 * t ** 2 + 2 * c_1 * t, 
            x_range=[-2, 5],
            use_smoothing=False
        )

        self.play(Transform(graph, graph_scaled))
        # self.play(FadeOut(graph))

        self.wait()
