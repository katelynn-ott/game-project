# Katelynn Ottmann
# gamefunctions.py
# 04/18/25

"""gamefunctions.py

Contains utility functions for the Python adventure game:
- save/load game state
- print welcome message
- handle shop interactions
- generate and fight monsters
"""
import json
import random
import pygame
import os
from wanderingMonster import WanderingMonster
equipped_weapon = None
owned_weapons = []

pygame.mixer.init()
sound_folder = os.path.join("sounds")
entering_shop_sound = pygame.mixer.Sound(os.path.join(sound_folder, "door.wav"))
shop_sound = pygame.mixer.Sound(os.path.join(sound_folder, "coins.wav"))

def print_welcome(name, width):
    print("-" * (width * 2))
    print(f"Welcome, {name}, to the Adventure Game!".center(width * 2))
    print("-" * (width * 2))

def shop(player_gold):
    global owned_weapons, equipped_weapon
    entering_shop_sound.play()

    while True:
        print("\n--- Shop Menu ---")
        print(f"Current Gold: {player_gold}")
        print("----------------------")
        print("1. Potion       - 10g")
        print("2. Sword        - 15g")
        print("3. Shield       - 12g")
        print("4. Magic Scroll - 20g")
        print("5. Exit Shop")
        print("----------------------")
        choice = input("Choose an item to buy: ")

        if choice == "1":
            if player_gold >= 10:
                player_gold -= 10
                shop_sound.play()
                print("You bought a potion!")
            else:
                print("Not enough gold.")

        elif choice == "2":
            if player_gold >= 15:
                player_gold -= 15
                shop_sound.play()
                owned_weapons.append("Sword")
                print("You bought a sword!")
            else:
                print("Not enough gold.")

        elif choice == "3":
            if player_gold >= 12:
                player_gold -= 12
                shop_sound.play()
                owned_weapons.append("Shield")
                print("You bought a shield!")
            else:
                print("Not enough gold.")

        elif choice == "4":
            if player_gold >= 20:
                player_gold -= 20
                shop_sound.play()
                owned_weapons.append("Magic Scroll")
                print("You bought a magic scroll!")
            else:
                print("Not enough gold.")

        elif choice == "5":
            entering_shop_sound.play()
            print("Leaving shop...")
            break
        else:
            print("Invalid input.")

    return player_gold

def sleep(hp, gold):
    print("\nYou rest at the inn.")
    if gold >= 5:
        gold -= 5
        hp = 30
        print("You feel refreshed. HP fully restored.")
    else:
        print("Not enough gold to rest.")
    return hp, gold

def equip_weapon():
    global equipped_weapon
    if not owned_weapons:
        print("You don't own any weapons yet. Visit the shop to buy one.")
        return

    print("\nYour owned weapons:")
    for idx, weapon in enumerate(owned_weapons, 1):
        print(f"{idx}. {weapon}")

    choice = input("Which weapon would you like to equip? Enter the number: ").strip()
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(owned_weapons):
            equipped_weapon = owned_weapons[choice - 1]
            print(f"{equipped_weapon} equipped!")
            if equipped_weapon == "Sword":
                print("The Sword increases your damage!")
            else:
                print(f"{equipped_weapon} has no special damage effects.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid input.")

def fight_monster(monster):
    global equipped_weapon  
    print(f"You encountered a {monster.name} with {monster.hp} HP!")
    
    if "Magic Scroll" in owned_weapons:  
        use_scroll = input("Use Magic Scroll to instantly defeat this monster? (y/n): ").strip().lower()
        if use_scroll == "y":
            print(f"The Magic Scroll glows and destroys the {monster.name}!")
            owned_weapons.remove("Magic Scroll")
            return "win"

    while monster.hp > 0:
        choice = input("Do you want to (1) Fight or (2) Run? ").strip()
        if choice in ["1", "fight", "f"]:
            if equipped_weapon == "Sword":
                damage = random.randint(6, 10)  
            else:
                damage = random.randint(3, 6)
            monster.hp -= damage
            print(f"You hit the {monster.name} for {damage} damage! It has {max(monster.hp, 0)} HP left.")
            if monster.hp <= 0:
                print(f"You defeated the {monster.name}!")
                return "win"
            else:
                print(f"The {monster.name} attacks you!")
                return "lose"
        elif choice in ["2", "run", "r"]:
            return "run"
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
def save_game(player_pos, player_hp, player_gold, monsters):
    data = {
        "player_pos": player_pos,
        "player_hp": player_hp,
        "player_gold": player_gold,
        "monsters": [m.to_dict() for m in monsters]
    }
    with open("savefile.json", "w") as f:
        json.dump(data, f)
    print("Game saved.")

def load_game():
    try:
        with open("savefile.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def new_random_monster():
    name = random.choice(["Sprite", "Slime", "Ghost"])
    position = (random.randint(0, 9), random.randint(0, 9)) 
    if name == "Sprite":
        color = (255, 0, 0)
        hp = 10
    elif name == "Slime":
        color = (0, 255, 0)
        hp = 15
    elif name == "Ghost":
        color = (255, 255, 0)
        hp = 20
    gold = random.randint(5, 15)
    return WanderingMonster(position, color, gold, name, hp)



def generate_monsters():
    monsters = [new_random_monster() for _ in range(2)]
    for m in monsters:
        print("spawned:", m.name)
    return monsters


def test_functions():

    print_welcome("Kate", 20)
    print_welcome("Audrey", 30)
    print_welcome("Alex", 25)

    print_shop_menu("Apple", 31, "Pear", 1.234)
    print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
    print_shop_menu("Milk", 2.5, "Cookies", 3.99)

    print(purchase_item(1.23, 10, 3))
    print(purchase_item(1.23, 2.01, 3))
    print(purchase_item(3.41, 21.12))
    print(purchase_item(31.41, 21.12))

    for _ in range(3):
        m = new_random_monster()
        print(m)

