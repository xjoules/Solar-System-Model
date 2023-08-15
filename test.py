import pygame
import math

# Constants
G = 6.67430e-11  # Gravitational constant
earth_mass = 5.972e24  # Earth's mass in kg
moon_mass = 7.342e22  # Moon's mass in kg
earth_moon_distance = 3.844e8  # Earth-Moon distance in meters
earth_initial_velocity = math.sqrt(G * moon_mass / earth_moon_distance)  # Initial velocity of Earth
moon_initial_velocity = -math.sqrt(G * earth_mass / earth_moon_distance)  # Initial velocity of Moon

# Initialize pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Earth and Moon Simulation")
clock = pygame.time.Clock()

# Colors
blue = (0, 0, 255)
gray = (192, 192, 192)

# Celestial Body class
class CelestialBody:
    def __init__(self, mass, x, y, velocity):
        self.mass = mass
        self.x = x
        self.y = y
        self.velocity = velocity

    def update_position(self, time_step):
        self.x += self.velocity[0] * time_step
        self.y += self.velocity[1] * time_step

# Create Earth and Moon objects
earth = CelestialBody(earth_mass, screen_width // 2, screen_height // 2 - earth_moon_distance / 2, [0, earth_initial_velocity])
moon = CelestialBody(moon_mass, screen_width // 2, screen_height // 2 + earth_moon_distance / 2, [0, moon_initial_velocity])

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    dx = moon.x - earth.x
    dy = moon.y - earth.y
    distance = math.sqrt(dx ** 2 + dy ** 2)

    force_magnitude = (G * earth.mass * moon.mass) / (distance ** 2)
    acceleration = force_magnitude / moon.mass

    # Update velocities based on acceleration
    earth.velocity[1] += (acceleration * dy / distance) * 0.1
    moon.velocity[1] -= (acceleration * dy / distance) * 0.1

    earth.update_position(0.1)
    moon.update_position(0.1)

    pygame.draw.circle(screen, blue, (int(earth.x), int(earth.y)), 10)  # Draw Earth
    pygame.draw.circle(screen, gray, (int(moon.x), int(moon.y)), 5)  # Draw Moon

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
