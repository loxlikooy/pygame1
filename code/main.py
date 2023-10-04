# main.py
import pygame
import sys
from settings import *
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

# Create a restart button
restart_button = pygame.Rect(
    screen_width // 2 - 100,
    screen_height // 2 + 50,
    200,
    50
)
restart_font = pygame.font.Font(None, 36)
restart_text = restart_font.render("Restart", True, (255, 255, 255))
restart_text_rect = restart_text.get_rect(center=restart_button.center)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check for a mouse click on the restart button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if restart_button.collidepoint(event.pos):
                # Reset the game by creating a new level
                level = Level(level_map, screen)

    if not level.player.sprite.game_over:
        screen.fill('black')
        level.run()
    else:
        # Game over handling
        game_over_font = pygame.font.Font(None, 64)
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_text, game_over_rect)

        # Draw the restart button
        pygame.draw.rect(screen, (0, 0, 255), restart_button)
        screen.blit(restart_text, restart_text_rect)

    pygame.display.update()
    clock.tick(60)
