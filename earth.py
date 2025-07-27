import pygame
import math

class Earth:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 80
        self.angle = 0
        self.rotation_speed = 1  # degrees per frame
        
        # Realistic Earth colors
        self.ocean_blue = (25, 25, 112)      # Deep ocean blue
        self.land_green = (34, 139, 34)      # Forest green for continents
        self.land_brown = (160, 82, 45)      # Saddle brown for mountains
        self.ice_white = (240, 248, 255)     # Alice blue for ice caps
        
    def update(self):
        """Update Earth rotation"""
        self.angle += self.rotation_speed
        if self.angle >= 360:
            self.angle = 0
            
    def draw(self, screen):
        """Draw the rotating Earth with realistic colors"""
        # Draw main Earth body (oceans)
        pygame.draw.circle(screen, self.ocean_blue, (int(self.x), int(self.y)), self.radius)
        
        # Draw continents based on rotation
        self.draw_continents(screen)
        
        # Draw ice caps
        self.draw_ice_caps(screen)
        
        # Draw Earth outline
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), self.radius, 2)
        
    def draw_continents(self, screen):
        """Draw realistic continents that rotate with Earth"""
        # Calculate continent positions based on rotation
        continent_offset = math.radians(self.angle)
        
        # Continent 1 (Africa-like)
        cont1_x = self.x + math.cos(continent_offset) * 30
        cont1_y = self.y + math.sin(continent_offset) * 20
        if self.is_visible(continent_offset):
            pygame.draw.ellipse(screen, self.land_green, 
                              (cont1_x - 15, cont1_y - 25, 30, 50))
            # Add some brown for mountains/desert
            pygame.draw.ellipse(screen, self.land_brown, 
                              (cont1_x - 8, cont1_y - 10, 16, 20))
        
        # Continent 2 (America-like)
        cont2_offset = continent_offset + math.pi * 0.6
        cont2_x = self.x + math.cos(cont2_offset) * 35
        cont2_y = self.y + math.sin(cont2_offset) * 15
        if self.is_visible(cont2_offset):
            pygame.draw.ellipse(screen, self.land_green, 
                              (cont2_x - 20, cont2_y - 30, 40, 60))
            # Add mountain ranges
            pygame.draw.ellipse(screen, self.land_brown, 
                              (cont2_x - 15, cont2_y - 20, 30, 15))
        
        # Continent 3 (Asia-like)
        cont3_offset = continent_offset + math.pi * 1.3
        cont3_x = self.x + math.cos(cont3_offset) * 25
        cont3_y = self.y + math.sin(cont3_offset) * 25
        if self.is_visible(cont3_offset):
            pygame.draw.ellipse(screen, self.land_green, 
                              (cont3_x - 25, cont3_y - 20, 50, 40))
            # Add varied terrain
            pygame.draw.ellipse(screen, self.land_brown, 
                              (cont3_x - 20, cont3_y - 15, 25, 20))
    
    def draw_ice_caps(self, screen):
        """Draw polar ice caps"""
        # North pole
        pygame.draw.circle(screen, self.ice_white, 
                          (int(self.x), int(self.y - self.radius * 0.7)), 15)
        # South pole
        pygame.draw.circle(screen, self.ice_white, 
                          (int(self.x), int(self.y + self.radius * 0.7)), 12)
    
    def is_visible(self, angle):
        """Check if continent is on the visible side of Earth"""
        # Simple check - continent is visible if it's on the front hemisphere
        normalized_angle = angle % (2 * math.pi)
        return normalized_angle < math.pi
    
    def is_clicked(self, pos):
        """Check if Earth was clicked"""
        mouse_x, mouse_y = pos
        distance = math.sqrt((mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2)
        return distance <= self.radius
    
    def get_info(self):
        """Return information about Earth"""
        return """EARTH
        
Our home planet, the third planet from the Sun.
        
• Diameter: 12,742 km
• Age: 4.54 billion years
• Distance from Sun: 149.6 million km
• Atmosphere: 78% Nitrogen, 21% Oxygen
• Surface: 71% water, 29% land
• Satellites: 1 (Moon)

Earth is the only known planet with life,
supporting millions of species in diverse
ecosystems across land, sea, and air."""
