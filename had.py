import pygame
from sys import exit
import random
pygame.init()


screen_height = 900
screen_width = 1500

screen = pygame.display.set_mode((screen_width, screen_height))



hodiny_bod = pygame.time.Clock()
hodiny_bod1 = pygame.time.Clock()

čas_bod = 0
čas_bod1 = 0

running = True

score = 0
evolution =0
super_evolution = 0


#TEN HAD
player_surf = pygame.image.load_extended("cell.png").convert_alpha()

player_surf = pygame.transform.rotozoom(player_surf, 0, 1)

player_x = 200
player_y = 200
player_speed = 6
had_hitbox = player_surf.get_rect(midbottom=(player_x, player_y))


#bodík
bod = pygame.image.load("bol.png").convert_alpha()
bod = pygame.transform.rotozoom(bod, 0, 0.02)

bod_x = 500
bod_y = 500

bod_hitbox = bod.get_rect(midbottom=(bod_x, bod_y))



bod1 = pygame.image.load("android17.png").convert_alpha()
bod1 = pygame.transform.rotozoom(bod1, 0, 0.5)

bod1_x = 600
bod1_y = 600

bod1_hitbox = bod1.get_rect(midbottom=(bod1_x, bod1_y))


#bod2 = pygame.image.load("android.png").convert_alpha()
#bod2 = pygame.transform.rotozoom(bod2, 0, 0.1)
#
#bod2_x = 600
#bod2_y = 600
#
#bod2_hitbox = bod2.get_rect(midbottom=(bod2_x, bod2_y))

font = pygame.font.Font("Bytesized-Regular.ttf", 25)

theme = pygame.mixer.Sound("bla-bla-bla-ble-ble-ble-blu-blu-blu.mp3")

theme.set_volume(0.1)




while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
       
    screen.fill("green")

    score_screen = font.render(f"Score: {score}", False, "#000000")
    screen.blit(score_screen, (screen_width-200, 30))
   
    čas_bod += hodiny_bod.get_time()
    čas_bod1 += hodiny_bod1.get_time()
     
    key = pygame.key.get_pressed()
   
    if key[pygame.K_w]:
         had_hitbox.top -= player_speed
    if key[pygame.K_a]:
         had_hitbox.left -= player_speed
    if key[pygame.K_s]:
         had_hitbox.bottom += player_speed
    if key[pygame.K_d]:
         had_hitbox.right += player_speed
     
    screen.blit(player_surf, had_hitbox)
    screen.blit(bod, bod_hitbox)
    screen.blit(bod1, bod1_hitbox)
    #screen.blit(bod2, bod2_hitbox)
    

    if had_hitbox.colliderect(bod_hitbox):
        score += 1
        bod_hitbox = bod.get_rect(midbottom=(3000, 3000))
        čas_bod = 0
   
    if bod_hitbox.midbottom ==(3000, 3000) and čas_bod > 100:
        random_x = random.randint(50, screen_width- 50)
        random_y = random.randint(50, screen_height -50)
        bod_hitbox = bod.get_rect(midbottom=(random_x, random_y))
       
   
   
       

    if had_hitbox.colliderect(bod1_hitbox):
        score += 100
        bod1_hitbox = bod1.get_rect(midbottom=(3000, 3000))
        čas_bod1 = 0
        evolution += 1
       
    if evolution > 1:
        player_surf = pygame.image.load_extended("semi.png").convert_alpha()

    if bod1_hitbox.midbottom ==(3000, 3000) and čas_bod1 > 3000:
        random1_x = random.randint(50, screen_width- 50)
        random1_y = random.randint(50, screen_height -50)
        bod1_hitbox = bod1.get_rect(midbottom=(random1_x, random1_y))
   
    if čas_bod1 > 6000:
        bod1_hitbox = bod1.get_rect(midbottom=(3000, 3000))
        čas_bod1 = 0
        if bod1_hitbox.midbottom ==(3000, 3000) and čas_bod1 > 3000:
            random1_x = random.randint(50, screen_width- 50)
            random1_y = random.randint(50, screen_height -50)
            bod1_hitbox = bod1.get_rect(midbottom=(random1_x, random1_y))

       
   

   
    print(čas_bod1)
    theme.play()
   
   
    hodiny_bod.tick(60)
    hodiny_bod1.tick(60)

    pygame.display.update()

       


#super_evolution = výhra (postupně evoluce)


#Gohan(enemák) když se ho dotkne = GAME OVER - spawn každý 2 sekundy a po 5(7) zmizí