#Guided project to learn how pygame works and to create the iconic snake game
#Library for game functions
import pygame
#Library for time
import time
#Library for random generator
import random

#Begins game
pygame.init()

#RBG values for colors
white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Dimensions of window
dis_width = 600
dis_height = 400

#Display of window
dis = pygame.display.set_mode((dis_width,dis_height))
#Title of window
pygame.display.set_caption("Snake game by Uruj")

#Setting up fps
clock = pygame.time.Clock()

#Size+speed of block
snake_block = 10
snake_speed = 15

#Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#Function for keeping score
def Your_score(score):
    value = score = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

#Function to draw snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black,[x[0],x[1],snake_block,snake_block])

#Function to present message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

#Function for game logic
def gameLoop():
    game_over = False
    game_close = False

    #Starting position of snake
    x1 = dis_width/2
    y1 = dis_width/2

    #Change in position of snake
    x1_change = 0
    y1_change = 0

    #List to render snake
    snake_list = []
    Length_of_snake = 1
    #Random generation of food
    foodx = round(random.randrange(0,dis_width - snake_block)/10.0)*10
    foody = round(random.randrange(0,dis_height - snake_block)/10.0)*10


    #Logic to end game
    while not game_over:

        while game_close:
            dis.fill(red)
            message("You Lost! Press Q-Quit or C-Play", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #Logic for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #Logic if you eat yourself
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 <0:
            game_close = True
        #Position movement
        x1 += x1_change
        y1 += y1_change
        #Background color
        dis.fill(white)
        #Rendering food
        pygame.draw.rect(dis,red,[foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list)>Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x== snake_Head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(Length_of_snake-1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_width - snake_block)/10.0)*10
            foody = round(random.randrange(0,dis_height - snake_block)/10.0)*10
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
