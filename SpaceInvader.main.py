import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space wars")
background=pygame.image.load("Background.png")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
while True:
    screen.blit(background,(0,0))
    
    pygame.display.update()
    
    
if __name__ == '__main__':
    pass
    # import the main game file
