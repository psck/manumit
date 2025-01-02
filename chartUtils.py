from manim import *
#Create 2 rectangles with different colors and a number that shows the percentage of the first rectangle

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
        label_angle = (start_angle - angle / 2) * DEGREES
        label_radius = 2.5  # Slightly outside the wedge
        label_text.move_to([label_radius * np.cos(label_angle), label_radius * np.sin(label_angle), 0])
        label_texts.add(label_text)
    return slices, label_texts
        
def divide_rectangle(percentages, totalWidth, height=1):
    assert sum(percentages) == 100, "Percentages must sum to 100"
    
    rectangles = VGroup()
    current_x = -totalWidth / 2  # Start from the left edge

    for percentage in percentages:
        width = totalWidth * (percentage / 100)
        rect = Square(side_length=width).set_stroke(WHITE, width=2)
        rect.move_to([current_x + width / 2, 0, 0])  # Center the square
        height = totalWidth  # Ensure the height is the same as the width for a square
        rect = Rectangle(width=width, height=height).set_stroke(WHITE, width=2)
        rect.move_to([current_x + width / 2, 0, 0])  # Center the rectangle
        rectangles.add(rect)
        current_x += width  # Move to the next position

    return rectangles
def draw_coordinate_system(x_range, y_range, x_step=1, y_step=1):
    numberplane = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=abs(x_range[1] - x_range[0]),
        y_length=abs(y_range[1] - y_range[0]),
        axis_config={"include_numbers": True},
        background_line_style={
            "stroke_color": BLUE_D,
            "stroke_width": 1,
            "stroke_opacity": 0.6
        }
    )
    return numberplane

def Dots(number,radius=0.05,color=WHITE,grid_x=25,grid_y=10, buff=0.1):
    people = VGroup(*[Dot(radius=0.05,color=color) for x in range(250)])
    people.arrange_in_grid(25,10,buff=0.1)
    return people

class TestDots(Scene):
    def construct(self):
        dots = Dots(250)
        self.play(Create(dots))
        first20Dots=VGroup(*dots[:20])
        endPoint=dots.get_bottom()
        
        self.play(first20Dots.animate.set_color(RED), run_time=1)
        self.play(first20Dots.animate.shift(RIGHT*2))
        arc_path = ArcBetweenPoints(
            start=first20Dots.get_center(),
            end=endPoint+DOWN*((first20Dots.height/2)+0.1),angle=-PI*1)
        self.add(arc_path)
        self.play(MoveAlongPath(first20Dots, arc_path), run_time=2)

class TestCoordinateSystem(Scene):
    def construct(self):
        coordinate_system = draw_coordinate_system([-10, 10],[ -5, 5])
        self.play(Create(coordinate_system))

class TestRectangle(Scene):
     def construct(self):
        rectangle=divide_rectangle([20, 30, 39,10,1], 1,1)
        self.play(Create(rectangle))

class TestPie(Scene):
    def construct(self):
        slices,text=draw_pie_chart([20, 30, 39,10,1], ["A", "B", "C", "D", "E"], [BLUE, GREEN, RED, YELLOW, PURPLE])
        self.play(Create(slices), Write(text))