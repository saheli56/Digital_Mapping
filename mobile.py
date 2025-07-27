import pygame
import math

class Mobile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 60
        
        # Realistic mobile colors
        self.phone_black = (20, 20, 20)       # Matte black phone body
        self.phone_edge = (40, 40, 40)        # Phone edge highlight
        self.screen_dark = (15, 15, 15)       # Dark screen when off
        self.screen_blue = (0, 120, 215)      # Blue screen when active
        self.screen_bright = (100, 149, 237)  # Bright screen areas
        self.button_silver = (192, 192, 192)  # Silver home button
        self.button_dark = (128, 128, 128)    # Button shadow
        self.signal_green = (0, 200, 0)       # Green signal bars
        self.signal_fade = (0, 150, 0)        # Faded signal
        self.camera_black = (0, 0, 0)         # Camera lens
        self.camera_ring = (100, 100, 100)    # Camera ring
        self.speaker_dark = (30, 30, 30)      # Speaker grille
        
        # Animation for screen
        self.screen_pulse = 0
        self.pulse_speed = 0.08
        self.notification_blink = 0
        
    def update(self):
        """Update mobile phone animations"""
        self.screen_pulse += self.pulse_speed
        if self.screen_pulse >= 2 * math.pi:
            self.screen_pulse = 0
        
        self.notification_blink += 0.15
        if self.notification_blink >= 2 * math.pi:
            self.notification_blink = 0
    
    def draw(self, screen):
        """Draw the realistic mobile phone with detailed features"""
        # Draw phone shadow for depth
        shadow_rect = pygame.Rect(self.x - self.width//2 + 2, self.y - self.height//2 + 2,
                                 self.width, self.height)
        pygame.draw.rect(screen, (10, 10, 10), shadow_rect, border_radius=8)
        
        # Draw phone body with rounded corners
        phone_rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.width, self.height)
        pygame.draw.rect(screen, self.phone_black, phone_rect, border_radius=8)
        
        # Draw phone edge highlight for 3D effect
        edge_rect = pygame.Rect(self.x - self.width//2 + 1, self.y - self.height//2 + 1,
                               self.width - 2, self.height - 2)
        pygame.draw.rect(screen, self.phone_edge, edge_rect, 1, border_radius=7)
        
        # Draw detailed screen
        self.draw_screen(screen)
        
        # Draw camera module
        self.draw_camera(screen)
        
        # Draw speaker grille
        self.draw_speaker(screen)
        
        # Draw home button
        button_y = self.y + self.height//2 - 8
        pygame.draw.circle(screen, self.button_dark, (int(self.x + 1), int(button_y + 1)), 5)
        pygame.draw.circle(screen, self.button_silver, (int(self.x), int(button_y)), 5)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(button_y)), 3)
        pygame.draw.circle(screen, self.button_dark, (int(self.x), int(button_y)), 5, 1)
        
        # Draw side buttons (volume, power)
        # Volume buttons
        pygame.draw.rect(screen, self.phone_edge, 
                        (self.x - self.width//2 - 2, self.y - 10, 2, 8))
        pygame.draw.rect(screen, self.phone_edge, 
                        (self.x - self.width//2 - 2, self.y, 2, 8))
        
        # Power button
        pygame.draw.rect(screen, self.phone_edge, 
                        (self.x + self.width//2, self.y - 8, 2, 12))
    
    def draw_screen(self, screen):
        """Draw detailed phone screen with realistic display"""
        # Screen bezel
        screen_rect = pygame.Rect(self.x - self.width//2 + 4, self.y - self.height//2 + 12,
                                 self.width - 8, self.height - 24)
        pygame.draw.rect(screen, self.screen_dark, screen_rect, border_radius=4)
        
        # Active screen area with subtle pulsing
        screen_brightness = int(40 + 20 * math.sin(self.screen_pulse))
        screen_color = (screen_brightness, screen_brightness, min(255, screen_brightness + 80))
        
        active_screen = pygame.Rect(screen_rect.x + 1, screen_rect.y + 1,
                                   screen_rect.width - 2, screen_rect.height - 2)
        pygame.draw.rect(screen, screen_color, active_screen, border_radius=3)
        
        # Screen highlights and reflections
        highlight_rect = pygame.Rect(active_screen.x + 2, active_screen.y + 2,
                                    active_screen.width - 4, 4)
        pygame.draw.rect(screen, self.screen_bright, highlight_rect, border_radius=2)
        
        # Status bar
        status_bar = pygame.Rect(active_screen.x + 2, active_screen.y + 2,
                                active_screen.width - 4, 8)
        pygame.draw.rect(screen, (0, 80, 160), status_bar)
        
        # App icons simulation
        for i in range(3):
            for j in range(4):
                icon_x = active_screen.x + 4 + j * 6
                icon_y = active_screen.y + 12 + i * 8
                icon_color = [(0, 150, 255), (255, 100, 0), (0, 200, 50), (200, 0, 150)][j]
                pygame.draw.rect(screen, icon_color, (icon_x, icon_y, 4, 4), border_radius=1)
        
        # Signal bars
        self.draw_signal_bars(screen, active_screen)
        
        # Notification LED
        if math.sin(self.notification_blink) > 0.5:
            pygame.draw.circle(screen, (0, 255, 0), 
                             (int(self.x + 8), int(self.y - self.height//2 + 8)), 2)
    
    def draw_camera(self, screen):
        """Draw realistic camera module"""
        camera_x = self.x + 8
        camera_y = self.y - self.height//2 + 8
        
        # Camera module housing
        pygame.draw.circle(screen, self.camera_ring, (int(camera_x), int(camera_y)), 6)
        pygame.draw.circle(screen, self.phone_black, (int(camera_x), int(camera_y)), 5)
        
        # Camera lens
        pygame.draw.circle(screen, self.camera_black, (int(camera_x), int(camera_y)), 4)
        pygame.draw.circle(screen, (50, 50, 100), (int(camera_x), int(camera_y)), 2)
        
        # Lens reflection
        pygame.draw.circle(screen, (150, 150, 200), 
                          (int(camera_x - 1), int(camera_y - 1)), 1)
        
        # Flash LED
        pygame.draw.circle(screen, (255, 255, 200), 
                          (int(camera_x - 8), int(camera_y)), 2)
    
    def draw_speaker(self, screen):
        """Draw speaker grille with realistic holes"""
        speaker_y = self.y - self.height//2 + 6
        speaker_rect = pygame.Rect(self.x - 8, speaker_y - 1, 16, 2)
        pygame.draw.rect(screen, self.speaker_dark, speaker_rect, border_radius=1)
        
        # Speaker holes
        for i in range(8):
            hole_x = self.x - 7 + i * 2
            pygame.draw.circle(screen, self.phone_black, (int(hole_x), int(speaker_y)), 1)

    def draw_signal_bars(self, screen, screen_rect):
        """Draw realistic animated signal strength bars"""
        bar_x = screen_rect.x + screen_rect.width - 20
        bar_y = screen_rect.y + 3
        
        # Draw 4 signal bars with realistic animation
        for i in range(4):
            bar_height = (i + 1) * 2
            # Add subtle pulsing effect with different phases
            pulse_factor = 1 + 0.1 * math.sin(self.screen_pulse + i * 0.5)
            animated_height = max(1, int(bar_height * pulse_factor))
            
            # Signal strength color based on bars
            if i < 2:
                color = self.signal_fade
            else:
                color = self.signal_green
            
            pygame.draw.rect(screen, color,
                           (bar_x + i * 3, bar_y + (6 - animated_height), 
                            2, animated_height))
        
        # WiFi symbol
        wifi_x = bar_x - 8
        wifi_y = bar_y + 2
        for i in range(3):
            radius = (i + 1) * 2
            pygame.draw.arc(screen, self.signal_green,
                           (wifi_x - radius, wifi_y - radius, radius * 2, radius * 2),
                           -math.pi/4, math.pi/4, 1)
    
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
