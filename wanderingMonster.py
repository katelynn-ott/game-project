# wanderingMonster.py
# 4/18/25

"""wanderingMonster.py

Defines the WanderingMonster class for the Python adventure game.
Each monster has a position, color, and gold value. Monsters can move
randomly on the map grid and be serialized for game saving/loading.
"""

import random
class WanderingMonster:
    """
        Initialize a wandering monster.

        Args:
            position (tuple): (x, y) grid position of the monster.
            color (tuple): RGB color of the monster.
            gold (int): Gold carried by the monster.
        """
    def __init__(self, position, color, gold, name="Monster", hp=10):
        self.position = position
        self.color = color
        self.gold = gold
        self.name = name
        self.hp = hp

    def move(self):
        """Move the monster randomly in one of the four directions."""
        import random
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        new_x = max(0, min(self.position[0] + dx, 9))
        new_y = max(0, min(self.position[1] + dy, 9))
        self.position = (new_x, new_y)

    def to_dict(self):
        """Convert the monster to a dictionary for saving."""
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
            data (dict): Dictionary with keys 'position', 'color', 'gold'.

        Returns:
            WanderingMonster: A new monster object.
        """
        return cls(
            tuple(data["position"]),
            data["color"],
            data["gold"],
            data["name"],
            data["hp"]
        )


