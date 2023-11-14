def menu():
    print("Menu:")
    print("1. Add value")
    print("2. Edit value")
    print("3. Delete value")
    print("4. Quit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            print("Option 1 selected: Add value")
        elif choice == "2":
            print("Option 2 selected: Edit value")
        elif choice == "3":
            print("Option 3 selected: Delete value")
        elif choice == "4":
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
