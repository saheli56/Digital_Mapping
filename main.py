import pygame
import sys
import math
from earth import Earth
from satellite import Satellite
from car import Car
from mobile import Mobile
from school import School
from info_panel import InfoPanel
from animation_effects import RadiationWaves, ConnectionLines

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)  # More realistic sky color
GRASS_GREEN = (34, 139, 34)  # Forest green for grass
DARK_GRASS = (0, 100, 0)    # Darker green for grass texture
BROWN = (101, 67, 33)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Digital Mapping - Interactive Earth Scene")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game state
        self.earth_clicked = False
        self.show_info_panel = False
        self.info_text = ""
        
        # Initialize objects
        self.earth = Earth(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.satellite = None
        self.car = None
        self.mobile = None
        self.school = None
        self.info_panel = InfoPanel()
        self.radiation_waves = None
        self.connection_lines = None
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.handle_click(event.pos)
                    
    def handle_click(self, pos):
        # Check Earth click
        if self.earth.is_clicked(pos):
            if not self.earth_clicked:
                self.earth_clicked = True
                self.spawn_scene_elements()
            else:
                self.show_info_panel = True
                self.info_text = self.earth.get_info()
        
        # Check other elements if they exist
        if self.satellite and self.satellite.is_clicked(pos):
            self.show_info_panel = True
            self.info_text = self.satellite.get_info()
            
        if self.car and self.car.is_clicked(pos):
            self.show_info_panel = True
            self.info_text = self.car.get_info()
            
        if self.mobile and self.mobile.is_clicked(pos):
            self.show_info_panel = True
            self.info_text = self.mobile.get_info()
            
        if self.school and self.school.is_clicked(pos):
            self.show_info_panel = True
            self.info_text = self.school.get_info()
            
        # Check if clicking outside info panel to close it
        if self.show_info_panel:
            if not self.info_panel.is_clicked(pos):
                self.show_info_panel = False
                
    def spawn_scene_elements(self):
        """Spawn all scene elements when Earth is clicked"""
        # Create satellite high above Earth (topmost part)
        self.satellite = Satellite(self.earth.x, 80)
        
        # Create grassland (will be drawn in render method)
        
        # Create school on grassland
        self.school = School(200, SCREEN_HEIGHT - 150)
        
        # Create car at school
        self.car = Car(self.school.x + 50, self.school.y + 30)
        
        # Create mobile phone near the ground (on grassland)
        grass_y = self.earth.y + self.earth.radius + 50
        self.mobile = Mobile(SCREEN_WIDTH - 200, grass_y + 30)
        
        # Create radiation waves
        self.radiation_waves = RadiationWaves(self.satellite.x, self.satellite.y)
        
        # Create connection lines
        self.connection_lines = ConnectionLines()
        
    def update(self):
        # Update Earth rotation
        self.earth.update()
        
        if self.earth_clicked:
            # Update satellite
            if self.satellite:
                self.satellite.update()
                
            # Update car movement
            if self.car:
                self.car.update()
                
            # Update radiation waves
            if self.radiation_waves:
                self.radiation_waves.update(self.satellite.x, self.satellite.y)
                
            # Update connection lines
            if self.connection_lines and self.satellite and self.car and self.mobile:
                self.connection_lines.update(
                    (self.satellite.x, self.satellite.y),
                    (self.car.x, self.car.y),
                    (self.mobile.x, self.mobile.y)
                )
    
    def draw_grassland(self):
        """Draw realistic grassland below Earth"""
        grass_y = self.earth.y + self.earth.radius + 50
        pygame.draw.rect(self.screen, GRASS_GREEN, 
                        (0, grass_y, SCREEN_WIDTH, SCREEN_HEIGHT - grass_y))
        
        # Add realistic grass texture with varying heights and colors
        grass_colors = [DARK_GRASS, (46, 125, 50), (27, 94, 32)]
        for i in range(0, SCREEN_WIDTH, 8):
            # Vary grass height and color for realism
            grass_height = 8 + (i % 12)
            color_idx = (i // 8) % len(grass_colors)
            pygame.draw.line(self.screen, grass_colors[color_idx], 
                           (i, grass_y), (i, grass_y + grass_height), 2)
            pygame.draw.line(self.screen, grass_colors[color_idx], 
                           (i + 3, grass_y), (i + 3, grass_y + grass_height - 2), 1)
    
    def render(self):
        self.screen.fill(SKY_BLUE)  # Realistic sky background
        
        # Draw Earth
        self.earth.draw(self.screen)
        
        if self.earth_clicked:
            # Draw grassland
            self.draw_grassland()
            
            # Draw radiation waves first (behind satellite)
            if self.radiation_waves:
                self.radiation_waves.draw(self.screen)
            
            # Draw satellite
            if self.satellite:
                self.satellite.draw(self.screen)
                
            # Draw school
            if self.school:
                self.school.draw(self.screen)
                
            # Draw car
            if self.car:
                self.car.draw(self.screen)
                
            # Draw mobile
            if self.mobile:
                self.mobile.draw(self.screen)
                
            # Draw connection lines
            if self.connection_lines:
                self.connection_lines.draw(self.screen)
        
        # Draw info panel if needed
        if self.show_info_panel:
            self.info_panel.draw(self.screen, self.info_text)
            
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
