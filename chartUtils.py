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