import pygame
from sys import *
import random

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

#music
zelda = pygame.mixer.Sound('a little lost woods.mp3')
chip = pygame.mixer.Sound('chip.mp3')
lose_song = pygame.mixer.Sound('while lesson.mp3')

lose_song.set_volume(.2)

chip.set_volume(.2)

jump_sound = pygame.mixer.Sound('jump.wav')
passed_sound = pygame.mixer.Sound('passed.wav')


jump_sound.set_volume(.11)

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('BOX JUMP')

box_area = [0,0,
            50,50]
box = pygame.rect.Rect(box_area)
box.bottom = 400

floor_area = [0,400,
              500,100]
floor = pygame.rect.Rect(floor_area)


fontPick = pygame.font.get_fonts()
font = pygame.font.SysFont(fontPick[5],30,False)
font2 = pygame.font.SysFont(fontPick[3],20,True)
font3 = pygame.font.SysFont(fontPick[10],50,True)


JUMP = pygame.K_SPACE
RESTART = pygame.K_r
EXIT = pygame.K_ESCAPE


### trying to remove 10 jumps from holding spacebar FIXED



clock = pygame.time.Clock()
def win(won):
    zelda.play()
    chip.stop()


    while won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill('black')
        keys = pygame.key.get_pressed()
        if keys[RESTART]:
            won = False
            main()
        if keys[EXIT]:
            won = False
            exit()
        winner_font = font.render("**YOU WON**",False,'white','black')
        winner_font2 = font.render("**'r' to restart**",False,'white','black')
        winner_font3 = font.render("**'esc' to exit**",False,'white','black')
        screen.blit(winner_font,[100,200])
        screen.blit(winner_font2,[100,250])
        screen.blit(winner_font3,[100,300])
        
        pygame.display.update()

def game_over(gameOver, v1,v2,v3,score):
    chip.stop()
    lose_song.play()
    

    while gameOver:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        if keys[RESTART]:
            main()
            
        screen.fill('lightblue')
        restart_font = font3.render(f"Score = {score}",False,[5,100,206])
        restart_font2 = font3.render(f"Press 'r' to Restart",False,[5,100,206])
        screen.blit(restart_font,[0,220])
        screen.blit(restart_font2,[0,270])
        pygame.draw.rect(screen,'red',box,0)
        pygame.draw.rect(screen,'yellow',floor,0)

        pygame.draw.polygon(screen,'black',[(v1,400),(v2,400),(v3,350)],0)

        pygame.display.update()

def main():

    lose_song.stop()
    zelda.stop()
    chip.play()

    v1 = 400 #initial
    v2 = 450 #initial + 50
    v3 = 425 #initial + 25

    count = 1 #used as a cooldown for jumps

    rate = .01 #used to speed up obstacles

    jumped_over_count = 0 #used to see how many triangles you jumped over

    run = True

    box.bottom = 400  

    player_color = "red"

    
    low = 1
    high = 10
    while run:

        #event handling start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        score = jumped_over_count * 50
        keys = pygame.key.get_pressed()
        
        rate = random.randrange(low,high)
        
        if keys[JUMP] or count < .99:
            if count > .99:
                print("jump")
                jump_sound.play()
                print(count)
                count = .50
                #box rising
            else:
                if count > .49 and count < .70: 
                    box.bottom -= 8
                if count > .70 and box.bottom < 400:
                    box.bottom += 10
                count += .01
                print(box.bottom)
                #box falling

        
        
        #event handling end

        #drawing block start
        screen.fill('blue')
        title_text = font.render("BOX JUMP GAME",False,"white",'gray')
        screen.blit(title_text,(150,50))
        
        

        pygame.draw.rect(screen,player_color,box,0)
        pygame.draw.rect(screen,'yellow',floor,0)
        controls_text = font2.render("'Spacebar to JUMP'",False,'black')
        screen.blit(controls_text,[100,450])
        if jumped_over_count < 5:
            pygame.draw.polygon(screen,'black',[(v1,400),(v2,400),(v3,350)],0)
            if box.collidepoint(v1,395):
                run = False
                game_over(True,v1,v2,v3,score)
            if box.collidepoint(v2,395):
                run = False
                game_over(True,v1,v2,v3,score)
            if box.collidepoint(v3,345):
                run = False
                game_over(True,v1,v2,v3,score)
        if jumped_over_count >= 5 and jumped_over_count < 10:
            pygame.draw.polygon(screen,'yellow',[(v1,400),(v2,400),(v3,310)],0)
            if box.collidepoint(v1,395):
                run = False
                game_over(True,v1,v2,v3,score)
            if box.collidepoint(v2,395):
                run = False
                game_over(True,v1,v2,v3,score)
            if box.collidepoint(v3,305):
                run = False
                game_over(True,v1,v2,v3,score)
        if jumped_over_count >= 10 and jumped_over_count < 25:
            pygame.draw.polygon(screen,'red',[(v1,400),(v2,400),(v3,350)],0)
            if box.collidepoint(v1,395):
                run = False
                game_over(True,v1,v2,v3,score)
            if box.collidepoint(v2,395):
                run = False
                game_over(True,v1,v2,v3,score)
            if box.collidepoint(v3,345):
                run = False
                game_over(True,v1,v2,v3,score)

        if jumped_over_count >= 25: #win condition
            win(True) 
        if jumped_over_count >= 1 and jumped_over_count < 10:
            player_color = "gray"
        if jumped_over_count >= 10 and jumped_over_count < 20:
            player_color = "purple"
        if jumped_over_count >= 20 and jumped_over_count < 25:
            player_color = "blue"
        if player_color == "blue":
            yikes_text = font2.render("Oh no! Good luck!",False,'red')
            screen.blit(yikes_text,[100,435])
        if player_color == "purple":
            low = -2
        if jumped_over_count >= 15:
            low = -2
            high = 2
        if v1 > -50 and v2 > -50 and v3 > -50:
            v1 -= 5 + rate
            v2 -= 5 + rate
            v3 -= 5 + rate
            print(rate)
        else:
            jumped_over_count += 1
            passed_sound.play()
            v1 = 500
            v2 = v1 + 50
            v3 = v1 + 25
            
            if rate > 15:
                rate = 12
        score_text = font2.render(f"Current Score! : {score}",False,'black')
        screen.blit(score_text,[100,415])
        # pygame.draw.line(screen,'white',[0,400],[5,400],5)

       

        #drawing block end


        pygame.display.update()
        clock.tick(60)
main()

