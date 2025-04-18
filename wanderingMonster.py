#wanderingMonster.py
#Katelynn Ottmann
import random

GRID_WIDTH = 10
GRID_HEIGHT = 10
TOWN_SQUARE = (0, 0)

class WanderingMonster:
    MONSTER_TYPES = {
        'Zombie': 'red',
        'Slime': 'green',
        'Goblin': 'purple',
        'Orc': 'orange'
    }

    def __init__(self, name, monster_type, gold, location):
        self.name = name
        self.monster_type = monster_type
        self.color = self.MONSTER_TYPES.get(monster_type, 'gray')
        self.gold = gold
        self.location = location

    def move(self):
        x, y = self.location
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
                if (new_x, new_y) != TOWN_SQUARE:
                    self.location = (new_x, new_y)
                    break

    @classmethod
    def new_random_monster(cls, player_pos, existing_monsters):
        name = random.choice(['Gronk', 'Blib', 'Skur', 'Mog'])
        monster_type = random.choice(list(cls.MONSTER_TYPES.keys()))
        gold = random.randint(5, 20)

        while True:
            location = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if location != TOWN_SQUARE and location != player_pos and location not in [m.location for m in existing_monsters]:
                break

        return cls(name, monster_type, gold, location)
