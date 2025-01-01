from manim import *
from manim import Point

from  utls import load_csv_data, returnnMonthAxisLabels, generate_increasing_numbers
import csv

CONFIG = {
    "camera_config":{"background_color": "#003399"}
} 

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.


def constructFlag(self):
    # Flag dimensions:
    # Width = 4 units
    # Height = 2.5 units
    # Ratio 2.5:4 is the same as 5:8
    width = 4
    height = 2.5
    
    # The top white stripe (half the height)
    top_stripe = Rectangle(
        width=width, 
        height=height/2
    ).set_fill(WHITE, 1).set_stroke(width=0)
    top_stripe.move_to(UP * height/4)  # Move up so it’s centered overall
    
    # The bottom red stripe (the other half)
    bottom_stripe = Rectangle(
        width=width, 
        height=height/2
    ).set_fill(RED, 1).set_stroke(width=0)
    bottom_stripe.move_to(DOWN * height/4) # Move down below the white stripe
    return (VGroup(top_stripe, bottom_stripe))    
        # Add the stripes to the scene  


def constructLogo():
    left_top = Polygon(
        [-2, 1, 0],  # top-left corner of logo
        [-1, 0, 0],  # left corner of diamond
        [ 0, 1, 0]   # top corner of diamond
    )
    
    left_bottom = Polygon(
        [-2,-1, 0],  # bottom-left corner of logo
        [-1, 0, 0],  # left corner of diamond
        [ 0,-1, 0]   # bottom corner of diamond
    )

    # Red shapes on the right side:
    left_side = Polygon(
        [ -2, 1, 0],  # top-right corner of logo
        [ -3, 0, 0],  # right corner of diamond
        [ -2, -1, 0]   # top corner of diamond
    )

    right_side = Polygon(
        [0,1,0],
        [0,-1,0],
        [1,0,0]
    )

    group=VGroup(left_top, left_bottom, left_side, right_side)
    return group


class TextExample(Scene):
    def construct(self):
        
        text = Text("MSS Poland IT", font="Arial", font_size=90,color=RED)
        svg = SVGMobject("/Users/marcin/projects/manim-ce/resources/tree.svg")
        svg.set_height(3)
        svg.to_edge(UP)
      #  self.play(DrawBorderThenFill(svg))
       
        self.play(Write(text))
        logo=constructLogo()
        logo.set_fill(RED, opacity=1)
        logo.set_stroke(RED, width=1)
        self.play(Transform(text, logo))
         
        self.play(text.animate.scale(0.3).to_corner(UL))
       
        text2=Text("People" ,font_size=50,color=WHITE)
        text2.next_to(text, RIGHT)
        line=Line(
            np.array((-7,text2.get_corner(DR)[1]-0.1,0)),
            np.array((7,text2.get_corner(DR)[1]-0.1,0)),
            stroke_color=[RED,RED,WHITE])
        
        
        
        self.play(Write(text2),Create(line))
        text4 = Text( "Converted 46 people \nincreasing perm to contractor ratio",
        font_size=30, color=WHITE,t2c={"46": YELLOW, "perm": YELLOW, "contractor": YELLOW})
class PieChart(Scene):
    def construct(self):       
        def draw_pie_chart(percentages, labels, fill_colors):
            # Ensure the percentages sum to 100
            assert sum(percentages) == 100, "Percentages must sum to 100"
            assert len(percentages) == len(fill_colors), "Each percentage must have a corresponding fill color"

            # Create the pie chart
            start_angle = 0
            slices = VGroup()
            label_texts = VGroup()
            for i, (percentage, label, color) in enumerate(zip(percentages, labels, fill_colors)):
                angle = percentage / 100 * 360
                wedge = AnnularSector(
                    inner_radius=0,
                    outer_radius=2,
                    angle=angle * DEGREES,
                    start_angle=start_angle * DEGREES,
                    fill_color=color,
                    fill_opacity=0.8,
                    stroke_color=WHITE,
                    stroke_width=2
                )
                slices.add(wedge)
                start_angle += angle

            # Add label and percentage annotation
                label_text = Text(f"{label}: {percentage}%", font_size=24, color=WHITE)
                label_text.move_to(wedge.get_center())
                label_texts.add(label_text)
            
            return slices, label_texts
        
        
        slices, labels = draw_pie_chart([30, 20, 25, 25], ["A", "B", "C", "D"], [BLUE, GREEN, RED, YELLOW])
        self.add(labels)
        self.play(Create(slices))
     

