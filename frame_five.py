from manim import *

class FrameFive(Scene):
    def construct(self):
        prove = MathTex(
            r"\text{Prove }(a_0 = 0, a_1 = 1)",
        )
        self.play(Write(prove))
        self.play(prove.animate.to_edge(UP))
        self.wait()

        a = MathTex(
            r"a = [a_0 \text{ } a_1 \text{ } 1] = \text{[0 1 1]}",
        ).next_to(prove, direction=DOWN)
        self.play(Write(a))
        self.wait()        

        polys = MathTex(
            r"Ua(x) = \frac{1}{2} x^2 - \frac{3}{2} x + 1, \qquad Va(x) = \frac{3}{2} x^2 - \frac{13}{2} x + 6",
        ).next_to(a, direction=DOWN)
        self.play(Write(polys))
        self.wait()

        product = MathTex(
            r"Ua(x) \cdot Va(x) = \frac{3}{4} x^4 - \frac{11}{2} x^3 + \frac{57}{4} x^2 - \frac{31}{2} x + 6",
        ).next_to(polys, direction=DOWN)
        self.play(Write(product))
        self.wait()

        t = MathTex(
            r"t(x) = 0, x \in {1, 2, 3} \Rightarrow t(x) = (x - 1)(x - 2)(x - 3)",
        ).next_to(product, direction=DOWN)
        self.play(Write(t))
        self.wait()

        product_zero = MathTex(
            r"(Ua \cdot Va)(x) = 0, x \in \{1, 2, 3\}",
        ).next_to(t, direction=DOWN)
        self.play(Write(product_zero))
        self.wait()

        self.remove(prove, a,polys, product, t, product_zero)
        self.wait()

        frac = MathTex(
            r"\frac{Ua \cdot Va}{t(x)} = h(x)",
        )
        self.play(Write(frac))
        self.wait()
        self.play(frac.animate.to_edge(UP))
        self.wait()

        frac_updated = MathTex(
            r"\frac{\frac{3}{4} x^4 - \frac{11}{2} x^3 + \frac{57}{4} x^2 - \frac{31}{2} x + 6}{(x - 1)(x - 2)(x - 3)} = h(x)",
        ).to_edge(UP)

        self.play(TransformMatchingTex(frac, frac_updated))
        self.wait()

        frac_updated_bis = MathTex(
            r"\frac{\frac{3}{4} x^4 - \frac{11}{2} x^3 + \frac{57}{4} x^2 - \frac{31}{2} x + 6}{x^3 - 6 x^2 + 11 x - 6} = h(x)",
        ).to_edge(UP)

        self.play(TransformMatchingTex(frac_updated, frac_updated_bis))
        self.wait()

        frac_final = MathTex(
            r"\frac{3}{4} x - 1 = h(x)",
        ).to_edge(UP)

        self.play(TransformMatchingTex(frac_updated_bis, frac_final))
        self.wait()

        tau = MathTex(
            r"\text{Proof: }\tau \rightarrow A = Ua(\tau), B = Va(\tau), H = h(\tau)",
        ).next_to(frac_final, direction=DOWN)
        tau[0][6].set_color(PINK)
        tau[0][13].set_color(PINK)
        tau[0][21].set_color(PINK)
        tau[0][28].set_color(PINK)
        self.play(Write(tau))
        self.wait()

        verify = MathTex(
            r"\text{Verify: }A \cdot B \stackrel{?}{=} t(\tau) \cdot H",
        ).next_to(tau, direction=DOWN)
        verify[0][14].set_color(PINK)
        self.play(Write(verify))
        self.wait()

        pre_computed = MathTex(
            r"\text{Pre-computed trusted setup: } (\tau, T = t(\tau))",
        ).next_to(verify, direction=DOWN)
        pre_computed[0][26].set_color(PINK)
        pre_computed[0][32].set_color(PINK)
        self.play(Write(pre_computed))
        self.wait()

        self.wait()