from manim import *

class FrameThree(Scene):
    def construct(self):
        condition_1_name = MathTex(
            r"\mathcal{C}_1: ",
        ).to_edge(UL)
        condition_2_name = MathTex(
            r"\mathcal{C}_2: ",
        ).next_to(condition_1_name, direction=DOWN)
        condition_3_name = MathTex(
            r"\mathcal{C}_3: ",
        ).next_to(condition_2_name, direction=DOWN)

        name_group = Group(condition_1_name, condition_2_name, condition_3_name)
        self.add(name_group)

        condition_1_u = MathTex(
            r"a_0",
        ).next_to(condition_1_name, direction=RIGHT)
        condition_2_u = MathTex(
            r"a_0",
        ).next_to(condition_2_name, direction=RIGHT)
        condition_3_u = MathTex(
            r"a_1",
        ).next_to(condition_3_name, direction=RIGHT)

        u_group = Group(condition_1_u, condition_2_u, condition_3_u)
        self.add(u_group)

        condition_1_dot = MathTex(
            r" \cdot ",
        ).next_to(condition_1_u, direction=RIGHT)
        condition_2_dot = MathTex(
            r" \cdot ",
        ).next_to(condition_2_u, direction=RIGHT)
        condition_3_dot = MathTex(
            r" \cdot ",
        ).next_to(condition_3_u, direction=RIGHT)

        dot_group = Group(condition_1_dot, condition_2_dot, condition_3_dot)
        self.add(dot_group)

        condition_2_v = MathTex(
            r"(a_0 - 1)",
        ).next_to(condition_2_dot, direction=RIGHT)
        condition_1_v = MathTex(
            r"a_1",
        ).next_to(condition_2_v, direction=UP)
        condition_3_v = MathTex(
            r"(a_1 - 1)",
        ).next_to(condition_3_dot, direction=RIGHT)

        v_group = Group(condition_1_v, condition_2_v, condition_3_v)
        self.add(v_group)

        condition_2_equal = MathTex(
            r" = 0",
        ).next_to(condition_2_v, direction=RIGHT)
        condition_1_equal = MathTex(
            r" = 0",
        ).next_to(condition_2_equal, direction=UP)
        condition_3_equal = MathTex(
            r" = 0",
        ).next_to(condition_3_v, direction=RIGHT)

        equal_group = Group(condition_1_equal, condition_2_equal, condition_3_equal)
        self.add(equal_group)

        self.wait()

        u_box_cond = SurroundingRectangle(u_group, corner_radius=0.2, color=GREEN, buff=SMALL_BUFF)
        self.play(Create(u_box_cond))

        v_box_cond = SurroundingRectangle(v_group, corner_radius=0.2, color=YELLOW, buff=SMALL_BUFF)
        self.play(Create(v_box_cond))
        self.wait()

        # U matrix

        u_r_1 = MathTex("1")
        u_r_2 = MathTex("2").next_to(u_r_1, direction=DOWN, buff=MED_SMALL_BUFF)
        u_r_3 = MathTex("3").next_to(u_r_2, direction=DOWN, buff=MED_SMALL_BUFF)
        u_r_group = Group(u_r_1, u_r_2, u_r_3).to_corner(DL, buff=LARGE_BUFF)
        
        u_eq_1 = MathTex(
            r"1 \cdot a_0 + 0 \cdot a_1 + 0 \cdot 1",
        ).next_to(u_r_1, direction=RIGHT, buff=MED_LARGE_BUFF)
        u_eq_2 = MathTex(
            r"1 \cdot a_0 + 0 \cdot a_1 + 0 \cdot 1",
        ).next_to(u_r_2, direction=RIGHT, buff=MED_LARGE_BUFF)
        u_eq_3 = MathTex(
            r"0 \cdot a_0 + 1 \cdot a_1 + 0 \cdot 1",
        ).next_to(u_r_3, direction=RIGHT, buff=MED_LARGE_BUFF)
        u_eq_group = Group(u_eq_1, u_eq_2, u_eq_3)
        u_column = MathTex("\quad a_0 \qquad a_1 \qquad 1 \quad").next_to(u_eq_group, direction=UP, buff=MED_SMALL_BUFF)
        u_group = Group(u_r_group, u_eq_group, u_column)
        u_box = SurroundingRectangle(u_group, corner_radius=0.2, color=GREEN, buff=MED_SMALL_BUFF)
        self.play(Create(u_box))
        self.wait()
        self.play(FadeIn(u_group))
        self.wait()
        u_group_first = Group(u_box, u_group)

        u_r_1 = MathTex("1")
        u_r_2 = MathTex("2").next_to(u_r_1, direction=DOWN, buff=MED_SMALL_BUFF)
        u_r_3 = MathTex("3").next_to(u_r_2, direction=DOWN, buff=MED_SMALL_BUFF)
        u_r_group = Group(u_r_1, u_r_2, u_r_3).to_corner(DL, buff=LARGE_BUFF)
        
        u_eq_1 = MathTex(
            r"1 \quad + 0 \quad + 0 \quad",
        ).next_to(u_r_1, direction=RIGHT, buff=MED_LARGE_BUFF)
        u_eq_2 = MathTex(
            r"1 \quad + 0 \quad + 0 \quad",
        ).next_to(u_r_2, direction=RIGHT, buff=MED_LARGE_BUFF)
        u_eq_3 = MathTex(
            r"0 \quad + 1 \quad + 0 \quad",
        ).next_to(u_r_3, direction=RIGHT, buff=MED_LARGE_BUFF)
        u_eq_group = Group(u_eq_1, u_eq_2, u_eq_3)
        u_column = MathTex("\quad a_0 \quad a_1 \quad 1 \quad").next_to(u_eq_group, direction=UP, buff=MED_SMALL_BUFF)
        u_group = Group(u_r_group, u_eq_group, u_column)
        u_box = SurroundingRectangle(u_group, corner_radius=0.2, color=GREEN, buff=MED_SMALL_BUFF)
        u_group_second = Group(u_box, u_group)
        self.play(Transform(u_group_first, u_group_second))
        self.wait()

        u_r_1 = MathTex("1")
        u_r_2 = MathTex("2").next_to(u_r_1, direction=DOWN, buff=MED_LARGE_BUFF)
        u_r_3 = MathTex("3").next_to(u_r_2, direction=DOWN, buff=MED_LARGE_BUFF)
        u_r_group = Group(u_r_1, u_r_2, u_r_3).to_corner(DL, buff=LARGE_BUFF)
        
        u_matrix = Matrix([[1, 0, 0], [1, 0, 0], [0, 1, 0]]).next_to(u_r_group, direction=RIGHT)
        u_column = MathTex("\quad a_0 \qquad a_1 \qquad 1 \quad").next_to(u_matrix, direction=UP, buff=MED_SMALL_BUFF)
        u_group = Group(u_r_group, u_matrix, u_column)
        u_matrix_box = SurroundingRectangle(u_group, corner_radius=0.2, color=GREEN, buff=MED_SMALL_BUFF)
        u_final = Group(u_matrix_box, u_group)
        
        self.remove(u_group_first)
        self.play(Transform(u_group_second, u_final))

        # V matrix

        v_r_1 = MathTex("1")
        v_r_2 = MathTex("2").next_to(v_r_1, direction=DOWN, buff=MED_SMALL_BUFF)
        v_r_3 = MathTex("3").next_to(v_r_2, direction=DOWN, buff=MED_SMALL_BUFF)
        v_r_group = Group(v_r_1, v_r_2, v_r_3).next_to(u_final, direction=RIGHT, buff=LARGE_BUFF)
        
        v_eq_1 = MathTex(
            r"0 \cdot a_0 + 1 \cdot a_1 + 0 \cdot 1",
        ).next_to(v_r_1, direction=RIGHT, buff=MED_LARGE_BUFF)
        v_eq_2 = MathTex(
            r"1 \cdot a_0 + 0 \cdot a_1 - 1 \cdot 1",
        ).next_to(v_r_2, direction=RIGHT, buff=MED_LARGE_BUFF)
        v_eq_3 = MathTex(
            r"0 \cdot a_0 + 1 \cdot a_1 - 1 \cdot 1",
        ).next_to(v_r_3, direction=RIGHT, buff=MED_LARGE_BUFF)
        v_eq_group = Group(v_eq_1, v_eq_2, v_eq_3)
        v_column = MathTex("\quad a_0 \qquad a_1 \qquad 1 \quad").next_to(v_eq_group, direction=UP, buff=MED_SMALL_BUFF)
        v_group = Group(v_r_group, v_eq_group, v_column)
        v_box = SurroundingRectangle(v_group, corner_radius=0.2, color=YELLOW, buff=MED_SMALL_BUFF)
        self.play(Create(v_box))
        self.wait()
        self.play(FadeIn(v_group))
        self.wait()
        v_group_first = Group(v_box, v_group)

        v_r_1 = MathTex("1")
        v_r_2 = MathTex("2").next_to(v_r_1, direction=DOWN, buff=MED_SMALL_BUFF)
        v_r_3 = MathTex("3").next_to(v_r_2, direction=DOWN, buff=MED_SMALL_BUFF)
        v_r_group = Group(v_r_1, v_r_2, v_r_3).next_to(u_final, direction=RIGHT, buff=LARGE_BUFF)
        
        v_eq_1 = MathTex(
            r"0 \quad + 1 \quad + 0 \quad",
        ).next_to(v_r_1, direction=RIGHT, buff=MED_LARGE_BUFF)
        v_eq_2 = MathTex(
            r"1 \quad + 0 \quad - 1 \quad",
        ).next_to(v_r_2, direction=RIGHT, buff=MED_LARGE_BUFF)
        v_eq_3 = MathTex(
            r"0 \quad + 1 \quad - 1 \quad",
        ).next_to(v_r_3, direction=RIGHT, buff=MED_LARGE_BUFF)
        v_eq_group = Group(v_eq_1, v_eq_2, v_eq_3)
        v_column = MathTex("\quad a_0 \quad a_1 \quad 1 \quad").next_to(v_eq_group, direction=UP, buff=MED_SMALL_BUFF)
        v_group = Group(v_r_group, v_eq_group, v_column)
        v_box = SurroundingRectangle(v_group, corner_radius=0.2, color=YELLOW, buff=MED_SMALL_BUFF)
        v_group_second = Group(v_box, v_group)
        self.play(Transform(v_group_first, v_group_second))
        self.wait()

        v_r_1 = MathTex("1")
        v_r_2 = MathTex("2").next_to(v_r_1, direction=DOWN, buff=MED_LARGE_BUFF)
        v_r_3 = MathTex("3").next_to(v_r_2, direction=DOWN, buff=MED_LARGE_BUFF)
        v_r_group = Group(v_r_1, v_r_2, v_r_3).next_to(u_final, direction=RIGHT, buff=LARGE_BUFF)
        
        v_matrix = Matrix([[0, 1, 0], [1, 0, -1], [0, 1, -1]]).next_to(v_r_group, direction=RIGHT)
        v_column = MathTex("\quad a_0 \qquad a_1 \qquad 1 \quad").next_to(v_matrix, direction=UP, buff=MED_SMALL_BUFF)
        v_group = Group(v_r_group, v_matrix, v_column)
        v_matrix_box = SurroundingRectangle(v_group, corner_radius=0.2, color=YELLOW, buff=MED_SMALL_BUFF)
        v_final = Group(v_matrix_box, v_group)
        
        self.remove(v_group_first)
        self.play(Transform(v_group_second, v_final))

        self.wait()
        self.remove(u_group_second, u_final, v_group_second)
        self.play(v_final.animate.to_edge(DL))
        self.play(FadeOut(u_box_cond))

        invisible = Rectangle().next_to(v_final, direction=UP, buff=MED_LARGE_BUFF)

        self.wait()
        rectangle = Rectangle(color=PURPLE, height=4.1, width=1).next_to(invisible, direction=DOWN).shift(RIGHT * 0.2)
        self.add(rectangle)
        self.wait()

        invisible = Rectangle().next_to(v_final, direction=UR, buff=LARGE_BUFF)
        equation = MathTex(
            r"v_2(x) = x^2 - 4x + 4",
        ).next_to(invisible, direction=DOWN, buff=LARGE_BUFF).set_color(PURPLE)
        self.play(Write(equation))
        self.wait()

        eq_1 = MathTex(
            r"v_2(1) = 1^2 - 4 \cdot 1 + 4 = 1",
        ).next_to(equation, direction=DOWN)
        eq_2 = MathTex(
            r"v_2(2) = 2^2 - 4 \cdot 2 + 4 = 0",
        ).next_to(eq_1, direction=DOWN)
        eq_3 = MathTex(
            r"v_2(3) = 3^2 - 4 \cdot 3 + 4 = 1",
        ).next_to(eq_2, direction=DOWN)
        eq_group = Group(eq_1, eq_2, eq_3)
        self.play(FadeIn(eq_group))
        self.wait()

        eq_1[0][15].set_color(PURPLE)
        eq_2[0][15].set_color(PURPLE)
        eq_3[0][15].set_color(PURPLE)
        
        v_matrix[0][1].set_color(PURPLE)
        v_matrix[0][4].set_color(PURPLE)
        v_matrix[0][7].set_color(PURPLE)

        self.wait()

        eq_1[0][3].set_color(ORANGE)
        eq_2[0][3].set_color(ORANGE)
        eq_3[0][3].set_color(ORANGE)

        v_r_1[0].set_color(ORANGE)
        v_r_2[0].set_color(ORANGE)
        v_r_3[0].set_color(ORANGE)

        self.wait()

        g = Group(equation, eq_group, rectangle)
        self.play(FadeOut(g))
        self.wait()

        v_r_1 = MathTex("1")
        v_r_2 = MathTex("2").next_to(v_r_1, direction=DOWN, buff=MED_LARGE_BUFF)
        v_r_3 = MathTex("3").next_to(v_r_2, direction=DOWN, buff=MED_LARGE_BUFF)
        v_r_group = Group(v_r_1, v_r_2, v_r_3).to_corner(DL, buff=LARGE_BUFF)

        v_matrix = Matrix([
            [r"0 \qquad", "v_2(1)", "0"], 
            [r"1 \qquad", "v_2(2)", "-1"], 
            [r"0 \qquad", "v_2(3)", "1"]]
        ).next_to(v_r_group, direction=RIGHT)
        v_column = MathTex("\quad a_0 \qquad a_1 \qquad 1 \quad").next_to(v_matrix, direction=UP, buff=MED_SMALL_BUFF)
        v_group_new = Group(v_r_group, v_matrix, v_column)
        v_matrix_box_new = SurroundingRectangle(v_group_new, corner_radius=0.2, color=YELLOW, buff=MED_SMALL_BUFF)
        self.play(ReplacementTransform(v_matrix_box, v_matrix_box_new))
        self.play(ReplacementTransform(v_group, v_group_new))
        self.wait()

        v_r_1 = MathTex("1")
        v_r_2 = MathTex("2").next_to(v_r_1, direction=DOWN, buff=MED_LARGE_BUFF)
        v_r_3 = MathTex("3").next_to(v_r_2, direction=DOWN, buff=MED_LARGE_BUFF)
        v_r_group = Group(v_r_1, v_r_2, v_r_3).to_corner(DL, buff=LARGE_BUFF)

        v_matrix_final = Matrix([
            ["v_1(1)", "v_2(1)", "v_3(1)"], 
            ["v_1(2)", "v_2(2)", "v_3(2)"], 
            ["v_1(3)", "v_2(3)", "v_3(3)"]]
        ).next_to(v_r_group, direction=RIGHT)
        v_column = MathTex("\qquad a_0 \qquad a_1 \qquad 1 \quad").next_to(v_matrix, direction=UP, buff=MED_SMALL_BUFF)
        v_group_final = Group(v_r_group, v_matrix_final, v_column)
        v_matrix_box_final = SurroundingRectangle(v_group_final, corner_radius=0.2, color=YELLOW, buff=MED_SMALL_BUFF)
        self.play(ReplacementTransform(v_matrix_box_new, v_matrix_box_final))
        self.play(ReplacementTransform(v_group_new, v_group_final))
        self.wait()

        g = Group(v_matrix_box_final, v_group_final)
        g.shift(UP * 1.1)
        self.wait()

        eq_1 = MathTex(
            r"v_1(x) = -1x^2 + 4x -3"
        )
        eq_2 = MathTex(
            r"v_2(x) = 1x^2 - 4x + 4",
        ).next_to(eq_1, direction=DOWN)
        eq_3 = MathTex(
            r"v_3(x) = \frac{1}{2}x^2 - \frac{5}{2}x + 2",
        ).next_to(eq_2, direction=DOWN)
        eq_group = Group(eq_1, eq_2, eq_3).next_to(v_matrix_box_new, direction=RIGHT).shift(UP)
        self.play(FadeIn(eq_group))
        self.wait()

        final_v_eq = MathTex(
            r"Va(x) = a_0 \cdot v_1(x) + a_1 \cdot v_2(x) + 1 \cdot v_3(x)"
        ).to_edge(DOWN).set_color(YELLOW).shift(UP * 0.3)
        self.play(Write(final_v_eq))
        self.wait()

        self.play(FadeIn(u_box_cond))
        self.wait()

        final_u_eq = MathTex(
            r"Ua(x) = a_0 \cdot u_1(x) + a_1 \cdot u_2(x) + 1 \cdot u_3(x)"
        ).next_to(final_v_eq, direction=DOWN).set_color(GREEN)
        self.play(Write(final_u_eq))
        self.wait()


