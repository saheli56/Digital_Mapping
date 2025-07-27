import pygame
import math

class Satellite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 20
        self.angle = 0
        self.rotation_speed = 2  # degrees per frame
        
        # Realistic satellite colors
        self.body_silver = (169, 169, 169)    # Dark gray for body
        self.panel_blue = (25, 25, 112)       # Dark blue solar panels
        self.panel_frame = (105, 105, 105)    # Dim gray for panel frames
        self.antenna_black = (0, 0, 0)        # Black antenna
        
    def update(self):
        """Update satellite rotation"""
        self.angle += self.rotation_speed
        if self.angle >= 360:
            self.angle = 0
            
    def draw(self, screen):
        """Draw the realistic rotating satellite"""
        # Calculate rotation
        rad_angle = math.radians(self.angle)
        
        # Draw main satellite body
        pygame.draw.rect(screen, self.body_silver, 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height))
        
        # Draw solar panels
        self.draw_solar_panels(screen, rad_angle)
        
        # Draw antenna
        antenna_tip_x = self.x + math.cos(rad_angle - math.pi/2) * 15
        antenna_tip_y = self.y + math.sin(rad_angle - math.pi/2) * 15
        pygame.draw.line(screen, self.antenna_black, 
                        (self.x, self.y), (antenna_tip_x, antenna_tip_y), 3)
        
        # Draw satellite outline
        pygame.draw.rect(screen, self.antenna_black, 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height), 2)
    
    def draw_solar_panels(self, screen, angle):
        """Draw realistic rotating solar panels"""
        panel_length = 30
        panel_width = 8
        
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
        
        # Draw panel frames first
        pygame.draw.line(screen, self.panel_frame, 
                        (left_start_x, left_start_y), (left_end_x, left_end_y), panel_width + 2)
        pygame.draw.line(screen, self.panel_frame, 
                        (right_start_x, right_start_y), (right_end_x, right_end_y), panel_width + 2)
        
        # Draw solar panels
        pygame.draw.line(screen, self.panel_blue, 
                        (left_start_x, left_start_y), (left_end_x, left_end_y), panel_width)
        pygame.draw.line(screen, self.panel_blue, 
                        (right_start_x, right_start_y), (right_end_x, right_end_y), panel_width)
        
        # Add realistic panel cell details
        for i in range(5):
            offset = (i - 2) * panel_width // 5
            # Left panel cells
            pygame.draw.line(screen, (0, 0, 139),
                           (left_start_x + offset, left_start_y + offset),
                           (left_end_x + offset, left_end_y + offset), 1)
            # Right panel cells
            pygame.draw.line(screen, (0, 0, 139),
                           (right_start_x + offset, right_start_y + offset),
                           (right_end_x + offset, right_end_y + offset), 1)
    
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
