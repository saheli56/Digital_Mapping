import pygame

class School:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 120
        self.height = 80
        
        # Realistic building colors
        self.brick_red = (139, 69, 19)        # Saddle brown for brick
        self.roof_dark = (105, 105, 105)      # Dim gray for roof
        self.door_brown = (101, 67, 33)       # Dark brown door
        self.window_glass = (173, 216, 230)   # Light blue windows
        self.window_frame = (255, 255, 255)   # White window frames
        self.sign_white = (248, 248, 255)     # Ghost white for sign
        
    def draw(self, screen):
        """Draw the realistic school building"""
        # Draw main building
        pygame.draw.rect(screen, self.brick_red, 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height))
        
        # Draw roof
        roof_points = [
            (self.x - self.width//2 - 10, self.y - self.height//2),
            (self.x, self.y - self.height//2 - 20),
            (self.x + self.width//2 + 10, self.y - self.height//2)
        ]
        pygame.draw.polygon(screen, self.roof_dark, roof_points)
        
        # Draw windows
        self.draw_windows(screen)
        
        # Draw door
        door_width = 20
        door_height = 35
        door_x = self.x - door_width//2
        door_y = self.y + self.height//2 - door_height
        pygame.draw.rect(screen, self.door_brown, 
                        (door_x, door_y, door_width, door_height))
        
        # Draw door handle
        pygame.draw.circle(screen, (255, 215, 0), 
                          (door_x + door_width - 5, door_y + door_height//2), 2)
        
        # Draw school sign
        self.draw_school_sign(screen)
        
        # Draw building outline
        pygame.draw.rect(screen, (0, 0, 0), 
                        (self.x - self.width//2, self.y - self.height//2, 
                         self.width, self.height), 2)
    
    def draw_windows(self, screen):
        """Draw realistic school windows"""
        window_width = 15
        window_height = 20
        
        # Left windows
        for i in range(2):
            window_x = self.x - self.width//2 + 15 + i * 25
            window_y = self.y - self.height//2 + 15
            
            pygame.draw.rect(screen, self.window_glass, 
                           (window_x, window_y, window_width, window_height))
            pygame.draw.rect(screen, self.window_frame, 
                           (window_x, window_y, window_width, window_height), 2)
            
            # Window cross
            pygame.draw.line(screen, self.window_frame,
                           (window_x + window_width//2, window_y),
                           (window_x + window_width//2, window_y + window_height), 1)
            pygame.draw.line(screen, self.window_frame,
                           (window_x, window_y + window_height//2),
                           (window_x + window_width, window_y + window_height//2), 1)
        
        # Right windows
        for i in range(2):
            window_x = self.x + 10 + i * 25
            window_y = self.y - self.height//2 + 15
            
            pygame.draw.rect(screen, self.window_glass, 
                           (window_x, window_y, window_width, window_height))
            pygame.draw.rect(screen, self.window_frame, 
                           (window_x, window_y, window_width, window_height), 2)
            
            # Window cross
            pygame.draw.line(screen, self.window_frame,
                           (window_x + window_width//2, window_y),
                           (window_x + window_width//2, window_y + window_height), 1)
            pygame.draw.line(screen, self.window_frame,
                           (window_x, window_y + window_height//2),
                           (window_x + window_width, window_y + window_height//2), 1)
    
    def draw_school_sign(self, screen):
        """Draw realistic school identification sign"""
        sign_rect = pygame.Rect(self.x - 30, self.y - self.height//2 - 35, 60, 15)
        pygame.draw.rect(screen, self.sign_white, sign_rect)
        pygame.draw.rect(screen, (0, 0, 0), sign_rect, 2)
        
        # School text would go here (simplified as a rectangle for now)
        pygame.draw.rect(screen, (0, 0, 0), 
                        (self.x - 25, self.y - self.height//2 - 30, 50, 5))
    
    def is_clicked(self, pos):
        """Check if school was clicked"""
        mouse_x, mouse_y = pos
        return (self.x - self.width//2 <= mouse_x <= self.x + self.width//2 and
                self.y - self.height//2 <= mouse_y <= self.y + self.height//2)
    
    def get_info(self):
        """Return information about the school"""
        return """DIGITAL MAPPING SCHOOL
        
Educational institution teaching modern
geography and satellite technology.
        
• Founded: 2020
• Students: 450
• Courses: GIS, Remote Sensing, GPS
• Facilities: Computer lab, Satellite dish
• Programs: Digital cartography
• Technology: GPS tracking for buses
• Field trips: Via GPS navigation

The school uses satellite technology
for navigation, emergency systems,
and teaching digital mapping skills."""
