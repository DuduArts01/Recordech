#library
import os, sys
import pygame, sys
from time import sleep

#import file
from outset import Outset
from button import Button

#init pygame
pygame.init()

#Dimension Window
width_window = 854
hight_window = 480

screen = pygame.display.set_mode([width_window, hight_window], pygame.RESIZABLE)

directory_main = os.path.dirname(__file__)
# Directory main

directory_outset = os.path.join(directory_main, "data/outset")
#directory outset

directory_button = os.path.join(directory_main, "data/button")
#directory button

    #load image and sprite
outset_image = pygame.image.load(os.path.join(directory_outset, "outset.png")).convert_alpha()
#outset image

three_risk_sprite_sheet = pygame.image.load(os.path.join(directory_button, "Three_risk/three_risk.png")).convert_alpha()
#button three risk

back_button_sprite_sheet = pygame.image.load(os.path.join(directory_button, "arrow/arrow_left.png")).convert_alpha()
#button back

game_button_sprite_sheet = pygame.image.load(os.path.join(directory_button, "game/game.png")).convert_alpha()
#button game


#Loop controller
mainLoop = True
outsetLoop = True
homeLoop = False
loginhomeLoop = False
memorygameLoop = False

if __name__ == "__main__":
    while mainLoop:
        '''Main Loop'''
        while outsetLoop:
            '''Outset'''
            screen.fill([255, 255, 255])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    outsetLoop = False
                    mainLoop = False

            outset = Outset(outset_image, (screen.get_width() / 2), (screen.get_height() / 2), 404, 708, 404, 708, (screen.get_width() / 2.5), (screen.get_height() / 1.5))

            outset.draw(screen)

            pygame.display.update()

            sleep(3)
            outsetLoop = False
            homeLoop = True

        three_risk_button = Button(three_risk_sprite_sheet, (screen.get_width() / 25), (screen.get_height() / 20), 40, 40, 40, 40, (screen.get_width() / 20), (screen.get_height() / 15))
            #three risk

        game_button = Button(game_button_sprite_sheet, (screen.get_width() / 2), (screen.get_height() / 2), 226, 270, 226, 270, (screen.get_width() / 15), (screen.get_height() / 10))
        #Button game

        while homeLoop:
            '''Home'''
            pygame.display.set_caption("RECORDECH (Home)")

            screen.fill([255, 255, 255])

            # color of display
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    homeLoop = False
                    mainLoop = False
                    # close window
                if event.type == pygame.VIDEORESIZE:
                    three_risk_button = Button(three_risk_sprite_sheet, (screen.get_width() / 25), (screen.get_height() / 20), 40, 40, 40, 40, (screen.get_width() / 20), (screen.get_height() / 15))
                    #three risk    
                    
                    game_button = Button(game_button_sprite_sheet, (screen.get_width() / 2), (screen.get_height() / 2), 226, 270, 226, 270, (screen.get_width() / 15), (screen.get_height() / 10))
        #Button game

            if three_risk_button.action:                
                loginhomeLoop = True
                sleep(0.3)
                homeLoop = False  
            
            if game_button.action:
                memorygameLoop = True
                sleep(0.3)
                homeLoop = False
            
            pygame.draw.rect(screen, [0, 98, 255], pygame.Rect(0, 0, (screen.get_width()), (screen.get_height() / 10)))
            #Draw a rectangle, i.e, it would be a top bar

            three_risk_button.draw(screen)

            game_button.draw(screen)

            pygame.display.update()
            # display update

        back_button = Button(back_button_sprite_sheet, (screen.get_width() / 40), (screen.get_height() / 20), 32, 15, 32, 15, (screen.get_width() / 25), (screen.get_height() / 20))
        #back button
        while loginhomeLoop:
            '''Login home'''
            pygame.display.set_caption("RECORDECH (User)")
            screen.fill([255, 255, 255])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loginhomeLoop = False
                    mainLoop = False
                    # close window
                if event.type == pygame.VIDEORESIZE:
                    back_button = Button(back_button_sprite_sheet, (screen.get_width() / 40), (screen.get_height() / 20), 32, 15, 32, 15, (screen.get_width() / 25), (screen.get_height() / 20))
            
            if back_button.action:                
                homeLoop = True
                sleep(0.3)
                loginhomeLoop = False
                
            
            pygame.draw.rect(screen, [0, 98, 255], pygame.Rect(0, 0, (screen.get_width() / 2.3), (screen.get_height())))
            #Rect would be background login

            back_button.draw(screen)

            pygame.display.update()
        while memorygameLoop:
            pygame.display.set_caption("RECORDECH (Memory Game)")

            screen.fill([255, 255, 255])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    memorygameLoop = False
                    mainLoop = False
                    # close window
                if event.type == pygame.VIDEORESIZE:
                    back_button = Button(back_button_sprite_sheet, (screen.get_width() / 40), (screen.get_height() / 20), 32, 15, 32, 15, (screen.get_width() / 25), (screen.get_height() / 20))
         
            if back_button.action:                
                homeLoop = True
                sleep(0.3)
                memorygameLoop = False
            
            back_button.draw(screen)

            pygame.display.update()
        

pygame.quit()
sys.exit()