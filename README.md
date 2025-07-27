# Digital Mapping - Interactive Earth Scene

An educational 2D animated interactive scene built with Python and Pygame, demonstrating satellite communication and digital mapping concepts.

## Features

### Interactive Elements
- **Rotating Earth**: Realistic planet with continents, oceans, and polar ice caps
- **Satellite**: Positioned at the top with rotating solar panels and subtle radiation waves
- **Smart Car**: Emerges from the school and moves across the grassland
- **Mobile Phone**: Positioned near ground level with animated signal bars and screen
- **School Building**: Realistic architecture with detailed windows and doors

### Realistic Graphics
- **Earth**: High-definition Earth image with realistic rotation and 3D shadow effects
- **Sky**: Natural sky blue background
- **Grassland**: Realistic green grass with varied texture and natural colors
- **Satellite**: Dark gray body with blue solar panels and proper positioning
- **Buildings**: Natural brick and material colors
- **Vehicles**: Realistic car colors with proper lighting

### Animations
- Earth rotates with visible continents
- Satellite rotates with extending solar panels
- Radiation waves emanate from the satellite
- Animated connection lines between satellite, car, and mobile phone
- Car moves smoothly across the screen
- Mobile phone has pulsing screen and signal indicators

### Information System
- Click any element to view detailed information
- Info panel with close button
- Educational content about each component

## How to Use

1. **Start the Application**: Run `python main.py`
2. **Activate the Scene**: Click on the rotating Earth
3. **Explore Elements**: Click on any element (Earth, Satellite, Car, Mobile, School) to learn more
4. **Close Info Panels**: Click the X button or click outside the panel

## Controls

- **Left Mouse Click**: Interact with elements
- **Close Info Panel**: Click X button or outside panel area
- **Exit**: Close the window or press ESC

## Educational Content

Each element provides information about:
- Technical specifications
- Real-world applications
- Role in digital mapping and satellite communication
- Educational value for understanding modern technology

## File Structure

```
Digital_mapping/
├── main.py              # Main game loop and coordination
├── earth.py             # Earth class with image loading and rotation
├── satellite.py         # Satellite with solar panels and rotation
├── car.py              # Moving car with GPS capabilities
├── mobile.py           # Mobile phone with signal animations
├── school.py           # School building with detailed architecture
├── info_panel.py       # Information display system
├── animation_effects.py # Radiation waves and connection lines
├── assets/             # Image assets folder
│   └── earth_hd.jpg    # High-definition Earth image
└── README.md           # This file
```

## Requirements

- Python 3.7+
- Pygame 2.0+

## Installation

```bash
pip install pygame
```

## Running the Application

```bash
python main.py
```

## Educational Objectives

This interactive scene teaches:
- Satellite communication principles
- GPS and navigation technology
- Digital mapping concepts
- Real-world applications of satellite technology
- Interactive learning through visualization

Perfect for educational environments, science fairs, or anyone interested in learning about satellite technology and digital mapping in an engaging way.
