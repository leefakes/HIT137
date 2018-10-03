# Import module
import turtle


class DrawNumber():
    def __init__(self, size=100, width=20, x=0, y=0, colour="#000000"):
        # turn off draw mode
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.showturtle()
        # Prepare to draw
        self.turtle.pendown()
        # Begin the fill process.
        self.turtle.pencolor(colour)
        # self.turtle.begin_fill()

        self.size = size
        self.height = size
        self.width = width
        self.x_orig = x
        self.y_orig = y

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"size: {self.size}, width: {self.width}, "
                f"x: {self.x}, y: {self.y}) ")

    def end(self):
        # Raise pen and hide turtle
        self.turtle.penup()
        self.turtle.hideturtle()

    def design(self):
        """ Override this method """
        pass

    def draw(self):
        self.design()
        self.end()
        return (int(self.x_orig+(self.size*0.85)),
                self.y_orig,
                self.size,
                self.width)


class Zero(DrawNumber):
    def design(self):
        # Set dimensions
        t = self.turtle
        width = self.width
        t.pensize(width)
        t.penup()
        t.sety(t.ycor() + (width*1.5))
        # Draw a zero
        t.pendown()
        t.right(90)
        t.circle(width*1.5,180)
        t.forward(width)
        t.circle(width*1.5,180)
        t.forward(width)


class One(DrawNumber):
    def design(self):
        # Set dimensions
        t = self.turtle
        width = self.width
        height = self.height
        # Draw the one
        t.pensize(width)
        t.forward(width*3)
        t.backward(width*1.5)
        t.left(90)
        t.forward(height-width)
        t.left(135)
        t.forward(width*2)


class Two(DrawNumber):
    def design(self):
        # Start from bottom left of number
        t = self.turtle
        width = self.width
        t.pensize(width)
        # Draw base of 2
        t.forward(width*3)
        # Move to start of 2's arc
        t.penup()
        t.setposition(t.xcor() - ((width*3)*.9)/2, t.ycor() + ((width*3)*.9)/2)
        start_of_arc_coord = t.position()
        # Draw arc
        t.pendown()
        t.circle(((width*3)*.9)/2,270)
        # Move back to home position
        t.penup()
        t.setposition(self.x_orig, self.y_orig)
        # Draw left side of 2
        t.pendown()
        t.left(180)
        t.forward(width*0.5)
        t.setposition(start_of_arc_coord)


class Eight(DrawNumber):
    def design(self):
        # Start from bottom left of number
        t = self.turtle
        width = self.width
        t.pensize(width)
        # Position for bottom arc of 8
        t.penup()
        t.setposition(t.xcor()+width*1.5, t.ycor() + (width*2.125))
        t.pendown()
        t.circle(width*0.9)
        t.right(180)
        t.circle(width*1.125)


def draw_2018(size=100):
    """ Creates turtle canvas and draws the year 2018 """

    # Set starting position and number size
    width = size/5
    screen_width = (4*size)
    screen_height = size + width
    x = (0 - (screen_width/2) + (2 * width))
    y = (0 - (screen_height/2) + width)
    # Create window for turtle display
    canvas = turtle.Screen()
    canvas.title("Drawing the year 2018 - Click in the window to close")
    offset = 50  # Allowance for window title bar
    canvas.setup(screen_width, screen_height + offset)
    # The new starting position is passed back from the class instance
    x, y, size, width = Two(size=size, width=width,
                            x=x, y=y, colour="#aad4d4").draw()
    x, y, size, width = Zero(size=size, width=width,
                             x=x, y=y, colour="#efbbef").draw()
    x, y, size, width = One(size=size, width=width,
                            x=x, y=y, colour="#aad4d4").draw()
    x, y, size, width = Eight(size=size, width=width,
                              x=x, y=y, colour="#efbbef").draw()

    # Click on screen to close window
    canvas.exitonclick()

    return


# Execute main function
draw_2018(size=150)
