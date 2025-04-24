# Katelynn Ottmann
# game.py
# 04/18/25

"""game.py

Main game loop and Pygame display for the Python adventure game.
Initializes game state, handles player input, movement, combat, shop,
and interactions with wandering monsters on a persistent map grid.
"""
import pygame
import os
import sys
import random
from wanderingMonster import WanderingMonster
import gamefunctions
import json
equipped_weapon = None
owned_weapons = []
pygame.init()
pygame.mixer.init()

sound_folder = os.path.join("sounds")
battle_start_sound = pygame.mixer.Sound(os.path.join(sound_folder, "encounter.wav"))
winner_sound = pygame.mixer.Sound(os.path.join(sound_folder, "winner.wav"))
loser_sound = pygame.mixer.Sound(os.path.join(sound_folder, "loser.wav"))
entering_shop_sound = pygame.mixer.Sound(os.path.join(sound_folder, "door.wav"))
shop_sound = pygame.mixer.Sound(os.path.join(sound_folder, "coins.wav"))
step_sound = pygame.mixer.Sound(os.path.join(sound_folder, "walking.wav"))

CELL_SIZE = 50
MAP_WIDTH = 10
MAP_HEIGHT = 10
SCREEN_WIDTH = CELL_SIZE * MAP_WIDTH
SCREEN_HEIGHT = CELL_SIZE * MAP_HEIGHT
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adventure Game")
font = pygame.font.SysFont(None, 36)

# Try loading images
try:
    player_image = pygame.image.load("Old hero.png")
    player_image = pygame.transform.scale(player_image, (160, 160))
except:
    player_image = None

monster_images = {}
monster_image_files = {
    "Sprite": "mon1_sprite.png",
    "Slime": "glooRotated.png",
    "Ghost": "flameball-32x32.png"
}
for name, file in monster_image_files.items():
    try:
        img = pygame.image.load(file)
        monster_images[name] = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
    except:
        monster_images[name] = None

def draw_status_bar(hp, gold):
    hp_text = font.render(f"HP: {hp}", True, (0, 0, 0))
    gold_text = font.render(f"Gold: {gold}", True, (0, 0, 0))
    weapon_text = font.render(f"Weapon: {equipped_weapon if equipped_weapon else 'None'}", True, (0, 0, 0))
    screen.blit(hp_text, (10, 10))
    screen.blit(gold_text, (10, 40))
    screen.blit(weapon_text, (10, 70))


player_name = input("What is your name? ")
gamefunctions.print_welcome(player_name, SCREEN_WIDTH // 10)

loaded = gamefunctions.load_game()
if loaded:
    player_pos = tuple(loaded["player_pos"])
    player_hp = loaded["player_hp"]
    player_gold = loaded["player_gold"]
    monsters = [WanderingMonster.from_dict(m) for m in loaded["monsters"]]
else:
    player_pos = (5, 5)
    player_hp = 30
    player_gold = 20
    monsters = gamefunctions.generate_monsters()

def game_loop():
    global player_pos, player_hp, player_gold, monsters
    turn_counter = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)
        draw_status_bar(player_hp, player_gold)

        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        # Draw player
        if player_image:
            screen.blit(player_image, (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE))
        else:
            pygame.draw.rect(screen, PLAYER_COLOR,
                             (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Draw monsters
        for monster in monsters:
            if monster_images.get(monster.name):
                screen.blit(monster_images[monster.name],
                            (monster.position[0] * CELL_SIZE, monster.position[1] * CELL_SIZE))
            else:
                pygame.draw.rect(screen, monster.color,
                                 (monster.position[0] * CELL_SIZE, monster.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamefunctions.save_game(player_pos, player_hp, player_gold, monsters)
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        new_pos = list(player_pos)
        moved = False

        if keys[pygame.K_LEFT]: new_pos[0] -= 1; moved = True
        elif keys[pygame.K_RIGHT]: new_pos[0] += 1; moved = True
        elif keys[pygame.K_UP]: new_pos[1] -= 1; moved = True
        elif keys[pygame.K_DOWN]: new_pos[1] += 1; moved = True

        if moved and new_pos != list(player_pos):
            step_sound.play()

        

        new_pos[0] = max(0, min(new_pos[0], MAP_WIDTH - 1))
        new_pos[1] = max(0, min(new_pos[1], MAP_HEIGHT - 1))
        player_pos = tuple(new_pos)

        if turn_counter % 2 == 0:
            for monster in monsters:
                monster.move()

        remaining_monsters = []
        encountered = False
        for monster in monsters:
            if monster.position == player_pos and not encountered:
                battle_start_sound.play()
                print(f"You encountered a {monster.name} with {monster.hp} HP!")
                while True:
                    action = input("Do you want to (f)ight, (r)un, or (t)own? ").strip().lower()
                    if action == 'f':
                        result = gamefunctions.fight_monster(monster)
                        if result == "win":
                            winner_sound.play()
                            print(f"You defeated the {monster.name} and gained {monster.gold} gold!")
                            player_gold += monster.gold
                        elif result == "lose":
                            loser_sound.play()
                            print(f"The {monster.name} hit you! You lost 5 HP.")
                            player_hp -= 5
                            remaining_monsters.append(monster)
                        break
                    elif action == 'r':
                        print(f"You ran away from the {monster.name}.")
                        remaining_monsters.append(monster)
                        break
                    elif action == 't':
                        print("Returning to town...")
                        return  
                    else:
                        print("Invalid choice. Please enter 'f', 'r', or 't'.")
                encountered = True
            else:
                remaining_monsters.append(monster)

        monsters = remaining_monsters

        if not monsters:
            print("All monsters defeated! New ones are appearing...")
            monsters = gamefunctions.generate_monsters()

        if player_hp <= 0:
            print("Game Over. You died.")
            gamefunctions.save_game(player_pos, player_hp, player_gold, monsters)
            running = False

        turn_counter += 1
        clock.tick(15)


# Town loop
while True:
    print("\n--- Town Square ---")
    print("1. Visit the shop")
    print("2. Rest at the inn")
    print("3. Equip your weapon")
    print("4. Leave town and explore")
    print("5. Save and quit")
    print("6. Quit without saving")

    choice = input("What would you like to do? ").strip().lower()

    if choice in ["1", "shop", "visit the shop"]:
        entering_shop_sound.play()
        player_gold = gamefunctions.shop(player_gold)
    elif choice in ["2", "rest", "inn", "rest at the inn"]:
        player_hp, player_gold = gamefunctions.sleep(player_hp, player_gold)
    elif choice in ["3", "equip", "equip weapon", "equip your weapon"]:
        gamefunctions.equip_weapon()
    elif choice in ["4", "explore", "leave town", "leave town and explore"]:
        game_loop()  
    elif choice in ["5", "save", "save and quit"]:
        gamefunctions.save_game(player_pos, player_hp, player_gold, monsters)
        print("Game saved. Goodbye!")
        break
    elif choice in ["6", "quit", "quit without saving"]:
        print("Quitting without saving. Goodbye!")
        break
    else:
        print("Invalid choice.")

