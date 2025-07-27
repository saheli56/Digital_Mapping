import pygame
import math

class Satellite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.angle = 0
        self.rotation_speed = 1.5  # degrees per frame
        
        # Realistic satellite colors
        self.body_silver = (192, 192, 192)    # Silver body
        self.body_dark = (128, 128, 128)      # Dark gray shadows
        self.panel_blue = (0, 0, 139)         # Dark blue solar panels
        self.panel_light = (100, 149, 237)    # Light blue panel reflections
        self.panel_frame = (169, 169, 169)    # Gray panel frames
        self.antenna_gold = (255, 215, 0)     # Gold antenna
        self.antenna_black = (0, 0, 0)        # Black antenna details
        self.thruster_red = (220, 20, 60)     # Red thruster
        self.light_blue = (173, 216, 230)     # Communication lights
        
    def update(self):
        """Update satellite rotation"""
        self.angle += self.rotation_speed
        if self.angle >= 360:
            self.angle = 0
            
    def draw(self, screen):
        """Draw the realistic rotating satellite"""
        # Calculate rotation
        rad_angle = math.radians(self.angle)
        
        # Draw satellite shadow for depth
        shadow_offset = 3
        pygame.draw.rect(screen, self.body_dark, 
                        (self.x - self.width//2 + shadow_offset, self.y - self.height//2 + shadow_offset, 
                         self.width, self.height))
        
        # Draw main satellite body with metallic look
        pygame.draw.rect(screen, self.body_silver, 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height))
        
        # Add metallic highlights
        pygame.draw.rect(screen, (220, 220, 220), 
                        (self.x - self.width//2 + 2, self.y - self.height//2 + 2, 
                         self.width - 4, 3))
        
        # Draw detailed equipment compartments
        self.draw_equipment_details(screen)
        
        # Draw enhanced solar panels
        self.draw_solar_panels(screen, rad_angle)
        
        # Draw multiple communication antennas
        self.draw_antennas(screen, rad_angle)
        
        # Draw thruster
        thruster_x = self.x + math.cos(rad_angle + math.pi) * 20
        thruster_y = self.y + math.sin(rad_angle + math.pi) * 20
        pygame.draw.circle(screen, self.thruster_red, (int(thruster_x), int(thruster_y)), 4)
        pygame.draw.circle(screen, (255, 100, 100), (int(thruster_x), int(thruster_y)), 2)
        
        # Draw communication lights
        for i, offset in enumerate([-0.3, 0, 0.3]):
            light_x = self.x + math.cos(rad_angle + offset) * 12
            light_y = self.y + math.sin(rad_angle + offset) * 12
            color = self.light_blue if i % 2 == 0 else (0, 255, 0)
            pygame.draw.circle(screen, color, (int(light_x), int(light_y)), 2)
        
        # Draw satellite outline
        pygame.draw.rect(screen, self.antenna_black, 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height), 2)
    
    def draw_equipment_details(self, screen):
        """Draw detailed equipment compartments on the satellite"""
        # Communication equipment box
        equipment_rect = pygame.Rect(self.x - 8, self.y - 6, 16, 12)
        pygame.draw.rect(screen, self.body_dark, equipment_rect)
        pygame.draw.rect(screen, self.antenna_black, equipment_rect, 1)
        
        # Small equipment details
        for i in range(3):
            for j in range(2):
                detail_x = self.x - 6 + i * 4
                detail_y = self.y - 4 + j * 4
                pygame.draw.rect(screen, (255, 215, 0), (detail_x, detail_y, 2, 2))
    
    def draw_antennas(self, screen, angle):
        """Draw multiple detailed communication antennas"""
        # Main dish antenna
        dish_x = self.x + math.cos(angle - math.pi/2) * 18
        dish_y = self.y + math.sin(angle - math.pi/2) * 18
        pygame.draw.circle(screen, self.antenna_gold, (int(dish_x), int(dish_y)), 8)
        pygame.draw.circle(screen, self.antenna_black, (int(dish_x), int(dish_y)), 8, 2)
        pygame.draw.circle(screen, self.antenna_gold, (int(dish_x), int(dish_y)), 3)
        
        # Support beam
        pygame.draw.line(screen, self.antenna_black, 
                        (self.x, self.y), (dish_x, dish_y), 2)
        
        # Secondary rod antennas
        for i, offset_angle in enumerate([math.pi/4, -math.pi/4, 3*math.pi/4]):
            rod_length = 20 if i == 0 else 15
            rod_tip_x = self.x + math.cos(angle + offset_angle) * rod_length
            rod_tip_y = self.y + math.sin(angle + offset_angle) * rod_length
            pygame.draw.line(screen, self.antenna_gold, 
                            (self.x, self.y), (rod_tip_x, rod_tip_y), 2)
            # Antenna tip
            pygame.draw.circle(screen, self.thruster_red, (int(rod_tip_x), int(rod_tip_y)), 2)

    def draw_solar_panels(self, screen, angle):
        """Draw realistic rotating solar panels with detailed cells"""
        panel_length = 40
        panel_width = 12
        
        # Left panel
        left_start_x = self.x - self.width//2 - panel_length * math.cos(angle)
        left_start_y = self.y - panel_length * math.sin(angle)
        left_end_x = self.x - self.width//2
        left_end_y = self.y
        
        # Right panel
        right_start_x = self.x + self.width//2
        right_start_y = self.y
        right_end_x = self.x + self.width//2 + panel_length * math.cos(angle)
        right_end_y = self.y + panel_length * math.sin(angle)
        
        # Draw panel shadows
        shadow_offset = 2
        pygame.draw.line(screen, self.body_dark, 
                        (left_start_x + shadow_offset, left_start_y + shadow_offset), 
                        (left_end_x + shadow_offset, left_end_y + shadow_offset), panel_width + 2)
        pygame.draw.line(screen, self.body_dark, 
                        (right_start_x + shadow_offset, right_start_y + shadow_offset), 
                        (right_end_x + shadow_offset, right_end_y + shadow_offset), panel_width + 2)
        
        # Draw panel frames
        pygame.draw.line(screen, self.panel_frame, 
                        (left_start_x, left_start_y), (left_end_x, left_end_y), panel_width + 4)
        pygame.draw.line(screen, self.panel_frame, 
                        (right_start_x, right_start_y), (right_end_x, right_end_y), panel_width + 4)
        
        # Draw solar panels with gradient effect
        pygame.draw.line(screen, self.panel_blue, 
                        (left_start_x, left_start_y), (left_end_x, left_end_y), panel_width)
        pygame.draw.line(screen, self.panel_blue, 
                        (right_start_x, right_start_y), (right_end_x, right_end_y), panel_width)
        
        # Add realistic panel cell grid pattern
        for i in range(8):
            offset_ratio = i / 8.0
            # Left panel cells
            cell_x = left_start_x + (left_end_x - left_start_x) * offset_ratio
            cell_y = left_start_y + (left_end_y - left_start_y) * offset_ratio
            
            for j in range(-2, 3):
                grid_offset = j * 2
                perp_x = -math.sin(angle) * grid_offset
                perp_y = math.cos(angle) * grid_offset
                
                color = self.panel_light if (i + j) % 2 == 0 else self.panel_blue
                pygame.draw.circle(screen, color, 
                                 (int(cell_x + perp_x), int(cell_y + perp_y)), 1)
            
            # Right panel cells
            cell_x = right_start_x + (right_end_x - right_start_x) * offset_ratio
            cell_y = right_start_y + (right_end_y - right_start_y) * offset_ratio
            
            for j in range(-2, 3):
                grid_offset = j * 2
                perp_x = -math.sin(angle) * grid_offset
                perp_y = math.cos(angle) * grid_offset
                
                color = self.panel_light if (i + j) % 2 == 0 else self.panel_blue
                pygame.draw.circle(screen, color, 
                                 (int(cell_x + perp_x), int(cell_y + perp_y)), 1)
    
    def is_clicked(self, pos):
        """Check if satellite was clicked"""
        mouse_x, mouse_y = pos
        # Simple rectangular collision detection
        return (self.x - self.width//2 <= mouse_x <= self.x + self.width//2 and
                self.y - self.height//2 <= mouse_y <= self.y + self.height//2)
    
    def get_info(self):
        """Return information about the satellite"""
        return """SATELLITE
        
Artificial satellite orbiting Earth for
communication and data transmission.
        
• Type: Communication Satellite
• Orbit Height: 35,786 km (Geostationary)
• Launch Date: 2023
• Purpose: Digital mapping and GPS
• Solar Panels: 2 x 15m arrays
• Power Output: 5.2 kW
• Signal Range: Global coverage

Satellites enable GPS navigation,
weather forecasting, and global
communications for modern society."""
