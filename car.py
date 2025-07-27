import pygame
import math

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start_x = x
        self.width = 40
        self.height = 20
        self.speed = 2  # pixels per frame
        self.max_distance = 800  # maximum distance to travel
        
        # Realistic car colors
        self.car_red = (139, 0, 0)           # Dark red for body
        self.tire_black = (0, 0, 0)          # Black tires
        self.rim_gray = (169, 169, 169)      # Gray rims
        self.glass_blue = (173, 216, 230)    # Light blue windshield
        self.headlight_cream = (255, 255, 224) # Light yellow headlights
        
    def update(self):
        """Update car movement"""
        # Move car to the right
        if self.x - self.start_x < self.max_distance:
            self.x += self.speed
    
    def draw(self, screen):
        """Draw the realistic car"""
        # Draw car body
        pygame.draw.rect(screen, self.car_red, 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height))
        
        # Draw windshield
        pygame.draw.rect(screen, self.glass_blue, 
                        (self.x - self.width//4, self.y - self.height//2 + 2, 
                         self.width//2, self.height//3))
        
        # Draw wheels with better detail
        wheel_radius = 6
        wheel_y = self.y + self.height//2 - 2
        
        # Left wheel
        pygame.draw.circle(screen, self.tire_black, 
                          (int(self.x - self.width//3), int(wheel_y)), wheel_radius)
        pygame.draw.circle(screen, self.rim_gray, 
                          (int(self.x - self.width//3), int(wheel_y)), wheel_radius - 2)
        
        # Right wheel
        pygame.draw.circle(screen, self.tire_black, 
                          (int(self.x + self.width//3), int(wheel_y)), wheel_radius)
        pygame.draw.circle(screen, self.rim_gray, 
                          (int(self.x + self.width//3), int(wheel_y)), wheel_radius - 2)
        
        # Draw headlights
        pygame.draw.circle(screen, self.headlight_cream, 
                          (int(self.x + self.width//2 - 3), int(self.y - 3)), 3)
        pygame.draw.circle(screen, self.headlight_cream, 
                          (int(self.x + self.width//2 - 3), int(self.y + 3)), 3)
        
        # Draw car outline
        pygame.draw.rect(screen, self.tire_black, 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height), 2)
    
    def is_clicked(self, pos):
        """Check if car was clicked"""
        mouse_x, mouse_y = pos
        return (self.x - self.width//2 <= mouse_x <= self.x + self.width//2 and
                self.y - self.height//2 <= mouse_y <= self.y + self.height//2)
    
    def get_info(self):
        """Return information about the car"""
        return """SMART CAR
        
GPS-enabled vehicle with satellite
communication capabilities.
        
• Model: EcoSmart 2025
• Engine: Electric hybrid
• GPS System: Multi-satellite receiver
• Connectivity: 5G + Satellite
• Range: 450 km electric mode
• Autopilot: Level 3 autonomous
• Sensors: Lidar, Camera, Radar

Modern cars use satellite navigation
for real-time traffic updates, route
optimization, and emergency services."""
