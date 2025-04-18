#game.py
import pygame
import random
from gamefunctions import (
    print_welcome,
    create_random_monster,
    buy_item,
    equip_weapon,
    use_special_item,
    display_inventory,
)


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Adventure Game")

font = pygame.font.SysFont(None, 24)


player_x = 5
player_y = 5
tile_size = 32
player_hp = 100
player_gold = 150
inventory = []
monster_position = (random.randint(0, 19), random.randint(0, 14))
game_running = True


def draw_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))


def draw_map(player_x, player_y, monster_pos):
    screen.fill((0, 0, 0))
    for y in range(15):
        for x in range(20):
            rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            color = (50, 50, 50)
            if (x, y) == (player_x, player_y):
                color = (0, 255, 0)
            elif (x, y) == monster_pos:
                color = (255, 0, 0)
            pygame.draw.rect(screen, color, rect, 0)
            pygame.draw.rect(screen, (100, 100, 100), rect, 1)


def fight_monster(player_hp, player_gold, inventory):
    print("\nA monster appears!")
    monster = create_random_monster()
    print(f"Name: {monster['name']}")
    print(f"Description: {monster['description']}")
    print(f"Health: {monster['health']}")
    print(f"Power: {monster['power']}")

    used_item, msg = use_special_item(inventory)
    print(msg)
    if used_item:
        print("You defeated the monster instantly!")
        player_gold += monster["money"]
        return player_hp, player_gold

    weapon, weapon_msg = equip_weapon(inventory)
    print(weapon_msg)
    if weapon:
        player_attack = random.randint(50, 100)
    else:
        player_attack = random.randint(10, 40)

    monster_attack = monster["power"]
    print(f"You attack with {player_attack} power.")
    print(f"The monster attacks with {monster_attack} power.")

    if player_attack >= monster["health"]:
        print("You defeated the monster!")
        player_gold += monster["money"]
    else:
        damage = monster_attack
        print(f"The monster hit you for {damage} damage!")
        player_hp -= damage
        if player_hp <= 0:
            print("You have died.")
    return player_hp, player_gold


def run_map(player_x, player_y, player_hp, player_gold, monster_position):
    clock = pygame.time.Clock()
    running = True
    while running:
        draw_map(player_x, player_y, monster_position)
        draw_text(f"HP: {player_hp}", 10, 10)
        draw_text(f"Gold: {player_gold}", 10, 30)
        pygame.display.flip()
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return player_hp, player_gold, "quit", monster_position
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_y = max(0, player_y - 1)
                elif event.key == pygame.K_DOWN:
                    player_y = min(14, player_y + 1)
                elif event.key == pygame.K_LEFT:
                    player_x = max(0, player_x - 1)
                elif event.key == pygame.K_RIGHT:
                    player_x = min(19, player_x + 1)
                elif event.key == pygame.K_RETURN:
                    running = False
                    return player_hp, player_gold, "town", monster_position

                if (player_x, player_y) == monster_position:
                    player_hp, player_gold = fight_monster(player_hp, player_gold, inventory)
                    monster_position = (random.randint(0, 19), random.randint(0, 14))

    return player_hp, player_gold, "continue", monster_position


def town(player_gold):
    print("\nYou've entered the town.")
    display_inventory(inventory)
    print("You can buy: Sword (75g), Potion (25g), Mystical Amulet (250g)")
    choice = input("What would you like to buy? ").strip()
    if choice:
        player_gold, message = buy_item(choice, player_gold, inventory)
        print(message)
    return player_gold


def main():
    global player_x, player_y, player_hp, player_gold, monster_position

    print_welcome("Kate")
    while game_running:
        player_hp, player_gold, result, monster_position = run_map(
            player_x, player_y, player_hp, player_gold, monster_position
        )
        if result == "quit":
            break
        elif result == "town":
            player_gold = town(player_gold)


if __name__ == "__main__":
    main()

