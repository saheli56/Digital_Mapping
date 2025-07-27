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
        if self.earth.is_clicked(pos) and self.earth.visible:
            if not self.earth_clicked:
                self.earth_clicked = True
                self.spawn_scene_elements()
                # Make Earth disappear after spawning scene elements
                self.earth.visible = False
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
        """Draw realistic grassland below Earth with flowers and design elements"""
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
        
        # Add flowers scattered across the grassland
        self.draw_flowers(grass_y)
        
        # Add bushes and small plants
        self.draw_bushes(grass_y)
        
        # Add small rocks and pebbles
        self.draw_rocks(grass_y)
        
        # Add dandelions and wildflowers
        self.draw_wildflowers(grass_y)
    
    def draw_flowers(self, grass_y):
        """Draw colorful flowers scattered across the grassland"""
        flower_colors = [
            (255, 105, 180),  # Hot pink
            (255, 165, 0),    # Orange
            (255, 255, 0),    # Yellow
            (138, 43, 226),   # Blue violet
            (255, 20, 147),   # Deep pink
            (255, 69, 0),     # Red orange
        ]
        
        # Draw flowers at specific positions for consistency
        flower_positions = [
            (150, grass_y + 15), (300, grass_y + 20), (450, grass_y + 12),
            (600, grass_y + 18), (750, grass_y + 15), (900, grass_y + 22),
            (1050, grass_y + 16), (200, grass_y + 25), (350, grass_y + 30),
            (500, grass_y + 28), (650, grass_y + 24), (800, grass_y + 27),
            (950, grass_y + 29), (1100, grass_y + 26), (100, grass_y + 35),
            (250, grass_y + 32), (400, grass_y + 38), (550, grass_y + 34),
            (700, grass_y + 36), (850, grass_y + 33), (1000, grass_y + 37)
        ]
        
        for i, (x, y) in enumerate(flower_positions):
            if x < SCREEN_WIDTH:
                color = flower_colors[i % len(flower_colors)]
                # Flower petals
                for j in range(5):
                    angle = j * 72  # 360/5 = 72 degrees
                    petal_x = x + int(3 * math.cos(math.radians(angle)))
                    petal_y = y + int(3 * math.sin(math.radians(angle)))
                    pygame.draw.circle(self.screen, color, (petal_x, petal_y), 2)
                # Flower center
                pygame.draw.circle(self.screen, (255, 255, 0), (x, y), 1)
                # Flower stem
                pygame.draw.line(self.screen, (0, 100, 0), (x, y), (x, y + 8), 1)
    
    def draw_bushes(self, grass_y):
        """Draw small bushes and shrubs"""
        bush_positions = [
            (180, grass_y + 20), (380, grass_y + 25), (580, grass_y + 22),
            (780, grass_y + 24), (980, grass_y + 21), (1180, grass_y + 23)
        ]
        
        bush_green = (34, 139, 34)
        dark_bush = (0, 100, 0)
        
        for x, y in bush_positions:
            if x < SCREEN_WIDTH:
                # Main bush body
                pygame.draw.ellipse(self.screen, bush_green, (x - 8, y, 16, 12))
                # Bush highlight
                pygame.draw.ellipse(self.screen, (60, 179, 113), (x - 6, y + 1, 12, 4))
                # Bush shadow
                pygame.draw.ellipse(self.screen, dark_bush, (x - 7, y + 8, 14, 6))
    
    def draw_rocks(self, grass_y):
        """Draw small rocks and pebbles"""
        rock_positions = [
            (120, grass_y + 30), (320, grass_y + 35), (520, grass_y + 32),
            (720, grass_y + 36), (920, grass_y + 33), (1120, grass_y + 34)
        ]
        
        rock_gray = (105, 105, 105)
        dark_rock = (69, 69, 69)
        
        for x, y in rock_positions:
            if x < SCREEN_WIDTH:
                # Main rock
                pygame.draw.ellipse(self.screen, rock_gray, (x, y, 6, 4))
                # Rock highlight
                pygame.draw.ellipse(self.screen, (169, 169, 169), (x + 1, y, 3, 2))
                # Rock shadow
                pygame.draw.ellipse(self.screen, dark_rock, (x + 1, y + 2, 4, 3))
    
    def draw_wildflowers(self, grass_y):
        """Draw dandelions and small wildflowers"""
        wildflower_positions = [
            (80, grass_y + 18), (280, grass_y + 22), (480, grass_y + 19),
            (680, grass_y + 21), (880, grass_y + 20), (1080, grass_y + 23)
        ]
        
        for i, (x, y) in enumerate(wildflower_positions):
            if x < SCREEN_WIDTH:
                if i % 2 == 0:
                    # Dandelion
                    pygame.draw.circle(self.screen, (255, 255, 0), (x, y), 3)
                    pygame.draw.circle(self.screen, (255, 215, 0), (x, y), 2)
                    # Dandelion stem
                    pygame.draw.line(self.screen, (0, 100, 0), (x, y), (x, y + 6), 1)
                else:
                    # Small white wildflower
                    for j in range(4):
                        angle = j * 90
                        petal_x = x + int(2 * math.cos(math.radians(angle)))
                        petal_y = y + int(2 * math.sin(math.radians(angle)))
                        pygame.draw.circle(self.screen, (255, 255, 255), (petal_x, petal_y), 1)
                    pygame.draw.circle(self.screen, (255, 255, 0), (x, y), 1)
                    # Stem
                    pygame.draw.line(self.screen, (0, 100, 0), (x, y), (x, y + 5), 1)
    
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
