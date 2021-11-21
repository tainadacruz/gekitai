import pygame
from player import Player
from guess import Guess
from state import State

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 600])

state = State()

base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(350, 200, 50, 32)
button = pygame.Rect(375, 250, 50, 32)

player_1 = Player("Player 1", 10, 200, 400)
player_2 = Player("Player 2", 10, 550, 400)

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
BLACK = pygame.Color('black')
color = color_passive
  
active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                active = True
                state.execute(user_text)
                guess = Guess(state)
                print(user_text)
            else:
                active = False
    
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
      
    screen.fill((255, 255, 255))
  
    if active:
        color = color_active
    else:
        color = color_passive
          
    #pygame.draw.rect(screen, BLACK, player_1.rect)
    #pygame.draw.rect(screen, BLACK, player_2.rect)
    pygame.draw.rect(screen, "grey", input_rect)
    pygame.draw.rect(screen, color, button)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    send = base_font.render('   >', True, (255, 255, 255))
    player_message = base_font.render('Hidder, escolha o número de bolinhas:', True, (0,0,0)) #Mudar hidder/guesser de acordo com estado
      
    screen.blit(player_message, (200,150))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    screen.blit(send, button)

    input_rect.w = max(100, text_surface.get_width()+10)

    pygame.display.flip()
    clock.tick(60)


