# Katelynn Ottmann
#wanderingMonster
import pygame
import random

"""
Defines the WanderingMonster class for the Python adventure game.
Each monster has a position, color, gold value, HP, and optional image.
Monsters can move randomly on the map grid and be serialized for saving.
"""
CELL_SIZE = 50

class WanderingMonster:
    """
    Represents a monster that wanders the map.

    Attributes:
        position (tuple): (x, y) grid position.
        color (tuple): RGB color if no image is used.
        gold (int): Gold dropped when defeated.
        name (str): Name of the monster.
        hp (int): Health points.
        image (pygame.Surface): Optional image for visual representation.
    """

    def __init__(self, position, color, gold, name="Monster", hp=10):
        """
        Initialize a wandering monster.

        Args:
            position (tuple): (x, y) position on the grid.
            color (tuple): RGB color fallback if no image is used.
            gold (int): Amount of gold the monster holds.
            name (str): Monster type/name (determines image).
            hp (int): Hit points.
        """
        self.position = position
        self.color = color
        self.gold = gold
        self.name = name
        self.hp = hp
        self.image = self.load_image()

    def load_image(self):
        """
        Load and scale an image for the monster based on its name.
        Returns:
            pygame.Surface or None: Loaded and scaled image or None if not found.
        """
        try:
            if self.name == "Sprite":
                img = pygame.image.load("mon1_sprite.png")
            elif self.name == "Slime":
                img = pygame.image.load("glooRotated.png")
            elif self.name == "Ghost":
                img = pygame.image.load("flameball-32x32.png")
            else:
                return None
            return pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))  
        except Exception as e:
            print(f"Error loading image for {self.name}: {e}")
            return None

    def move(self):
        """
        Move the monster randomly in one of the four directions.
        """
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        new_x = max(0, min(self.position[0] + dx, 9))
        new_y = max(0, min(self.position[1] + dy, 9))
        self.position = (new_x, new_y)

    def to_dict(self):
        """
        Convert the monster to a dictionary for saving.

        Returns:
            dict: Dictionary representation of the monster.
        """
        return {
            "position": self.position,
            "color": self.color,
            "gold": self.gold,
            "name": self.name,
            "hp": self.hp
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a WanderingMonster from saved data.

        Args:
            data (dict): Dictionary with keys 'position', 'color', 'gold', 'name', 'hp'.

        Returns:
            WanderingMonster: A new monster object.
        """
        return cls(
            data["position"],
            tuple(data["color"]),
            data["gold"],
            data.get("name", "Monster"),
            data.get("hp", 10)
        )
