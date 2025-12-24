
import pygame
pygame.init()
import random

width=1000
height=1000
blue=(0,0,255)
acua=(138, 43, 226)
red=(255,0,0)
white=(255,255,255)

#window
window = pygame.display.set_mode((width,height))
pygame.display.set_caption(('first_game'))

#carackter's parametrs

player_size = 30
player_x = width // 2 - player_size // 2 
player_y = height // 2 - player_size // 2
player_speed = 10

#carackter2's parametrs
player2_size=30
player2_x = width // 4 - player2_size
player2_y = width // 2 - player_size
player2_speed = 10

#bullet of player
bullet_width=10               
bullet_height=4
bullet_speed=20
bullets=[]



#enemey's  parameters

enemy_speed=10
enemy_size=20
enemy_x=random.randint(0,width - enemy_size)
enemy_y = 0


enemey2_size =30
enemy2_x = random.randint(0,width - enemey2_size)
enemy2_y = 0
enemy2_speed = 10
player2_fire_cooldown = 0 # otomatik ateş için timer
clock = pygame.time.Clock()
runing = True
while runing:
    clock.tick(60)
    for event in pygame.event.get():#bütün eventleri   ele aliyoruz
        if event.type == pygame.QUIT:
            runing = False
    #player move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        player_x = max(10,min(player_x,width-player_size - 10))
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        player_x = max(10,min(player_x,width-player_size - 10))
    if keys[pygame.K_UP]:
        player_y -= player_speed
        player_y = max(0,min(player_y,height-player_size)) 

    if keys[pygame.K_DOWN]:
        player_y += player_speed
        player_y = max(0,min(player_y,height-player_size))

    if random.randint(0,100) < 10:
        player2_direction = random.choice([-3,3])
        player2_x += player2_direction * player2_speed

        if player2_x <= 0:
            player2_x = 0
            player2_direction = 1

        elif player2_x >= width - player2_size:
            player2_x = width - player2_size
            player2_direction = -1   
 
    #bullets of player
    if keys[pygame.K_SPACE]:
        bullet_2x=player_x  - bullet_width // 2
        bullet_2y = player_y + player_size // 2 - bullet_height // 2

        bullet_x=player_x + player_size 
        bullet_y = player_y +  player_size // 2
       
        bullets.append(pygame.Rect(bullet_x,bullet_y,bullet_height,bullet_width))
        bullets.append(pygame.Rect(bullet_2x,bullet_2y,bullet_height,bullet_width))
    
    
    # bullets of player2
    if player2_fire_cooldown  == 0: 
        bullet_x = player2_x + bullet_width
        bullet_y = player2_y + bullet_width 
        bullets.append(pygame.Rect(bullet_x,bullet_y,bullet_width,bullet_height))  
        player2_fire_cooldown = 3
    else:
        player2_fire_cooldown -= 1
         
     
     #bullets  hareketi ve carpisma
    enemy_rect = pygame.Rect(enemy_x,enemy_y, enemy_size,enemy_size)
    enemy2_rect = pygame.Rect(enemy2_x,enemy2_y,enemey2_size,enemey2_size)   
    for bullet in bullets[:]:  
           bullet.y -= bullet_speed
           if bullet.y < 0:
            bullets.remove(bullet)

           elif bullet.colliderect(enemy_rect):
               bullets.remove(bullet)
               enemy_y = 0
               enemy_x = random.randint(0 , width - enemy_size)
           elif bullet.colliderect(enemy2_rect):
               bullets.remove(bullet)
               enemy2_y = 0
               enemy2_x = random.randint(0 , width - enemey2_size)     
                  

                
    
    enemy2_y += enemy2_speed
    if enemy2_y > height :
        enemy2_y = 0
        enemy2_x = random.randint(0,width-enemey2_size)


    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_y = 0    
        enemy_x = random.randint(0,width-enemy_size)    
  
    window.fill(white)
    pygame.draw.rect(window,blue,(player_x,player_y,player_size,player_size))
    pygame.draw.rect(window,red,(enemy_x,enemy_y,enemy_size,enemy_size))
    pygame.draw.rect(window,red,(player2_x,player2_y,player2_size,player2_size))
    pygame.draw.rect(window,acua,(enemy2_x,enemy2_y,enemey2_size,enemey2_size))
    for bullet in bullets: 
        pygame.draw.rect(window,red,bullet)

    pygame.display.update()
pygame.quit()