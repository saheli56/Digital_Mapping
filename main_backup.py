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
    
    def draw_mountains(self):
        """Draw distant mountains for atmospheric depth"""
        # Get horizon line based on Earth position
        horizon_y = self.earth.y + self.earth.radius + 30
        
        # Mountain ranges at different distances for parallax effect
        mountain_ranges = [
            {'peaks': [(0, 40), (200, 60), (400, 35), (600, 55), (800, 30), (1000, 45), (1200, 25)], 'color': MOUNTAIN_PURPLE, 'alpha': 60},
            {'peaks': [(100, 30), (300, 45), (500, 25), (700, 40), (900, 20), (1100, 35)], 'color': MOUNTAIN_BLUE, 'alpha': 40},
        ]
        
        for mountain_range in mountain_ranges:
            # Create surface for alpha blending
            mountain_surface = pygame.Surface((SCREEN_WIDTH, 100), pygame.SRCALPHA)
            
            # Create mountain silhouette points
            points = [(0, 100)]  # Start from bottom left
            
            for x, height in mountain_range['peaks']:
                points.append((x, 100 - height))
            
            points.append((SCREEN_WIDTH, 100))  # End at bottom right
            points.append((SCREEN_WIDTH, 100))  # Close the polygon
            points.append((0, 100))
            
            # Draw mountain silhouette
            pygame.draw.polygon(mountain_surface, (*mountain_range['color'], mountain_range['alpha']), points)
            
            # Blit to main screen
            self.screen.blit(mountain_surface, (0, horizon_y - 70))
        
        # Add atmospheric haze
        haze_surface = pygame.Surface((SCREEN_WIDTH, 50), pygame.SRCALPHA)
        for y in range(50):
            alpha = int(30 * (1 - y / 50))  # Fade from opaque to transparent
            if alpha > 0:
                pygame.draw.line(haze_surface, (*HORIZON_MIST, alpha), (0, y), (SCREEN_WIDTH, y))
        
        self.screen.blit(haze_surface, (0, horizon_y - 20))

    def draw_grassland(self):

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE_TOP = (87, 138, 201)     # Darker blue at top
SKY_BLUE_MID = (135, 206, 235)    # Medium blue in middle
SKY_BLUE_BOTTOM = (176, 224, 230) # Lighter blue at bottom
CLOUD_WHITE = (255, 255, 255)     # Pure white clouds
CLOUD_GRAY = (240, 240, 240)      # Light gray cloud shadows
SUN_YELLOW = (255, 255, 0)        # Bright sun
SUN_GLOW = (255, 255, 200)        # Sun glow effect

