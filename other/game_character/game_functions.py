import sys
import pygame

from game_character.bullet import Bullet


def check_events(screen, settings, ship, bullets):
    """Checks for events by user"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, settings, ship, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, screen, settings, ship, bullets):
    if event.key == pygame.K_LEFT:
        ship.left_movement_flag = True
    if event.key == pygame.K_RIGHT:
        ship.right_movement_flag = True
    if event.key == pygame.K_UP:
        ship.up_movement_flag = True
    if event.key == pygame.K_DOWN:
        ship.down_movement_flag = True
    if event.key == pygame.K_SPACE:
        create_bullet(screen, settings, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.left_movement_flag = False
    if event.key == pygame.K_RIGHT:
        ship.right_movement_flag = False
    if event.key == pygame.K_UP:
        ship.up_movement_flag = False
    if event.key == pygame.K_DOWN:
        ship.down_movement_flag = False


def create_bullet(screen, settings, ship, bullets):
    new_bullet = Bullet(screen, settings, ship)
    bullets.add(new_bullet)


def update_bullet(bullets):
    bullets.update()
    for bullet in bullets:
        bullet.draw()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(screen, ship, bullets, settings):
    """Renders the screen"""
    # draws screen
    screen.fill(settings.rgb_colors)
    ship.blitme()
    update_bullet(bullets)

    # updates display
    pygame.display.flip()
