import time
from tracemalloc import start
import pygame

width = 1200
height = 600

class Wall:

    def __init__(self, s_width, s_height) -> None:
        self.rect = pygame.Rect(int(s_width)-20, 0, 20, int(s_height))

        

    def draw_rect(self, screen, color):
        self.wall = pygame.draw.rect(screen, color, self.rect)

    def collision(self):
        pass

class Ball:

    def __init__(self, size, start_height, start_width) -> None:
        self.rect = pygame.Rect(int(start_width-0.5*size), int(start_height+0.5*size), size, size)

    def draw_rect(self, screen, color):
        self.ball = pygame.draw.rect(screen, color, self.rect)

    def move(self, direction, speed, screen, color):
        new_x = direction[0] * speed
        new_y = direction[1] * speed
        self.ball.move(new_x, new_y)
    

class Player:

    def __init__(self, left, top) -> None:
        self.rect = pygame.Rect(left, top-10, 20, 100)
    
    def draw_rect(self, screen, color):
        self.player = pygame.draw.rect(screen, color, self.rect)

    def move_player(self, direction, speed):
        pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong!")

    player_color = (220,220,220) #grayish

    oponent = Wall(width, height)
    oponent.draw_rect(screen, player_color)

    ball = Ball(20, height/2, width/2)
    ball.draw_rect(screen, player_color)

    player = Player(0, int(height/2))
    player.draw_rect(screen, player_color)

    start_time = time.time()
    time_delta = 0.1
    movement_speed = 5
    movement_direction = (1,0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        current_time = time.time()
        if current_time > start_time + time_delta:
            ball.move(movement_direction, movement_speed)


        pygame.display.flip()
            #elif event.type == 









if __name__=="__main__":
    main()