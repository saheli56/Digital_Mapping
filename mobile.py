import pygame
import math

class Mobile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50
        
        # Realistic mobile colors
        self.phone_black = (0, 0, 0)          # Black phone body
        self.screen_dark = (25, 25, 25)       # Dark screen when off
        self.screen_blue = (0, 100, 200)      # Blue screen when active
        self.button_silver = (192, 192, 192)  # Silver home button
        self.signal_green = (0, 128, 0)       # Green signal bars
        
        # Animation for screen
        self.screen_pulse = 0
        self.pulse_speed = 0.1
        
    def update(self):
        """Update mobile phone animations"""
        self.screen_pulse += self.pulse_speed
        if self.screen_pulse >= 2 * math.pi:
            self.screen_pulse = 0
    
    def draw(self, screen):
        """Draw the realistic mobile phone"""
        # Draw phone body
        pygame.draw.rect(screen, self.phone_black, 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height))
        
        # Draw screen with subtle pulsing effect
        screen_brightness = int(50 + 30 * math.sin(self.screen_pulse))
        screen_color = (screen_brightness, screen_brightness, min(255, screen_brightness + 50))
        
        pygame.draw.rect(screen, screen_color, 
                        (self.x - self.width//2 + 3, self.y - self.height//2 + 8, 
                         self.width - 6, self.height - 16))
        
        # Draw home button
        pygame.draw.circle(screen, self.button_silver, 
                          (int(self.x), int(self.y + self.height//2 - 6)), 4)
        
        # Draw signal bars
        self.draw_signal_bars(screen)
        
        # Draw phone outline with rounded corners effect
        pygame.draw.rect(screen, (50, 50, 50), 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height), 2)
    
    def draw_signal_bars(self, screen):
        """Draw realistic animated signal strength bars"""
        bar_x = self.x - self.width//2 + 5
        bar_y = self.y - self.height//2 + 12
        
        # Draw 4 signal bars with subtle animation
        for i in range(4):
            bar_height = (i + 1) * 3
            # Add subtle pulsing effect to signal bars
            pulse_factor = 1 + 0.1 * math.sin(self.screen_pulse + i * 0.3)
            animated_height = int(bar_height * pulse_factor)
            
            pygame.draw.rect(screen, self.signal_green,
                           (bar_x + i * 4, bar_y + (12 - animated_height), 
                            2, animated_height))
    
    def is_clicked(self, pos):
        """Check if mobile phone was clicked"""
        mouse_x, mouse_y = pos
        return (self.x - self.width//2 <= mouse_x <= self.x + self.width//2 and
                self.y - self.height//2 <= mouse_y <= self.y + self.height//2)
    
    def get_info(self):
        """Return information about the mobile phone"""
        return """SMARTPHONE
        
Modern mobile device with GPS and
satellite communication features.
        
• Model: GeoPhone Pro
• OS: Android 14 / iOS 17
• GPS: Multi-constellation receiver
• Connectivity: 5G, WiFi, Bluetooth
• Sensors: Accelerometer, Gyroscope
• Camera: 108MP with geotagging
• Battery: 5000mAh fast charge

Smartphones use satellite signals for
location services, mapping apps, and
emergency communication worldwide."""
