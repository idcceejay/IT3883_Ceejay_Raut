# Program Name: Assignment_1.py
# Course: IT3883/Section 01
# Student Name: Ceejay Raut
# Assignment Number: Lab1
# Due Date: 09/22/2026
# Purpose: A text-based menu that asks the user for an integer and stores it in
#          a list. The user can add integers, clear the list, display the list,
#          or exit the program.
# Resources: Claude (template structure, debugging hints, comment cleanup),
#            Turbo AI (learning), GitHub (code snippets for arguments and parameters)


# ---------------------------------------------------------------------------
# Input buffer
# ---------------------------------------------------------------------------
# Empty list that collects the integers the user enters when they pick option 1.
input_buffer = []


# ---------------------------------------------------------------------------
# Menu display
# ---------------------------------------------------------------------------
# Prints the menu so the user can see what they are able to do.
def show_menu():
    print("\n----Menu----")
    print("1. Add a number to the list")
    print("2. Clear the list of numbers")
    print("3. Display the list")
    print("4. Exit")


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
# Keeps showing the menu until the user chooses option 4.
while True:
    show_menu()
    # Ask the user which option they want.
    user_choice = input("\nEnter your choice (1-4): ")

    # Option 1: add an integer to the buffer
    if user_choice == "1":
        try:
            # int() raises a ValueError if the input is not a whole number.
            user_number_input = int(input("What is the integer that you want to input: "))
            # The input was a valid integer, so add it to the list.
            input_buffer.append(user_number_input)
            print(f"The number {user_number_input} has been added to the list")

        except ValueError:
            # The input was not an integer, so nothing is added.
            print("Invalid input. That is not an integer. Try again.")

    # Option 2: clear the buffer
    elif user_choice == "2":
        # Remove everything from the list, then loop back to the menu.
        input_buffer.clear()
        print("The list has been cleared")

    # Option 3: display the buffer
    elif user_choice == "3":
        # An empty list counts as False, so "not" makes this true when empty.
        if not input_buffer:
            print("There are no numbers to be listed")
        else:
            # The list has integers in it, so print it.
            print("The list of numbers is: ")
            print(input_buffer)

    # Option 4: exit the program
    elif user_choice == "4":
        print("Exiting the program...")
        # break leaves the while loop, which ends the program.
        break

    # Anything else: invalid menu choice
    else:
        # The choice was not 1-4, so tell the user and show the menu again.
        print("Invalid input. Try again.")
