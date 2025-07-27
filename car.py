import pygame
import math

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start_x = x
        self.width = 50
        self.height = 25
        self.speed = 2  # pixels per frame
        self.max_distance = 800  # maximum distance to travel
        
        # Realistic car colors
        self.car_red = (139, 0, 0)           # Dark red for body
        self.car_highlight = (220, 20, 60)   # Bright red highlights
        self.car_shadow = (100, 0, 0)        # Dark shadow
        self.tire_black = (0, 0, 0)          # Black tires
        self.rim_silver = (192, 192, 192)    # Silver rims
        self.rim_detail = (255, 255, 255)    # White rim details
        self.glass_blue = (100, 149, 237)    # Realistic glass tint
        self.glass_reflect = (173, 216, 230) # Glass reflections
        self.headlight_cream = (255, 255, 224) # Light yellow headlights
        self.headlight_bright = (255, 255, 255) # Bright headlight center
        self.grille_dark = (64, 64, 64)      # Dark grille
        self.chrome_silver = (220, 220, 220) # Chrome details
        
    def update(self):
        """Update car (position now controlled externally by slider)"""
        # Car position is now controlled by the slider in main.py
        # No automatic movement here
        pass
    
    def draw(self, screen):
        """Draw the realistic car with detailed features"""
        # Draw car shadow for depth
        shadow_offset = 3
        pygame.draw.ellipse(screen, (50, 50, 50), 
                           (self.x - self.width//2 + shadow_offset, 
                            self.y + self.height//2 + 2, 
                            self.width, 8))
        
        # Draw car body with 3D effect
        # Main body
        car_rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, 
                              self.width, self.height)
        pygame.draw.rect(screen, self.car_shadow, 
                        (car_rect.x + 2, car_rect.y + 2, car_rect.width, car_rect.height))
        pygame.draw.rect(screen, self.car_red, car_rect)
        
        # Car body highlights for metallic look
        pygame.draw.rect(screen, self.car_highlight, 
                        (car_rect.x + 2, car_rect.y + 2, car_rect.width - 4, 3))
        
        # Draw detailed windshield and windows
        self.draw_windows(screen)
        
        # Draw front grille
        grille_rect = pygame.Rect(self.x + self.width//2 - 5, self.y - 6, 5, 12)
        pygame.draw.rect(screen, self.grille_dark, grille_rect)
        # Grille lines
        for i in range(3):
            y_pos = grille_rect.y + 2 + i * 3
            pygame.draw.line(screen, self.chrome_silver, 
                           (grille_rect.x, y_pos), (grille_rect.x + 4, y_pos), 1)
        
        # Draw enhanced wheels with detailed rims
        self.draw_wheels(screen)
        
        # Draw detailed headlights
        self.draw_headlights(screen)
        
        # Draw side mirrors
        mirror_size = 3
        pygame.draw.circle(screen, self.chrome_silver, 
                          (int(self.x - self.width//4), int(self.y - self.height//2 - 2)), mirror_size)
        pygame.draw.circle(screen, self.glass_blue, 
                          (int(self.x - self.width//4), int(self.y - self.height//2 - 2)), mirror_size - 1)
        
        # Draw door handles
        pygame.draw.circle(screen, self.chrome_silver, 
                          (int(self.x - 5), int(self.y + 2)), 2)
        pygame.draw.circle(screen, self.chrome_silver, 
                          (int(self.x + 5), int(self.y + 2)), 2)
        
        # Draw car outline
        pygame.draw.rect(screen, self.tire_black, car_rect, 2)
    
    def draw_windows(self, screen):
        """Draw detailed car windows with reflections"""
        # Front windshield
        windshield = pygame.Rect(self.x + self.width//4, self.y - self.height//2 + 3, 
                                self.width//3, self.height//2 - 2)
        pygame.draw.rect(screen, self.glass_blue, windshield)
        # Windshield reflection
        pygame.draw.rect(screen, self.glass_reflect, 
                        (windshield.x + 1, windshield.y + 1, windshield.width - 2, 3))
        pygame.draw.rect(screen, self.tire_black, windshield, 1)
        
        # Side windows
        side_window = pygame.Rect(self.x - self.width//6, self.y - self.height//2 + 3, 
                                 self.width//3, self.height//2 - 2)
        pygame.draw.rect(screen, self.glass_blue, side_window)
        pygame.draw.rect(screen, self.glass_reflect, 
                        (side_window.x + 1, side_window.y + 1, side_window.width - 2, 2))
        pygame.draw.rect(screen, self.tire_black, side_window, 1)
        
        # Rear window
        rear_window = pygame.Rect(self.x - self.width//2 + 3, self.y - self.height//2 + 3, 
                                 self.width//4, self.height//2 - 2)
        pygame.draw.rect(screen, self.glass_blue, rear_window)
        pygame.draw.rect(screen, self.tire_black, rear_window, 1)
    
    def draw_wheels(self, screen):
        """Draw detailed wheels with realistic rims and tires"""
        wheel_radius = 8
        wheel_y = self.y + self.height//2 - 3
        
        # Left wheel
        left_wheel_x = int(self.x - self.width//3)
        left_wheel_y = int(wheel_y)
        
        # Tire
        pygame.draw.circle(screen, self.tire_black, (left_wheel_x, left_wheel_y), wheel_radius)
        # Rim
        pygame.draw.circle(screen, self.rim_silver, (left_wheel_x, left_wheel_y), wheel_radius - 2)
        # Rim spokes
        for i in range(5):
            angle = i * 72  # 360/5 = 72 degrees
            spoke_x = left_wheel_x + int(4 * math.cos(math.radians(angle)))
            spoke_y = left_wheel_y + int(4 * math.sin(math.radians(angle)))
            pygame.draw.line(screen, self.rim_detail, 
                           (left_wheel_x, left_wheel_y), (spoke_x, spoke_y), 2)
        # Center cap
        pygame.draw.circle(screen, self.rim_detail, (left_wheel_x, left_wheel_y), 2)
        
        # Right wheel
        right_wheel_x = int(self.x + self.width//3)
        right_wheel_y = int(wheel_y)
        
        # Tire
        pygame.draw.circle(screen, self.tire_black, (right_wheel_x, right_wheel_y), wheel_radius)
        # Rim
        pygame.draw.circle(screen, self.rim_silver, (right_wheel_x, right_wheel_y), wheel_radius - 2)
        # Rim spokes
        for i in range(5):
            angle = i * 72
            spoke_x = right_wheel_x + int(4 * math.cos(math.radians(angle)))
            spoke_y = right_wheel_y + int(4 * math.sin(math.radians(angle)))
            pygame.draw.line(screen, self.rim_detail, 
                           (right_wheel_x, right_wheel_y), (spoke_x, spoke_y), 2)
        # Center cap
        pygame.draw.circle(screen, self.rim_detail, (right_wheel_x, right_wheel_y), 2)
    
    def draw_headlights(self, screen):
        """Draw detailed headlights with realistic lighting effects"""
        headlight_x = self.x + self.width//2 - 2
        
        # Upper headlight
        upper_light = (int(headlight_x), int(self.y - 5))
        pygame.draw.circle(screen, self.headlight_cream, upper_light, 4)
        pygame.draw.circle(screen, self.headlight_bright, upper_light, 2)
        pygame.draw.circle(screen, self.chrome_silver, upper_light, 4, 1)
        
        # Lower headlight
        lower_light = (int(headlight_x), int(self.y + 5))
        pygame.draw.circle(screen, self.headlight_cream, lower_light, 4)
        pygame.draw.circle(screen, self.headlight_bright, lower_light, 2)
        pygame.draw.circle(screen, self.chrome_silver, lower_light, 4, 1)
        
        # Tail lights
        tail_x = self.x - self.width//2 + 2
        pygame.draw.circle(screen, (139, 0, 0), (int(tail_x), int(self.y - 3)), 3)
        pygame.draw.circle(screen, (255, 0, 0), (int(tail_x), int(self.y - 3)), 1)
        pygame.draw.circle(screen, (139, 0, 0), (int(tail_x), int(self.y + 3)), 3)
        pygame.draw.circle(screen, (255, 0, 0), (int(tail_x), int(self.y + 3)), 1)
    
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
