# Function to display the menu
def print_menu():
    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")
    print()
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


# Function to retrieve the price of the selected item
def get_price(selection):
    if selection == 1:
        return 3.50
    elif selection == 2:
        return 5.25
    elif selection == 3:
        return 4.75
    elif selection == 4:
        return 2.20
    return 0.0


def main():
    ordered_items = []
    total_price = 0.0

    # Initial welcome message
    print("Welcome to Taco Palace!  Please view the menu below and make a selection")
    print()

    while True:
        print_menu()
        choice = int(input("User entered: "))
        print()

        if choice == 1:
            print("You selected a Taco")
            ordered_items.append("Taco")
            total_price += get_price(choice)
        elif choice == 2:
            print("You selected a Burrito")
            ordered_items.append("Burrito")
            total_price += get_price(choice)
        elif choice == 3:
            print("You selected Nachos")
            ordered_items.append("Nachos")
            total_price += get_price(choice)
        elif choice == 4:
            print("You selected a Drink")
            ordered_items.append("Drink")
            total_price += get_price(choice)
        elif choice == 5:
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

        print()  # Add spacing between loops

    # Format and print the summary output when user quits
    if len(ordered_items) == 0:
        print("You did not order any items. Your total is $0.00")
    else:
        # Build a human-readable list of ordered items (e.g., "a Taco, a Burrito, and a Drink")
        item_summary = ""
        if len(ordered_items) == 1:
            item_summary = f"a {ordered_items[0]}"
        elif len(ordered_items) == 2:
            item_summary = f"a {ordered_items[0]} and a {ordered_items[1]}"
        else:
            item_summary = ", ".join([f"a {item}" for item in ordered_items[:-1]]) + f", and a {ordered_items[-1]}"

        print(f"You ordered {item_summary}.  Your total is ${total_price:.2f}")


if __name__ == "__main__":
    main()
