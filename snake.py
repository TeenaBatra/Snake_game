from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.head = None
        self.snake = []

    def create_snake_body(self):
        for pos in STARTING_POSITION:
            # snake_body = Turtle()
            # snake_body.penup()
            # snake_body.color("white")
            # snake_body.shape("square")
            # snake_body.goto(self.x, 0)
            # self.snake.append(snake_body)
            # self.x -= 20
            self.add_snake_body_segment(pos)

    def add_snake_body_segment(self, position):
        snake_body = Turtle()
        snake_body.penup()
        snake_body.color("white")
        snake_body.shape("square")
        snake_body.goto(position)
        self.snake.append(snake_body)

        self.head = self.snake[0]

    def extend(self):
        self.add_snake_body_segment(self.snake[-1].position())

    def move(self):
        for sb in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[sb - 1].xcor()
            new_y = self.snake[sb - 1].ycor()
            self.snake[sb].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
