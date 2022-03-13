import sys
import pygame
import random

#Part 1 - Game setup
pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture_file, x, y, w, h, xspeed, yspeed):
        super().__init__()
        self.image = pygame.image.load(picture_file)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed    
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
    def draw(self, screen):
        screen.blit(self.image, [self.rect.x, self.rect.y])
score = 0
timer_counter = 0
timer = 15
character = GameSprite("EEVEE.png", 0, 0, 50, 50, 0, 0)
font = pygame.font.Font("YHA font _).ttf", 30)
score_text = font.render(f"Score: {score}", True, [0, 255, 0] )
timer_text = font.render(f"Time: {timer}", True, [0, 255, 0] )


#Part 2 - Game loop
while True:
    #Part 2.1 - Get user input
    event_list = pygame.event.get()
    
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and timer > 0:
            print(event)
            if character.rect.left <= event.pos[0] <= character.rect.right and character.rect.top <= event.pos[1] <= character.rect.bottom:
                score += 1
                score_text = font.render(f"Score: {score}", True, [0, 255, 0])

    #Part 2.2 - Update game data
    if timer>0:
        timer_counter +=1
        if timer_counter % 25 == 0:
            timer -= 1
            timer_text = font.render(f"Timer: {timer}", True, [0, 255, 255])

            character.rect.x = random.randint(0, 800 - character.rect.width)
            character.rect.y = random.randint(score_text.get_height(), 600 - character.rect.height)

    #Part 2.3 - Update the screen by drawing
    screen.fill([25, 50, 100])
    character.draw(screen)
    screen.blit(score_text, (0, 0))
    screen.blit(timer_text, (200, 0))

    pygame.display.update()
    clock.tick(25)
