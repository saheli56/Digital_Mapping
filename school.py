import pygame

class School:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 140
        self.height = 90
        
        # Realistic building colors
        self.brick_red = (139, 69, 19)        # Saddle brown for brick
        self.brick_dark = (101, 50, 15)       # Dark brick shadow
        self.brick_light = (160, 82, 25)      # Light brick highlight
        self.mortar_gray = (192, 192, 192)    # Mortar between bricks
        self.roof_dark = (64, 64, 64)         # Dark gray roof
        self.roof_tile = (96, 96, 96)         # Roof tile pattern
        self.door_brown = (80, 50, 20)        # Dark brown door
        self.door_handle = (255, 215, 0)      # Gold door handle
        self.window_glass = (135, 206, 235)   # Sky blue windows
        self.window_frame = (255, 255, 255)   # White window frames
        self.window_shadow = (100, 100, 150)  # Window interior shadow
        self.sign_white = (248, 248, 255)     # Ghost white for sign
        self.sign_text = (0, 0, 0)            # Black text
        self.foundation_gray = (105, 105, 105) # Foundation
        
        # Initialize font for sign
        pygame.font.init()
        self.sign_font = pygame.font.Font(None, 16)
        
    def draw(self, screen):
        """Draw the realistic school building with detailed architecture"""
        # Draw foundation
        foundation_rect = pygame.Rect(self.x - self.width//2 - 5, 
                                     self.y + self.height//2 - 5,
                                     self.width + 10, 10)
        pygame.draw.rect(screen, self.foundation_gray, foundation_rect)
        
        # Draw building shadow for depth
        shadow_rect = pygame.Rect(self.x - self.width//2 + 3, 
                                 self.y - self.height//2 + 3,
                                 self.width, self.height)
        pygame.draw.rect(screen, self.brick_dark, shadow_rect)
        
        # Draw main building with brick pattern
        building_rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, 
                                   self.width, self.height)
        pygame.draw.rect(screen, self.brick_red, building_rect)
        
        # Draw realistic brick pattern
        self.draw_brick_pattern(screen, building_rect)
        
        # Draw detailed roof
        self.draw_roof(screen)
        
        # Draw windows with realistic details
        self.draw_windows(screen)
        
        # Draw detailed entrance door
        self.draw_entrance(screen)
        
        # Draw school sign with text
        self.draw_school_sign(screen)
        
        # Draw chimney
        self.draw_chimney(screen)
        
        # Draw building outline
        pygame.draw.rect(screen, (0, 0, 0), building_rect, 2)
    
    def draw_brick_pattern(self, screen, building_rect):
        """Draw realistic brick pattern on the building"""
        brick_height = 8
        brick_width = 20
        
        # Draw horizontal mortar lines
        for y in range(building_rect.y, building_rect.y + building_rect.height, brick_height):
            pygame.draw.line(screen, self.mortar_gray,
                           (building_rect.x, y), 
                           (building_rect.x + building_rect.width, y), 1)
        
        # Draw vertical mortar lines with offset pattern
        for row in range(building_rect.height // brick_height):
            y = building_rect.y + row * brick_height
            offset = (brick_width // 2) if row % 2 == 1 else 0
            
            for x in range(building_rect.x + offset, 
                          building_rect.x + building_rect.width, brick_width):
                if x < building_rect.x + building_rect.width:
                    pygame.draw.line(screen, self.mortar_gray,
                                   (x, y), (x, y + brick_height), 1)
                    
                    # Add brick highlights and shadows for 3D effect
                    brick_rect = pygame.Rect(x + 1, y + 1, 
                                           min(brick_width - 2, 
                                               building_rect.x + building_rect.width - x - 2), 
                                           brick_height - 2)
                    if brick_rect.width > 0:
                        # Highlight top edge
                        pygame.draw.line(screen, self.brick_light,
                                       (brick_rect.x, brick_rect.y),
                                       (brick_rect.x + brick_rect.width, brick_rect.y), 1)
                        # Shadow bottom edge
                        pygame.draw.line(screen, self.brick_dark,
                                       (brick_rect.x, brick_rect.y + brick_rect.height - 1),
                                       (brick_rect.x + brick_rect.width, brick_rect.y + brick_rect.height - 1), 1)
    
    def draw_roof(self, screen):
        """Draw detailed roof with tiles and gutters"""
        # Main roof shape
        roof_points = [
            (self.x - self.width//2 - 15, self.y - self.height//2),
            (self.x, self.y - self.height//2 - 25),
            (self.x + self.width//2 + 15, self.y - self.height//2)
        ]
        pygame.draw.polygon(screen, self.roof_dark, roof_points)
        
        # Roof tile pattern
        for i in range(5):
            tile_y = self.y - self.height//2 - 20 + i * 4
            left_x = self.x - (self.width//2 + 10) + i * 2
            right_x = self.x + (self.width//2 + 10) - i * 2
            pygame.draw.line(screen, self.roof_tile,
                           (left_x, tile_y), (right_x, tile_y), 2)
        
        # Roof ridge
        pygame.draw.line(screen, (40, 40, 40),
                        (self.x - 10, self.y - self.height//2 - 25),
                        (self.x + 10, self.y - self.height//2 - 25), 3)
        
        # Gutters
        pygame.draw.line(screen, (80, 80, 80),
                        (self.x - self.width//2 - 15, self.y - self.height//2),
                        (self.x + self.width//2 + 15, self.y - self.height//2), 2)
    
    def draw_chimney(self, screen):
        """Draw a realistic chimney"""
        chimney_rect = pygame.Rect(self.x + self.width//3, self.y - self.height//2 - 35,
                                  12, 25)
        pygame.draw.rect(screen, self.brick_red, chimney_rect)
        pygame.draw.rect(screen, self.brick_dark, chimney_rect, 1)
        
        # Chimney cap
        cap_rect = pygame.Rect(chimney_rect.x - 2, chimney_rect.y - 3,
                              chimney_rect.width + 4, 3)
        pygame.draw.rect(screen, self.roof_dark, cap_rect)

    def draw_windows(self, screen):
        """Draw realistic school windows with detailed frames and reflections"""
        window_width = 18
        window_height = 24
        
        # First floor windows
        window_positions = [
            # Left side windows
            (self.x - self.width//2 + 20, self.y - 5),
            (self.x - self.width//2 + 45, self.y - 5),
            # Right side windows
            (self.x + 15, self.y - 5),
            (self.x + 40, self.y - 5),
        ]
        
        for window_x, window_y in window_positions:
            # Window shadow/depth
            shadow_rect = pygame.Rect(window_x + 1, window_y + 1, window_width, window_height)
            pygame.draw.rect(screen, self.window_shadow, shadow_rect)
            
            # Main window frame
            frame_rect = pygame.Rect(window_x, window_y, window_width, window_height)
            pygame.draw.rect(screen, self.window_frame, frame_rect)
            
            # Glass area
            glass_rect = pygame.Rect(window_x + 2, window_y + 2, 
                                   window_width - 4, window_height - 4)
            pygame.draw.rect(screen, self.window_glass, glass_rect)
            
            # Window reflection
            reflection_rect = pygame.Rect(glass_rect.x + 1, glass_rect.y + 1,
                                        glass_rect.width // 2, glass_rect.height // 3)
            pygame.draw.rect(screen, (200, 230, 255), reflection_rect)
            
            # Window cross frame
            # Vertical bar
            pygame.draw.line(screen, self.window_frame,
                           (window_x + window_width//2, window_y + 2),
                           (window_x + window_width//2, window_y + window_height - 2), 2)
            # Horizontal bar
            pygame.draw.line(screen, self.window_frame,
                           (window_x + 2, window_y + window_height//2),
                           (window_x + window_width - 2, window_y + window_height//2), 2)
            
            # Window sill
            sill_rect = pygame.Rect(window_x - 2, window_y + window_height,
                                   window_width + 4, 3)
            pygame.draw.rect(screen, self.window_frame, sill_rect)
        
        # Second floor windows (smaller)
        upper_window_width = 15
        upper_window_height = 18
        upper_positions = [
            (self.x - self.width//2 + 25, self.y - self.height//2 + 15),
            (self.x - 5, self.y - self.height//2 + 15),
            (self.x + 25, self.y - self.height//2 + 15),
        ]
        
        for window_x, window_y in upper_positions:
            frame_rect = pygame.Rect(window_x, window_y, upper_window_width, upper_window_height)
            pygame.draw.rect(screen, self.window_frame, frame_rect)
            
            glass_rect = pygame.Rect(window_x + 2, window_y + 2, 
                                   upper_window_width - 4, upper_window_height - 4)
            pygame.draw.rect(screen, self.window_glass, glass_rect)
            pygame.draw.rect(screen, self.window_frame, frame_rect, 1)

    def draw_entrance(self, screen):
        """Draw detailed school entrance with steps and door"""
        # Entrance steps
        for i in range(3):
            step_rect = pygame.Rect(self.x - 25 + i * 2, 
                                   self.y + self.height//2 - 8 - i * 3,
                                   50 - i * 4, 4)
            pygame.draw.rect(screen, self.foundation_gray, step_rect)
            pygame.draw.rect(screen, (80, 80, 80), step_rect, 1)
        
        # Door frame
        door_frame_rect = pygame.Rect(self.x - 15, self.y + self.height//2 - 45,
                                     30, 40)
        pygame.draw.rect(screen, self.window_frame, door_frame_rect)
        
        # Main door
        door_rect = pygame.Rect(self.x - 13, self.y + self.height//2 - 43,
                               26, 36)
        pygame.draw.rect(screen, self.door_brown, door_rect)
        
        # Door panels
        panel1 = pygame.Rect(door_rect.x + 2, door_rect.y + 2, 
                            door_rect.width - 4, door_rect.height // 2 - 2)
        panel2 = pygame.Rect(door_rect.x + 2, door_rect.y + door_rect.height // 2 + 1,
                            door_rect.width - 4, door_rect.height // 2 - 3)
        
        pygame.draw.rect(screen, (100, 60, 30), panel1)
        pygame.draw.rect(screen, (100, 60, 30), panel2)
        pygame.draw.rect(screen, self.door_brown, panel1, 2)
        pygame.draw.rect(screen, self.door_brown, panel2, 2)
        
        # Door handle and lock
        handle_x = door_rect.x + door_rect.width - 6
        handle_y = door_rect.y + door_rect.height // 2
        pygame.draw.circle(screen, self.door_handle, (handle_x, handle_y), 3)
        pygame.draw.circle(screen, (200, 180, 0), (handle_x, handle_y), 2)
        
        # Door window (small)
        door_window = pygame.Rect(door_rect.x + 6, door_rect.y + 6, 8, 12)
        pygame.draw.rect(screen, self.window_glass, door_window)
        pygame.draw.rect(screen, self.window_frame, door_window, 1)
    
    def draw_school_sign(self, screen):
        """Draw realistic school identification sign with text"""
        # Sign post
        post_rect = pygame.Rect(self.x - 2, self.y - self.height//2 - 65, 4, 25)
        pygame.draw.rect(screen, (101, 67, 33), post_rect)
        
        # Main sign board (made larger to accommodate longer text)
        sign_rect = pygame.Rect(self.x - 50, self.y - self.height//2 - 65, 100, 30)
        pygame.draw.rect(screen, self.sign_white, sign_rect)
        pygame.draw.rect(screen, self.sign_text, sign_rect, 2)
        
        # Sign shadow for depth
        shadow_rect = pygame.Rect(sign_rect.x + 1, sign_rect.y + 1, 
                                 sign_rect.width, sign_rect.height)
        pygame.draw.rect(screen, (200, 200, 200), shadow_rect)
        pygame.draw.rect(screen, self.sign_white, sign_rect)
        pygame.draw.rect(screen, self.sign_text, sign_rect, 2)
        
        # School text - split into two lines to fit properly
        try:
            # First line
            text_surface = self.sign_font.render("VIDYASHILP PUBLIC", True, self.sign_text)
            text_rect = text_surface.get_rect(center=(self.x, self.y - self.height//2 - 55))
            screen.blit(text_surface, text_rect)
            
            # Second line
            text_surface2 = self.sign_font.render("SCHOOL", True, self.sign_text)
            text_rect2 = text_surface2.get_rect(center=(self.x, self.y - self.height//2 - 45))
            screen.blit(text_surface2, text_rect2)
        except:
            # Fallback if font fails
            pygame.draw.rect(screen, self.sign_text, 
                            (self.x - 45, self.y - self.height//2 - 58, 90, 3))
            pygame.draw.rect(screen, self.sign_text, 
                            (self.x - 20, self.y - self.height//2 - 48, 40, 3))
    
    def is_clicked(self, pos):
        """Check if school was clicked"""
        mouse_x, mouse_y = pos
        return (self.x - self.width//2 <= mouse_x <= self.x + self.width//2 and
                self.y - self.height//2 <= mouse_y <= self.y + self.height//2)
    
    def get_info(self):
        """Return information about the school"""
        return """VIDYASHILP PUBLIC SCHOOL
        
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
