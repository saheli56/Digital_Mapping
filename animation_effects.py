import pygame
import math

class RadiationWaves:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.waves = []
        self.wave_timer = 0
        self.wave_interval = 30  # frames between new waves
        
        # Realistic wave properties
        self.max_radius = 80
        self.wave_speed = 1.5
        self.wave_color = (0, 255, 100, 30)  # Subtle green with low transparency
        
    def update(self, x, y):
        """Update radiation waves position and animation"""
        self.x = x
        self.y = y
        
        # Create new wave
        self.wave_timer += 1
        if self.wave_timer >= self.wave_interval:
            self.waves.append({'radius': 0, 'alpha': 255})
            self.wave_timer = 0
        
        # Update existing waves
        for wave in self.waves[:]:  # Use slice to avoid modification during iteration
            wave['radius'] += self.wave_speed
            wave['alpha'] -= 3  # Fade out
            
            # Remove waves that are too big or faded
            if wave['radius'] > self.max_radius or wave['alpha'] <= 0:
                self.waves.remove(wave)
    
    def draw(self, screen):
        """Draw radiation waves"""
        for wave in self.waves:
            if wave['alpha'] > 0:
                # Create surface with alpha for transparency
                wave_surface = pygame.Surface((wave['radius'] * 2, wave['radius'] * 2), pygame.SRCALPHA)
                wave_color = (*self.wave_color[:3], max(0, min(255, wave['alpha'])))
                
                pygame.draw.circle(wave_surface, wave_color, 
                                 (wave['radius'], wave['radius']), 
                                 wave['radius'], 2)
                
                screen.blit(wave_surface, 
                           (self.x - wave['radius'], self.y - wave['radius']))

class ConnectionLines:
    def __init__(self):
        self.pulse_offset = 0
        self.pulse_speed = 0.1
        
        # Realistic connection line properties
        self.line_color = (100, 149, 237)    # Cornflower blue - more subtle
        self.pulse_color = (255, 165, 0)     # Orange pulse - less intense
        
    def update(self, satellite_pos, car_pos, mobile_pos):
        """Update connection line animations"""
        self.satellite_pos = satellite_pos
        self.car_pos = car_pos
        self.mobile_pos = mobile_pos
        
        self.pulse_offset += self.pulse_speed
        if self.pulse_offset >= 2 * math.pi:
            self.pulse_offset = 0
    
    def draw(self, screen):
        """Draw animated connection lines"""
        if not hasattr(self, 'satellite_pos'):
            return
            
        # Draw line from satellite to car
        self.draw_pulsing_line(screen, self.satellite_pos, self.car_pos, 0)
        
        # Draw line from satellite to mobile
        self.draw_pulsing_line(screen, self.satellite_pos, self.mobile_pos, math.pi)
    
    def draw_pulsing_line(self, screen, start_pos, end_pos, phase_offset):
        """Draw a single pulsing connection line"""
        # Base line
        pygame.draw.line(screen, self.line_color, start_pos, end_pos, 2)
        
        # Calculate pulse position
        pulse_progress = (math.sin(self.pulse_offset + phase_offset) + 1) / 2
        
        # Calculate pulse position along the line
        pulse_x = start_pos[0] + (end_pos[0] - start_pos[0]) * pulse_progress
        pulse_y = start_pos[1] + (end_pos[1] - start_pos[1]) * pulse_progress
        
        # Draw pulse dot
        pygame.draw.circle(screen, self.pulse_color, 
                          (int(pulse_x), int(pulse_y)), 5)
        
        # Draw glow effect around pulse
        for radius in range(8, 15, 2):
            alpha = max(0, 100 - (radius - 5) * 20)
            if alpha > 0:
                glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                glow_color = (*self.pulse_color, alpha)
                pygame.draw.circle(glow_surface, glow_color, 
                                 (radius, radius), radius)
                screen.blit(glow_surface, 
                           (pulse_x - radius, pulse_y - radius))