GRASS_GREEN = (34, 139, 34)       # Forest green for grass
DARK_GRASS = (0, 100, 0)          # Darker green for grass texture
LIGHT_GRASS = (50, 205, 50)       # Lighter green highlights
EARTH_BROWN = (139, 69, 19)       # Soil color
FLOWER_COLORS = [(255, 0, 127), (255, 20, 147), (255, 105, 180), (255, 255, 0), (255, 165, 0)]
MOUNTAIN_PURPLE = (72, 61, 139)   # Distant mountain color
MOUNTAIN_BLUE = (100, 149, 237)   # Mountain highlights
HORIZON_MIST = (230, 230, 250)    # Atmospheric haze
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
        
        # Sky and weather animation variables
        self.cloud_offset = 0
        self.sun_glow_pulse = 0
        
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
        
        # Update sky animations
        self.cloud_offset += 0.5  # Slow cloud movement
        if self.cloud_offset > SCREEN_WIDTH + 200:
            self.cloud_offset = -200
            
        self.sun_glow_pulse += 0.05
        if self.sun_glow_pulse > 2 * math.pi:
            self.sun_glow_pulse = 0
        
        if self.earth_clicked:
            # Update satellite
            if self.satellite:
                self.satellite.update()
                
            # Update car movement
            if self.car:
                self.car.update()
                
            # Update mobile phone
            if self.mobile:
                self.mobile.update()
                
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
    
    def draw_realistic_sky(self):
        """Draw a realistic sky with gradient, sun, and animated clouds"""
        # Draw sky gradient from top to bottom
        for y in range(SCREEN_HEIGHT):
            # Calculate gradient ratio
            ratio = y / SCREEN_HEIGHT
            
            # Interpolate between sky colors
            if ratio < 0.3:  # Top portion - darker blue
                blend_ratio = ratio / 0.3
                r = int(SKY_BLUE_TOP[0] * (1 - blend_ratio) + SKY_BLUE_MID[0] * blend_ratio)
                g = int(SKY_BLUE_TOP[1] * (1 - blend_ratio) + SKY_BLUE_MID[1] * blend_ratio)
                b = int(SKY_BLUE_TOP[2] * (1 - blend_ratio) + SKY_BLUE_MID[2] * blend_ratio)
            else:  # Bottom portion - lighter blue
                blend_ratio = (ratio - 0.3) / 0.7
                r = int(SKY_BLUE_MID[0] * (1 - blend_ratio) + SKY_BLUE_BOTTOM[0] * blend_ratio)
                g = int(SKY_BLUE_MID[1] * (1 - blend_ratio) + SKY_BLUE_BOTTOM[1] * blend_ratio)
                b = int(SKY_BLUE_MID[2] * (1 - blend_ratio) + SKY_BLUE_BOTTOM[2] * blend_ratio)
            
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        # Draw animated sun
        self.draw_sun()
        
        # Draw distant mountains for depth
        self.draw_mountains()
        
        # Draw animated clouds
        self.draw_clouds()
    
    def draw_sun(self):
        """Draw an animated sun with glow effect"""
        sun_x = SCREEN_WIDTH - 150
        sun_y = 100
        
        # Sun glow effect with pulsing
        glow_intensity = 1.0 + 0.2 * math.sin(self.sun_glow_pulse)
        glow_radius = int(40 * glow_intensity)
        
        # Draw multiple glow layers
        for i in range(5):
            glow_alpha = max(10, int(50 - i * 10))
            radius = glow_radius - i * 5
            if radius > 0:
                # Create a surface for alpha blending
                glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(glow_surface, (*SUN_GLOW, glow_alpha), (radius, radius), radius)
                self.screen.blit(glow_surface, (sun_x - radius, sun_y - radius))
        
        # Draw main sun
        pygame.draw.circle(self.screen, SUN_YELLOW, (sun_x, sun_y), 25)
        pygame.draw.circle(self.screen, (255, 255, 150), (sun_x, sun_y), 20)
        
        # Sun rays
        for i in range(8):
            angle = i * math.pi / 4 + self.sun_glow_pulse * 0.5
            ray_length = 40 + 5 * math.sin(self.sun_glow_pulse + i)
            end_x = sun_x + math.cos(angle) * ray_length
            end_y = sun_y + math.sin(angle) * ray_length
            start_x = sun_x + math.cos(angle) * 30
            start_y = sun_y + math.sin(angle) * 30
            pygame.draw.line(self.screen, SUN_YELLOW, (start_x, start_y), (end_x, end_y), 3)
    
    def draw_clouds(self):
        """Draw realistic animated clouds"""
        clouds_data = [
            {'x': -100 + self.cloud_offset, 'y': 80, 'size': 60, 'speed': 1.0},
            {'x': 200 + self.cloud_offset * 0.7, 'y': 120, 'size': 80, 'speed': 0.7},
            {'x': 500 + self.cloud_offset * 1.2, 'y': 60, 'size': 50, 'speed': 1.2},
            {'x': 800 + self.cloud_offset * 0.8, 'y': 140, 'size': 70, 'speed': 0.8},
        ]
        
        for cloud in clouds_data:
            if -200 < cloud['x'] < SCREEN_WIDTH + 200:  # Only draw visible clouds
                self.draw_single_cloud(cloud['x'], cloud['y'], cloud['size'])
    
    def draw_single_cloud(self, x, y, size):
        """Draw a single realistic cloud"""
        # Cloud shadow
        shadow_offset = 3
        cloud_circles = [
            (x - size//2, y, size//2),
            (x, y - size//3, size//1.5),
            (x + size//2, y, size//2),
            (x - size//4, y + size//4, size//2.5),
            (x + size//4, y + size//4, size//2.5),
        ]
        
        # Draw shadow
        for circle_x, circle_y, radius in cloud_circles:
            pygame.draw.circle(self.screen, CLOUD_GRAY, 
                             (int(circle_x + shadow_offset), int(circle_y + shadow_offset)), 
                             int(radius))
        
        # Draw main cloud
        for circle_x, circle_y, radius in cloud_circles:
            pygame.draw.circle(self.screen, CLOUD_WHITE, 
                             (int(circle_x), int(circle_y)), int(radius))

    def draw_grassland(self):
        """Draw enhanced realistic grassland with flowers and details"""
        grass_y = self.earth.y + self.earth.radius + 50
        grass_height = SCREEN_HEIGHT - grass_y
        
        # Draw soil/dirt base
        soil_rect = pygame.Rect(0, grass_y + grass_height - 20, SCREEN_WIDTH, 20)
        pygame.draw.rect(self.screen, EARTH_BROWN, soil_rect)
        
        # Draw grass base layer with gradient
        for y in range(int(grass_y), SCREEN_HEIGHT):
            ratio = (y - grass_y) / grass_height
            # Gradient from lighter green at top to darker at bottom
            r = int(GRASS_GREEN[0] * (1 - ratio * 0.3))
            g = int(GRASS_GREEN[1] * (1 - ratio * 0.2))
            b = int(GRASS_GREEN[2] * (1 - ratio * 0.3))
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        # Draw detailed grass blades with wind effect
        wind_offset = math.sin(self.cloud_offset * 0.1) * 2
        
        for i in range(0, SCREEN_WIDTH, 3):
            # Vary grass characteristics
            grass_base_height = 15 + (i % 20)
            wind_effect = wind_offset + math.sin(i * 0.05) * 1.5
            
            # Multiple grass blade colors for variety
            grass_colors = [DARK_GRASS, GRASS_GREEN, LIGHT_GRASS]
            color_idx = (i // 3) % len(grass_colors)
            grass_color = grass_colors[color_idx]
            
            # Draw grass blades with wind sway
            for blade in range(3):
                blade_x = i + blade
                blade_height = grass_base_height + (blade * 3) - (blade % 2) * 5
                blade_top_x = blade_x + wind_effect + (blade % 2 - 0.5) * 2
                blade_top_y = grass_y + (blade * 2)
                blade_bottom_y = grass_y + blade_height
                
                # Draw grass blade with varying thickness
                thickness = 2 if blade % 2 == 0 else 1
                pygame.draw.line(self.screen, grass_color,
                               (blade_x, blade_bottom_y),
                               (blade_top_x, blade_top_y), thickness)
        
        # Add flowers scattered throughout the grass
        self.draw_flowers(grass_y)
        
        # Add small details like rocks and patches
        self.draw_ground_details(grass_y)
    
    def draw_flowers(self, grass_y):
        """Draw small flowers scattered in the grass"""
        flower_positions = [
            (150, grass_y + 10), (300, grass_y + 15), (450, grass_y + 8),
            (600, grass_y + 12), (750, grass_y + 18), (900, grass_y + 6),
            (1050, grass_y + 14), (200, grass_y + 20), (800, grass_y + 25)
        ]
        
        for i, (x, y) in enumerate(flower_positions):
            flower_color = FLOWER_COLORS[i % len(FLOWER_COLORS)]
            
            # Flower petals
            petal_size = 3
            for angle in range(0, 360, 60):  # 6 petals
                petal_x = x + math.cos(math.radians(angle)) * petal_size
                petal_y = y + math.sin(math.radians(angle)) * petal_size
                pygame.draw.circle(self.screen, flower_color, (int(petal_x), int(petal_y)), 2)
            
            # Flower center
            pygame.draw.circle(self.screen, SUN_YELLOW, (x, y), 2)
            
            # Flower stem
            pygame.draw.line(self.screen, DARK_GRASS, (x, y), (x, y + 8), 1)
    
    def draw_ground_details(self, grass_y):
        """Draw small rocks and dirt patches for realism"""
        # Small rocks
        rock_positions = [(100, grass_y + 25), (400, grass_y + 30), (700, grass_y + 28), (1000, grass_y + 32)]
        for x, y in rock_positions:
            # Rock shadow
            pygame.draw.ellipse(self.screen, (60, 60, 60), (x + 1, y + 1, 8, 4))
            # Rock
            pygame.draw.ellipse(self.screen, (128, 128, 128), (x, y, 8, 4))
            pygame.draw.ellipse(self.screen, (160, 160, 160), (x, y, 6, 3))
        
        # Dirt patches
        dirt_patches = [(250, grass_y + 20), (550, grass_y + 25), (850, grass_y + 22)]
        for x, y in dirt_patches:
            pygame.draw.ellipse(self.screen, EARTH_BROWN, (x, y, 15, 8))
            pygame.draw.ellipse(self.screen, (120, 60, 20), (x + 2, y + 1, 10, 5))
    
    def render(self):
        # Draw realistic sky with gradient, sun, and clouds
        self.draw_realistic_sky()
        
        # Draw Earth
        self.earth.draw(self.screen)
        
        if self.earth_clicked:
            # Draw enhanced grassland
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