class AnimatedBar(Scene):    
    def create_animated_bar(startPercent, targetPercent, totalWidth):
        rect1 = Rectangle(width=totalWidth * startPercent, height=1).set_stroke(BLUE, width=5)
        rect2 = Rectangle(width=totalWidth * (1 - startPercent), height=1).set_stroke(GREEN, width=5)
        rect1.next_to(rect2, RIGHT, buff=0)

        number_rect1 = DecimalNumber(0, font_size=36, color=BLUE, unit="  \% ", num_decimal_places=1)
        def update_number(mob):
            mob.set_value((rect1.get_width() / totalWidth) * 100)
            mob.move_to(rect1.get_center())
        number_rect1.add_updater(update_number)

        number_rect2 = DecimalNumber(0, font_size=36, color=BLUE, unit="  \% ", num_decimal_places=1)
        def update_number2(mob):
            mob.set_value((rect2.get_width() / totalWidth) * 100)
            mob.move_to(rect2.get_center())
        number_rect2.add_updater(update_number2)

        return rect1, rect2, number_rect1, number_rect2

    def construct(self):
        startPercent = 0.3
        targetPercent = 0.6
        totalWidth = 4

        rect1, rect2, number_rect1, number_rect2 = create_animated_bar(startPercent, targetPercent, totalWidth)

        self.play(FadeIn(rect1, rect2, number_rect1, number_rect2))
        self.play(
            rect2.animate.stretch_to_fit_width((totalWidth * targetPercent), about_edge=LEFT),
            rect1.animate.stretch_to_fit_width(totalWidth * (1 - targetPercent), about_edge=RIGHT),
            run_time=3
        )
        self.wait(3)
   
        
        self.play(FadeIn(rect1,rect2,number_rect1,number_rect2))
        
        self.play(

            rect2.animate.stretch_to_fit_width((totalWidth*targetPercent), about_edge=LEFT),
            rect1.animate.stretch_to_fit_width(totalWidth*(1-targetPercent), about_edge=RIGHT),
            
            run_time=3
        )
        self.wait(3)

class AnimateBlocks(Scene):
    def construct(self):
        line=Line(LEFT,RIGHT,stroke_color=[BLUE,RED,BLUE])
        self.play(Create(line))
        blocks = VGroup(*[Rectangle(width=0.1,height=0.5)
        .set_stroke(BLUE if x <10  else RED,width=1,opacity=1)
         for x in range(20)])
        blocks.arrange(RIGHT, buff=0.1)
        self.play(FadeIn(blocks))
        self.wait(3)
    
class PeopleAsDots(Scene):
    def construct(self):
        people = VGroup(*[Dot(radius=0.05) for x in range(250)])
        people.arrange_in_grid(25,10,buff=0.1)
        people.to_edge(LEFT)
        self.play(GrowFromPoint(people,ORIGIN))
        self.wait(3)
        more_people = VGroup(*[Dot(radius=0.05) for x in range(10)])
        more_people.arrange_in_grid(1, 10, buff=0.1)
        more_people.next_to(people, DOWN, buff=0.1)
        self.play(Create(more_people))
        self.wait(3)

class PeopleAsGraph(Scene):
    def construct(self):
        data=load_csv_data("/Users/marcin/projects/manim-ce/data/output.csv")
   
        axes = Axes(
            x_range=[0, 35, 3],
            y_range=[100, 600, 50],
            axis_config={"color": BLUE},
            
        
        )

        axes.get_axes()[0].add_labels(returnnMonthAxisLabels(35))
        axes_labels = axes.get_axis_labels( y_label="Headcount")
     
        def linear(x):
            print (x,data[int(x)] ) 
            return data[int(x)]         
        graph = axes.plot(linear, color=YELLOW, use_smoothing=False)
               
      
        # graph_label = axes.get_graph_label(graph, label="2x + 1")

        self.play(FadeIn(axes,axes_labels),run_time=1)# type: ignore
        self.play(Create(graph)) 
        self.wait()
class GraphWithTracingDot(Scene):
    def construct(self):
        # Create a red dot
        dot = Dot(color=RED).move_to(ORIGIN)

        # Add the dot to the scene
        self.add(dot)

        # Play the jumping animation in a loop
        for _ in range(3):  # Dot jumps up and down 3 times
            self.play(dot.animate.move_to(UP * 2).set_rate_func(rate_functions.ease_in_out_quad), run_time=0.5)  # Jump up
            self.play(dot.animate.move_to(ORIGIN).set_rate_func(rate_functions.ease_in_out_quad), run_time=0.5)  # Jump down

class DotBezier(Scene):
    def construct(self):
        spiral = ParametricFunction(
            lambda t: np.array([
                t * np.cos(t),
                t * np.sin(t),
                0
            ]),
            t_range=np.array([0, 4 * PI, 0.01]),
            color=BLUE
        )
        dot = Dot(spiral.get_start(), color=RED)

        self.play(Create(spiral))
        self.play(MoveAlongPath(dot, spiral), run_time=8)
        self.wait()
    
