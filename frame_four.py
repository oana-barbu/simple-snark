from manim import *

class FrameFour(Scene):
    def construct(self):
        gen_eq = MathTex(
            r"Ua(x) \cdot Va(x) = 0",
        )
        self.play(Write(gen_eq))
        self.wait()

        interval = MathTex(
            r"x \in \{1, 2, 3\}",
        ).next_to(gen_eq, direction=DOWN)
        self.play(Write(interval))
        self.wait()

        # eq_1 = MathTex(
        #     r"Ua(1) \cdot Va(1) = 0",
        # )
        # self.play(ReplacementTransform(gen_eq, eq_1))
        # self.wait()

        # eq_2 = MathTex(
        #     r"Ua(2) \cdot Va(2) = 0",
        # )
        # self.play(ReplacementTransform(eq_1, eq_2))
        # self.wait()

        # eq_3 = MathTex(
        #     r"Ua(3) \cdot Va(3) = 0",
        # )
        # self.play(ReplacementTransform(eq_2, eq_3))
        # self.wait()

        # gen_eq = MathTex(
        #     r"Ua(x) \cdot Va(x) = 0",
        # )
        # self.play(ReplacementTransform(eq_3, gen_eq))
        # self.wait()

        self.remove(interval)
        self.play(gen_eq.animate.to_edge(UP))

        t_eq = MathTex(
            r"t(x) = (x - 1)(x - 2)(x - 3)",
        ).next_to(gen_eq, direction=DOWN)
        self.play(Write(t_eq))
        self.wait()

        product = MathTex(
            r"Ua(x) \cdot Va(x) = t(x) \cdot h(x)",
        ).next_to(t_eq, direction=DOWN)
        self.play(Write(product))
        self.wait()

        product_tau = MathTex(
            r"Ua(\tau) \cdot Va(\tau) = t(\tau) \cdot h(\tau)",
            # substrings_to_isolate=r"\tau"
        ).next_to(t_eq, direction=DOWN)
        product_tau[0][3].set_color(PINK)
        product_tau[0][9].set_color(PINK)
        product_tau[0][14].set_color(PINK)
        product_tau[0][19].set_color(PINK)
        self.play(ReplacementTransform(product, product_tau))
        self.wait()

        text = MathTex(
            r"\text{Trusted setup fixes }(\tau, T = t(\tau))",
        ).next_to(product_tau, direction=DOWN).set_color(PINK)
        self.play(Write(text))
        self.wait()

        final_check = MathTex(
            r"A \cdot B = T \cdot H",
        ).next_to(text, direction=DOWN)
        self.play(Write(final_check))
        self.wait()

        proof = MathTex(
            r"\text{Proof: }(A, B, H)",
        ).next_to(final_check, direction=DOWN).set_color(YELLOW)
        self.play(Write(proof))
        self.wait()

        verify = MathTex(
            r"\text{Verify: }A \cdot B \stackrel{?}{=} T \cdot H",
        ).next_to(proof, direction=DOWN).set_color(GREEN_D)
        self.play(Write(verify))
        self.wait()

        self.wait()