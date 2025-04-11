#game.py
import pygame
import gamefunctions
import random
import json


game_state = {}

GRID_SIZE = 10
SQUARE_SIZE = 32
TOWN_SQUARE = (0, 0)  
MONSTER_SQUARE = (5, 5)  


def run_map(player_x, player_y, player_hp, player_gold, monster_position):
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE))
    pygame.display.set_caption("Adventure Game Map")

    
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    running = True
    while running:
        screen.fill(WHITE)

        
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

        
        pygame.draw.circle(screen, GREEN, (TOWN_SQUARE[0] * SQUARE_SIZE + SQUARE_SIZE // 2, TOWN_SQUARE[1] * SQUARE_SIZE + SQUARE_SIZE // 2), 12)

       
        pygame.draw.circle(screen, RED, (monster_position[0] * SQUARE_SIZE + SQUARE_SIZE // 2, monster_position[1] * SQUARE_SIZE + SQUARE_SIZE // 2), 12)

        
        pygame.draw.rect(screen, BLUE, pygame.Rect(player_x * SQUARE_SIZE, player_y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return player_hp, player_gold, "game_over", monster_position
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_y > 0:
                    player_y -= 1
                elif event.key == pygame.K_DOWN and player_y < GRID_SIZE - 1:
                    player_y += 1
                elif event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= 1
                elif event.key == pygame.K_RIGHT and player_x < GRID_SIZE - 1:
                    player_x += 1

                
                if (player_x, player_y) == TOWN_SQUARE:
                    print("You have returned to the town!")
                    pygame.quit()
                    return player_hp, player_gold, "town", monster_position

               
                elif (player_x, player_y) == monster_position:
                    print("A monster appears!")
                    player_hp, player_gold = fight_monster(player_hp, player_gold)
                    if player_hp <= 0:
                        pygame.quit()
                        return player_hp, player_gold, "game_over", monster_position
                    else:
                        print("You defeated the monster!")
                        
                        monster_position = (random.randint(1, GRID_SIZE - 1), random.randint(1, GRID_SIZE - 1))

        pygame.display.update()
    
    pygame.quit()
    return player_hp, player_gold, "town", monster_position


def save_game(state, filename="savegame.json"):
    with open(filename, "w") as f:
        json.dump(state, f, indent=4)
    print("Game saved successfully.")

def load_game(filename="savegame.json"):
    try:
        with open(filename, "r") as f:
            state = json.load(f)
        return state
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return None


inventory = []

def main():
    print("Hello and welcome to a new adventure!")

    game_state = None

    while game_state is None:
        choice = input("\nDo you want to:\n1) Start a New Game\n2) Load a Saved Game\nEnter choice: ")

        if choice == "1": 
            player_name = input("\nWhat is your name? ")
            gamefunctions.print_welcome(player_name)
        
            while True:
                print(f"Please choose your playstyle, {player_name}:")
                print("1) Knight")
                print("2) Poet")
                print("3) Witch/Warlock")
                print("4) Traveler")
                print("5) Quit")

                class_choice = input("Enter your choice: ")

                if class_choice in ["1", "2", "3", "4", "5"]:
                    break
                print("Invalid input. Please choose 1, 2, 3, 4, or 5.")

            if class_choice == "1":
                player_hp = 200
                player_gold = 45
            elif class_choice == "2":
                player_hp = 130
                player_gold = 55
            elif class_choice == "3":
                player_hp = 180
                player_gold = 40
            elif class_choice == "4":
                player_hp = 120
                player_gold = 100
            elif class_choice == "5":
                print("Thanks for playing!")
                exit()
                
            player_inventory = []  
            game_state = {"Name": player_name, "Inventory": player_inventory, "HP": player_hp, "Gold": player_gold}

            print(f"\nYour HP: {player_hp}\n")
            print(f"Your gold: {player_gold}\n")

            break
        elif choice == "2":  
            game_state = load_game()
            if game_state:
                player_name = game_state["Name"]
                player_inventory = game_state["Inventory"]
                player_hp = game_state["HP"]
                player_gold = game_state["Gold"]

                print(f"\nWelcome back, {player_name}!")
                print(f"Inventory: {player_inventory}")
                print(f"Current HP: {player_hp}, Current Gold: {player_gold}\n")
                break  
            else:
                game_state = None  

        else:
            print("Invalid choice. Please enter 1 or 2.")
        
    player_x, player_y = TOWN_SQUARE 
    monster_position = (random.randint(1, GRID_SIZE - 1), random.randint(1, GRID_SIZE - 1))  # Random initial monster position

    while True:
        print("\nYou are in town.")
        print(f"Current HP: {player_hp}, Current Gold: {player_gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Visit the tavern")
        print("4) Visit the blacksmith")
        print("5) Save and Quit")

        while True:
            action = input("Enter your choice: ")
            if action in ["1", "2", "3", "4", "5"]:
                break
            print("Invalid input. Please choose 1, 2, 3, 4, or 5.")

        if action == "1":
            player_hp, player_gold, result, monster_position = run_map(player_x, player_y, player_hp, player_gold, monster_position)
            if result == "town":
                continue
            elif result == "game_over":
                print("Game over.")
                exit()

        elif action == "2":
            if player_gold >= 5:
                player_hp = 150  
                player_gold -= 5
                print("You feel refreshed after a good rest!")
            else:
                print("Not enough gold to sleep!")
        
        elif action == "3":
            print("\nWelcome to the Tavern! Here is what's available:")
            gamefunctions.print_shop_menu("Apple", 0.45, "Milk", 0.777)
            gamefunctions.print_shop_menu("Chicken Leg", 7.22, "Stew", 6.88)

            item_choice = input("Enter the name of the item you want to buy (or 'exit' to leave): ").lower()

            if item_choice == "apple" and player_gold >= 0.45:
                player_inventory.append("Apple")
                player_gold -= 0.45
                print(f"You bought an Apple for 0.45 Gold. Remaining Gold: {player_gold}")
            elif item_choice == "milk" and player_gold >= 0.777:
                player_inventory.append("Milk")
                player_gold -= 0.777
                print(f"You bought Milk for 0.777 Gold. Remaining Gold: {player_gold}")
            elif item_choice == "chicken leg" and player_gold >= 7.22:
                player_inventory.append("Chicken Leg")
                player_gold -= 7.22
                print(f"You bought a Chicken Leg for 7.22 Gold. Remaining Gold: {player_gold}")
            elif item_choice == "stew" and player_gold >= 6.88:
                player_inventory.append("Stew")
                player_gold -= 6.88
                print(f"You bought Stew for 6.88 Gold. Remaining Gold: {player_gold}")
            elif item_choice == "exit":
                print("You leave the shop.")
            else:
                print("Not enough gold or invalid item.")

        elif action == "4":
            print("\nWelcome to the shop! Here are the available items:")
            for item, details in gamefunctions.shop_items.items():
                print(f"{item}: {details['price']} Gold")

            item_name = input("Enter the name of the item you want to buy (or 'exit' to leave): ")

            if item_name.lower() == "exit":
                print("You leave the shop.")
            else:
                player_gold, message = gamefunctions.buy_item(item_name, player_gold, inventory)
                print(message)
      
        elif action == "5":
            game_state["Inventory"] = player_inventory
            game_state["HP"] = player_hp
            game_state["Gold"] = player_gold

            print("Saving the following game state:", game_state)
            save_game(game_state)
            print("Game saved. Thanks for playing!")
            break

if __name__ == "__main__":
    main()