class AnimatingMethods(Scene):
    def construct(self):
        grid = Tex(r"\pi").get_grid(10, 10, height=4)
        self.add(grid)

        # You can animate the application of mobject methods with the
        # ".animate" syntax:
        self.play(grid.animate.shift(LEFT))

        # Both of those will interpolate between the mobject's initial
        # state and whatever happens when you apply that method.
        # For this example, calling grid.shift(LEFT) would shift the
        # grid one unit to the left, but both of the previous calls to
        # "self.play" animate that motion.

        # The same applies for any method, including those setting colors.
        self.play(grid.animate.set_color(YELLOW))
        self.wait()
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        # The method Mobject.apply_complex_function lets you apply arbitrary
        # complex functions, treating the points defining the mobject as
        # complex numbers.
        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()

        # Even more generally, you could apply Mobject.apply_function,
        # which takes in functions form R^3 to R^3
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]),
                    p[1] + 0.5 * math.sin(p[0]),
                    p[2]
                ]
            ),
            run_time=5,
        )
        self.wait()



class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # Passing in muliple arguments to Tex will result
            # in the same expression as if those arguments had
            # been joined together, except that the submobject
            # hierarchy of the resulting mobject ensure that the
            # Tex mobject has a subject corresponding to
            # each of these strings.  For example, the Tex mobject
            # below will have 5 subjects, corresponding to the
            # expressions [A^2, +, B^2, =, C^2]
            Tex("A^2", "+", "B^2", "=", "C^2"),
            # Likewise here
            Tex("A^2", "=", "C^2", "-", "B^2"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So the line below is equivalent
            # to the commented out line below it.
            Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        # Now, we could try this again on the next line...
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()
        # ...and this looks nice enough, but since there's no tex
        # in lines[2] which matches "C^2" or "B^2", those terms fade
        # out to nothing while the C and B terms fade in from nothing.
        # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # we can specify that with a key map.
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # And to finish off, a simple TransformMatchingShapes would work
        # just fine.  But perhaps we want that exponent on A^2 to transform into
        # the square root symbol.  At the moment, lines[2] treats the expression
        # A^2 as a unit, so we might create a new version of the same line which
        # separates out just the A.  This way, when TransformMatchingTex lines up
        # all matching parts, the only mismatch will be between the "^2" from
        # new_line2 and the "\sqrt" from the final line.  By passing in,
        # transform_mismatches=True, it will transform this "^2" part into
        # the "\sqrt" part.
        new_line2 = Tex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE_E, 1)

        # On all frames, the constructor Brace(square, UP) will
        # be called, and the mobject brace will set its data to match
        # that of the newly constructed object
        brace = always_redraw(Brace, square, UP)

        text, number = label = VGroup(
            Text("Width = "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=2,
                include_sign=True,
            )
        )
        label.arrange(RIGHT)

        # This ensures that the method deicmal.next_to(square)
        # is called on every frame
        always(label.next_to, brace, UP)
        # You could also write the following equivalent line
        # label.add_updater(lambda m: m.next_to(brace, UP))

        # If the argument itself might change, you can use f_always,
        # for which the arguments following the initial Mobject method
        # should be functions returning arguments to that method.
        # The following line ensures thst decimal.set_value(square.get_y())
        # is called every frame
        f_always(number.set_value, square.get_width)
        # You could also write the following equivalent line
        # number.add_updater(lambda m: m.set_value(square.get_width()))

        self.add(square, brace, label)

        # Notice that the brace and label track with the square
        self.play(
            square.animate.scale(2),
            rate_func=there_and_back,
            run_time=2,
        )
        self.wait()
        self.play(
            square.animate.set_width(5, stretch=True),
            run_time=3,
        )
        self.wait()
        self.play(
            square.animate.set_width(2),
            run_time=3
        )
        self.wait()

        # In general, you can alway call Mobject.add_updater, and pass in
        # a function that you want to be called on every frame.  The function
        # should take in either one argument, the mobject, or two arguments,
        # the mobject and the amount of time since the last frame.
        now = self.time
        w0 = square.get_width()
        square.add_updater(
            lambda m: m.set_width(w0 * math.sin(self.time - now) + w0)
        )
        self.wait(4 * PI)


