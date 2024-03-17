import pygame
import config
import sys
import os
pygame.init()

WIN = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
SPACESHIP = pygame.transform.scale(pygame.image.load(
                    os.path.join('Assets','spaceship_red.png')), (config.SPACESHIP_WIDTH,config.SPACESHIP_HEIGHT)
)
BACKGROUND = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(
                    os.path.join('Assets', 'space.png')), (config.HEIGHT,config.WIDTH)), 90
)

def draw_screen(player):
    WIN.fill(config.WIN_COLOR)
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(SPACESHIP,(player.x,player.y))

    pygame.display.update()

def player_movement(player, keys_pressed):
    if(keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and player.x - config.SPACESHIP_VEL >= 0:
        player.x -= config.SPACESHIP_VEL
    if(keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and player.x + player.width + config.SPACESHIP_VEL < config.WIDTH:
        player.x += config.SPACESHIP_VEL

def main():
    clock = pygame.time.Clock()
    run = True

    player = pygame.Rect(config.WIDTH/2 - config.SPACESHIP_WIDTH/2 ,config.HEIGHT - 100,config.SPACESHIP_WIDTH,config.SPACESHIP_HEIGHT)
    player_bullets = []

    while run:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        keys_pressed = pygame.key.get_pressed()
        player_movement(player, keys_pressed)
        draw_screen(player)

    
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()