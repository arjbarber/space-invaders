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

def draw_screen(player,player_bullets):
    WIN.fill(config.WIN_COLOR)
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(SPACESHIP,(player.x,player.y))

    for bullet in player_bullets:
        pygame.draw.rect(WIN,config.BULLET_COLOR,bullet)

    pygame.display.update()

def player_movement(player, keys_pressed):
    if(keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and player.x - config.SPACESHIP_VEL >= 0:
        player.x -= config.SPACESHIP_VEL
    if(keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and player.x + player.width + config.SPACESHIP_VEL < config.WIDTH:
        player.x += config.SPACESHIP_VEL

def handle_bullets(player_bullets,player):
    for bullet in player_bullets:
        bullet.y -= config.BULLET_VEL
        if bullet.y <= 0:
            player_bullets.remove(bullet)

def main():
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    run = True

    player = pygame.Rect(config.WIDTH/2 - config.SPACESHIP_WIDTH/2 ,config.HEIGHT - 100,config.SPACESHIP_WIDTH,config.SPACESHIP_HEIGHT)
    player_bullets = []

    while run:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE) and len(player_bullets) < config.MAX_BULLETS:
                    bullet = pygame.Rect(player.x + player.width/2, player.y, config.BULLET_WIDTH, config.BULLET_HEIGHT)
                    player_bullets.append(bullet)
        

        keys_pressed = pygame.key.get_pressed()
        player_movement(player, keys_pressed)
        draw_screen(player,player_bullets)
        handle_bullets(player_bullets,player)

    
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()