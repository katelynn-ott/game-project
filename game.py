# game.py
import gamefunctions  # Import the gamefunctions module

def main():
    # Ask the user for their name
    player_name = input("Enter your name: ")
    
    # Call the print_welcome function from the gamefunctions module
    gamefunctions.print_welcome(player_name)
    
    # Call the print_shop_menu function to display available items
    gamefunctions.print_shop_menu("Sword", 10.99, "Potion", 2.49)
    
    # Ask the user how much money they have and call the purchase_item function
    money = float(input("Enter your available money: $"))
    num_purchased, leftover_money = gamefunctions.purchase_item(3.5, money, 3)
    print(f"Purchased {num_purchased} items. Remaining money: ${leftover_money:.2f}")
    
    # Call the create_random_monster function to generate a random monster
    random_monster = gamefunctions.create_random_monster()
    print(f"Monster: {random_monster['name']} - {random_monster['description']}")
    print(f"Health: {random_monster['health']}, Power: {random_monster['power']}, Money: {random_monster['money']}")

# This ensures the main function is called when this script is executed directly
if __name__ == "__main__":
    main()
