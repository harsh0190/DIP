import cv2
import random
from utils.Constants import SPEED_INCREMENT, BALL_RADIUS, BALL_VEL, BALL_COLOR

class Ball:
    def __init__(self, x, y):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = BALL_RADIUS
        self.vel = BALL_VEL
        self.color = BALL_COLOR
        self.x_vel = BALL_VEL
        self.y_vel = -1*BALL_VEL

    #Making a ball
    def draw(self, frame):
        cv2.circle(frame, (int(self.x), int(self.y)),
        self.radius,self.color, -1)

    #Moving the ball
    def move(self,frame):
        self.x += self.x_vel
        self.y += self.y_vel
        self.draw(frame)

    #Increasing the speed of ball
    def increase_speed(self):
        self.x_vel *= SPEED_INCREMENT
        self.y_vel *= SPEED_INCREMENT

    #Resetting the score
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

        # Randomize direction at every reset
        choice = random.random()
        x_dir = 1 if choice < 0.5 else -1
        choice = random.random()
        y_dir = 1 if choice < 0.5 else -1

        self.x_vel = x_dir * self.vel 
        self.y_vel = y_dir * self.vel