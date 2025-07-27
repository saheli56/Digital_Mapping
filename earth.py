import pygame
import math
import os

class Earth:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 80
        self.angle = 0
        self.rotation_speed = 0.5  # Slower, more realistic rotation
        self.visible = True  # Earth visibility flag
        
        # Load Earth image
        self.load_earth_image()
        
        # Create rotated surface for smooth rotation
        self.rotated_earth = None
        
    def load_earth_image(self):
        """Load and prepare the Earth image"""
        try:
            # Get the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            earth_path = os.path.join(script_dir, 'assets', 'earth_hd.jpg')
            
            # Load the Earth image
            self.original_earth = pygame.image.load(earth_path)
            
            # Scale the image to fit our desired radius (diameter = 2 * radius)
            earth_size = self.radius * 2
            self.original_earth = pygame.transform.scale(self.original_earth, (earth_size, earth_size))
            
            # Convert for better performance
            self.original_earth = self.original_earth.convert()
            
            # Create circular mask for the Earth image
            self.create_circular_mask()
            
            print(f"Successfully loaded Earth image from: {earth_path}")
            
        except pygame.error as e:
            print(f"Could not load Earth image: {e}")
            # Fallback to creating a simple circle if image fails to load
            self.original_earth = None
            self.create_fallback_earth()
            
    def create_fallback_earth(self):
        """Create a simple fallback Earth if image loading fails"""
        earth_size = self.radius * 2
        self.original_earth = pygame.Surface((earth_size, earth_size), pygame.SRCALPHA)
        # Draw a simple blue circle as fallback
        pygame.draw.circle(self.original_earth, (0, 100, 200), (self.radius, self.radius), self.radius)
        
    def create_circular_mask(self):
        """Create a circular mask to make Earth appear round"""
        earth_size = self.radius * 2
        
        # Convert image for better performance
        self.original_earth = self.original_earth.convert_alpha()
        
        # Create the final circular Earth surface
        circular_earth = pygame.Surface((earth_size, earth_size), pygame.SRCALPHA)
        circular_earth.fill((0, 0, 0, 0))  # Transparent background
        
        # Use pygame.mask for better performance
        center_x, center_y = self.radius, self.radius
        radius_squared = self.radius * self.radius
        
        # Copy pixels within the circle from original earth
        for x in range(earth_size):
            for y in range(earth_size):
                # Use squared distance to avoid sqrt calculation
                distance_squared = (x - center_x) ** 2 + (y - center_y) ** 2
                if distance_squared <= radius_squared:
                    # Copy pixel from original earth
                    pixel = self.original_earth.get_at((x, y))
                    circular_earth.set_at((x, y), pixel)
        
        self.original_earth = circular_earth
        print("Created circular Earth mask successfully")
        
    def update(self):
        """Update Earth rotation"""
        self.angle += self.rotation_speed
        if self.angle >= 360:
            self.angle = 0
            
    def draw(self, screen):
        """Draw the rotating Earth using the actual image"""
        if not self.visible:
            return
            
        if self.original_earth:
            # Create rotated version of the Earth image
            self.rotated_earth = pygame.transform.rotate(self.original_earth, self.angle)
            
            # Get the rect of the rotated image to center it properly
            rotated_rect = self.rotated_earth.get_rect()
            rotated_rect.center = (int(self.x), int(self.y))
            
            # Add a subtle shadow/glow effect for 3D appearance
            self.draw_earth_shadow(screen)
            
            # Draw the rotated Earth image
            screen.blit(self.rotated_earth, rotated_rect)
            
            # Draw a circular border to ensure perfect circle appearance
            pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), self.radius, 2)
            
            # Add a subtle rim light effect
            self.draw_earth_rim_light(screen)
        else:
            # Fallback to vector graphics if image failed to load
            self.draw_vector_earth(screen)
            
    def draw_vector_earth(self, screen):
        """Fallback vector-based Earth drawing"""
        # Draw main Earth body (oceans)
        pygame.draw.circle(screen, (25, 25, 112), (int(self.x), int(self.y)), self.radius)
        
        # Draw simple continents
        continent_offset = math.radians(self.angle)
        cont1_x = self.x + math.cos(continent_offset) * 30
        cont1_y = self.y + math.sin(continent_offset) * 20
        if self.is_visible(continent_offset):
            pygame.draw.ellipse(screen, (34, 139, 34), 
                              (cont1_x - 15, cont1_y - 25, 30, 50))
        
        # Draw Earth outline
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), self.radius, 2)
    
    def draw_earth_shadow(self, screen):
        """Draw a subtle shadow behind Earth for 3D effect"""
        shadow_offset = 3
        shadow_alpha = 80
        
        # Create shadow surface
        shadow_surface = pygame.Surface((self.radius * 2 + 10, self.radius * 2 + 10), pygame.SRCALPHA)
        pygame.draw.circle(shadow_surface, (0, 0, 0, shadow_alpha), 
                          (self.radius + 5, self.radius + 5), self.radius + 2)
        
        # Draw shadow slightly offset
        shadow_rect = shadow_surface.get_rect()
        shadow_rect.center = (int(self.x + shadow_offset), int(self.y + shadow_offset))
        screen.blit(shadow_surface, shadow_rect)
    
    def draw_earth_rim_light(self, screen):
        """Draw a subtle rim light effect for 3D appearance"""
        # Create rim light surface
        rim_surface = pygame.Surface((self.radius * 2 + 6, self.radius * 2 + 6), pygame.SRCALPHA)
        
        # Draw outer glow
        pygame.draw.circle(rim_surface, (135, 206, 235, 30), 
                          (self.radius + 3, self.radius + 3), self.radius + 3)
        pygame.draw.circle(rim_surface, (255, 255, 255, 20), 
                          (self.radius + 3, self.radius + 3), self.radius + 1)
        
        # Draw rim light
        rim_rect = rim_surface.get_rect()
        rim_rect.center = (int(self.x), int(self.y))
        screen.blit(rim_surface, rim_rect)
    
    def is_visible(self, angle):
        """Check if continent is on the visible side of Earth (for fallback)"""
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