class CoordinateSystemExample(Scene):
    def construct(self):
        axes = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-1, 10),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-2, 2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            height=6,
            width=10,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        # Keyword arguments of add_coordinate_labels can be used to
        # configure the DecimalNumber mobjects which it creates and
        # adds to the axes
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

        # Axes descends from the CoordinateSystem class, meaning
        # you can call call axes.coords_to_point, abbreviated to
        # axes.c2p, to associate a set of coordinates with a point,
        # like so:
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        self.wait()

        # Similarly, you can call axes.point_to_coords, or axes.p2c
        # print(axes.p2c(dot.get_center()))

        # We can draw lines from the axes to better mark the coordinates
        # of a given point.
        # Here, the always_redraw command means that on each new frame
        # the lines will be redrawn
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()

        # If we tie the dot to a particular set of coordinates, notice
        # that as we move the axes around it respects the coordinate
        # system defined by them.
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.75).to_corner(UL),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))

        # Other coordinate systems you can play around with include
        # ThreeDAxes, NumberPlane, and ComplexPlane.


class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=False,
            color=YELLOW,
        )
        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.
        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],
            color=GREEN,
        )

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(relu_graph, step_graph),
            FadeTransform(relu_label, step_label),
        )
        self.wait()

        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(
            FadeOut(step_graph),
            FadeOut(step_label),
            ShowCreation(parabola)
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()


class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)
        # You can texture a surface with up to two images, which will
        # be interpreted as the side towards the light, and away from
        # the light.  These can be either urls, or paths to a local file
        # in whatever you've set as the image directory in
        # the custom_config.yml file

        # day_texture = "EarthTextureMap"
        # night_texture = "NightEarthTextureMap"
        day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"
        night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"

        surfaces = [
            TexturedSurface(surface, day_texture, night_texture)
            for surface in [sphere, torus1, torus2]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        # Set perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3),
        )
        for mob in surfaces:
            mob.add(mob.mesh)
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2)
        for mob in surfaces[1:]:
            mob.rotate(PI / 2)

        self.play(
            Transform(surface, surfaces[1]),
            run_time=3
        )

        self.play(
            Transform(surface, surfaces[2]),
            # Move camera frame during the transition
            frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES),
            run_time=3
        )
        # Add ambient rotation
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

        # Play around with where the light is
        light_text = Text("You can move around the light source")
        light_text.move_to(surface_text)
        light_text.fix_in_frame()

        self.play(FadeTransform(surface_text, light_text))
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.animate.move_to(3 * IN), run_time=5)
        self.play(light.animate.shift(10 * OUT), run_time=5)

        drag_text = Text("Try moving the mouse while pressing d or f")
        drag_text.move_to(light_text)
        drag_text.fix_in_frame()

        self.play(FadeTransform(light_text, drag_text))
        self.wait()


class InteractiveDevelopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        # This opens an iPython terminal where you can keep writing
        # lines as if they were part of this construct method.
        # In particular, 'square', 'circle' and 'self' will all be
        # part of the local namespace in that terminal.
        self.embed()

        # Try copying and pasting some of the lines below into
        # the interactive shell
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEGREES))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
            In general, using the interactive shell
            is very helpful when developing new scenes
        """)
        self.play(Write(text))

        # In the interactive shell, you can just type
        # play, add, remove, clear, wait, save_state and restore,
        # instead of self.play, self.add, self.remove, etc.

        # To interact with the window, type touch().  You can then
        # scroll in the window, or zoom by holding down 'z' while scrolling,
        # and change camera perspective by holding down 'd' while moving
        # the mouse.  Press 'r' to reset to the standard camera position.
        # Press 'q' to stop interacting with the window and go back to
        # typing new commands into the shell.

        # In principle you can customize a scene to be responsive to
        # mouse and keyboard interactions
        always(circle.move_to, self.mouse_point)


class ControlsExample(Scene):
    def setup(self):
        self.textbox = Textbox()
        self.checkbox = Checkbox()
        self.color_picker = ColorSliders()
        self.panel = ControlPanel(
            Text("Text", font_size=24), self.textbox, Line(),
            Text("Show/Hide Text", font_size=24), self.checkbox, Line(),
            Text("Color of Text", font_size=24), self.color_picker
        )
        self.add(self.panel)

    def construct(self):
        text = Text("text", font_size=96)

        def text_updater(old_text):
            assert(isinstance(old_text, Text))
            new_text = Text(self.textbox.get_value(), font_size=old_text.font_size)
            # new_text.align_data_and_family(old_text)
            new_text.move_to(old_text)
            if self.checkbox.get_value():
                new_text.set_fill(
                    color=self.color_picker.get_picked_color(),
                    opacity=self.color_picker.get_picked_opacity()
                )
            else:
                new_text.set_opacity(0)
            old_text.become(new_text)

        text.add_updater(text_updater)

        self.add(MotionMobject(text))

        self.textbox.set_value("Manim")
        # self.wait(60)
        # self.embed()


# See https://github.com/3b1b/videos for many, many more
