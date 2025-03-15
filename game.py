# game.py
import gamefunctions  # Import the gamefunctions module

def main():
  
    player_name = input("Enter your name: ")

    gamefunctions.print_welcome(player_name)
  
    gamefunctions.print_shop_menu("Sword", 10.99, "Potion", 2.49)
  
    money = float(input("Enter your available money: $"))
    num_purchased, leftover_money = gamefunctions.purchase_item(3.5, money, 3)
    print(f"Purchased {num_purchased} items. Remaining money: ${leftover_money:.2f}")
  
    random_monster = gamefunctions.create_random_monster()
    print(f"Monster: {random_monster['name']} - {random_monster['description']}")
    print(f"Health: {random_monster['health']}, Power: {random_monster['power']}, Money: {random_monster['money']}")

if __name__ == "__main__":
    main()
