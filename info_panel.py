import pygame

class InfoPanel:
    def __init__(self):
        self.width = 300
        self.height = 400
        self.x = 50
        self.y = 50
        
        # Colors
        self.bg_color = (240, 240, 240)
        self.border_color = (0, 0, 0)
        self.text_color = (0, 0, 0)
        self.title_color = (0, 50, 100)
        
        # Font
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 24)
        self.text_font = pygame.font.Font(None, 18)
        
    def draw(self, screen, info_text):
        """Draw the information panel with text"""
        # Draw panel background
        panel_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.bg_color, panel_rect)
        pygame.draw.rect(screen, self.border_color, panel_rect, 3)
        
        # Draw close button
        close_button = pygame.Rect(self.x + self.width - 25, self.y + 5, 20, 20)
        pygame.draw.rect(screen, (200, 50, 50), close_button)
        pygame.draw.rect(screen, self.border_color, close_button, 2)
        
        # Draw X in close button
        pygame.draw.line(screen, (255, 255, 255),
                        (close_button.x + 5, close_button.y + 5),
                        (close_button.x + 15, close_button.y + 15), 2)
        pygame.draw.line(screen, (255, 255, 255),
                        (close_button.x + 15, close_button.y + 5),
                        (close_button.x + 5, close_button.y + 15), 2)
        
        # Render text
        self.render_text(screen, info_text)
    
    def render_text(self, screen, text):
        """Render multi-line text in the panel"""
        lines = text.split('\n')
        y_offset = self.y + 40
        line_height = 22
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                y_offset += line_height // 2
                continue
                
            # Use title font for the first non-empty line
            if i == 0 or (i == 1 and not lines[0].strip()):
                font = self.title_font
                color = self.title_color
            else:
                font = self.text_font
                color = self.text_color
            
            # Word wrap for long lines
            words = line.split(' ')
            current_line = ""
            
            for word in words:
                test_line = current_line + word + " "
                text_width = font.size(test_line)[0]
                
                if text_width < self.width - 20:  # Leave margin
                    current_line = test_line
                else:
                    if current_line:
                        text_surface = font.render(current_line.strip(), True, color)
                        screen.blit(text_surface, (self.x + 10, y_offset))
                        y_offset += line_height
                    current_line = word + " "
            
            # Render remaining text
            if current_line:
                text_surface = font.render(current_line.strip(), True, color)
                screen.blit(text_surface, (self.x + 10, y_offset))
                y_offset += line_height
    
    def is_clicked(self, pos):
        """Check if the panel (or close button) was clicked"""
        mouse_x, mouse_y = pos
        
        # Check if clicked inside panel
        if (self.x <= mouse_x <= self.x + self.width and
            self.y <= mouse_y <= self.y + self.height):
            
            # Check if close button was clicked
            close_x = self.x + self.width - 25
            close_y = self.y + 5
            if (close_x <= mouse_x <= close_x + 20 and
                close_y <= mouse_y <= close_y + 20):
                return False  # Close button clicked
            
            return True  # Panel clicked (don't close)
        
        return False  # Clicked outside panel
