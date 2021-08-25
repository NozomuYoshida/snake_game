from turtle import Turtle
import random

STARTING_POSITIONS = [(-160, 0), (-180, 0), (-200, 0)]
MOVE_DISTANCE = 20
INITIAL_SPEED = 2
GROWTH_SPEED = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.starting_positions = STARTING_POSITIONS
        self.velocity = INITIAL_SPEED
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position, color='white'):
        new_segment = Turtle('square')
        new_segment.color(color)
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self, color='white'):
        self.add_segment(self.segments[-1].position(), color)

    def increase_speed(self):
        self.velocity += GROWTH_SPEED
        for i in range(len(self.segments)):
            self.segments[i].speed(self.velocity)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[seg_num - 1].pos()
            self.segments[seg_num].setpos(new_position)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
