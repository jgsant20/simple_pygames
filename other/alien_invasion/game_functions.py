import sys
import pygame

from alien_invasion.bullet import Bullet
from alien_invasion.alien import Alien

def check_events(screen, settings, ship, bullets):
    """Checks responses from keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, screen, settings, ship, bullets):
    """Responds to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(screen, settings, ship, bullets)

def check_keyup_events(event, ship):
    """Responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_collision(aliens, bullets):
    for bullet in bullets:
        pygame.sprite.spritecollide(bullet, aliens, True)

def fire_bullet(screen, settings, ship, bullets):
    """Fires a bullet if limit not reached"""
    if len(bullets) < settings.bullets_allowed:
        # Creates a bullet object and adds it to bullets group
        new_bullet = Bullet(screen, settings, ship)
        bullets.add(new_bullet)

def remove_bullet(bullets):
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(settings, alien_width):
    """Determins number of aliens that can fit in a row"""
    available_space_x = settings.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_heigth):
    """Determines the number of rows of aliens that fit on the screen"""
    available_space_y = (settings.height - (3 * alien_heigth) - ship_height)
    number_rows = int(available_space_y / (2 * alien_heigth))
    return number_rows

def create_alien(screen, settings, alien_number, aliens, row_number):
    """Creates an alien"""
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien_height + row_number * alien_height * 2
    alien.x = alien.rect.x
    alien.y = alien.rect.y

    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height

    number_aliens_x = get_number_aliens_x(settings, alien_width)
    number_rows = get_number_rows(settings, ship_height, alien_height)

    # Create the first row of aliens
    for row_number in range(number_rows - 1):
        for alien_number in range(number_aliens_x - 1):
            # Create an alien and place it in the row
            create_alien(screen, settings, alien_number, aliens, row_number)

def check_fleet_edges(settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def update_aliens(settings, aliens):
    """Update the positions of all aliens in the fleet"""
    check_fleet_edges(settings, aliens)
    aliens.update()

def update_screen(settings, screen, ship, aliens, bullets):
    """Updates the screen's basic elements"""

    # bg
    screen.fill(settings.rgb_colors)

    # Redraws ship
    ship.blitme()

    # Redraws all aliens
    aliens.draw(screen)

    # Redraws all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Makes the screen visible
    pygame.display.flip()